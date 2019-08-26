import os
import shutil
import logging
import json
from lxml import etree
from lxml.cssselect import CSSSelector
try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO
try:
    import yaml
except ImportError:
    yaml = None


logger = logging.getLogger(__name__)


class DecorateException(Exception):
    pass


class NotFoundThemeDecorateException(DecorateException):
    pass


class Decorate(object):
    def __init__(self, theme_name):
        self.name = theme_name
        self._themes = None
        self._config = None
        self._theme_path = None
        self._additional_css = []
        self._additional_js = []

    @property
    def css(self):
        return self.config['css'] or []

    @property
    def javascript(self):
        return self.config['js'] or []

    @property
    def mutators(self):
        return self.config.get('classes') or {}

    def add_css(self, css):
        self._additional_css.append(css)

    def add_js(self, js):
        self._additional_js.append(js)

    def apply_to_dir(self, source, target):
        if not os.path.exists(target):
            os.makedirs(target)
        for root, dirs, files in os.walk(source):
            for filename in files:
                with open(os.path.join(source, filename)) as fd:
                    content = fd.read()
                with open(os.path.join(target, filename), 'w+') as fd:
                    fd.write(self.apply_to(content))

    def apply_to(self, html):
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(html), parser)
        root = tree.getroot()
        head = root.find('head')
        if head is None:
            head = etree.Element("head")
            root.insert(0, head)

        body = root.find('body')
        if body is None:
            body = etree.Element("body")
            root.append(body)

        for selector, classes in self.mutators.items():
            sel = CSSSelector(selector)
            for el in sel(tree):
                base = el.attrib.get('class', '').split()
                if "decorate-hook" in base:
                    index = base.index("decorate-hook")
                    pre = base[:index]
                    post = base[index:]
                    v = pre + classes + post
                else:
                    v = base + classes
                el.attrib['class'] = ' '.join(v)

        for css in self.css + self._additional_css:
            item = etree.Element(
                'link',
                dict(
                    rel="stylesheet",
                    href=css,
                ),
            )
            item.text = ''
            head.append(item)

        for js in self.javascript + self._additional_js:
            item = etree.Element(
                'script',
                dict(
                    rel="src",
                    src=js,
                )
            )
            item.text = ''
            head.append(item)
        # fix textareas
        for el in CSSSelector('textarea')(tree):
            if not el.text:
                el.text = ''
        return etree.tostring(tree).decode()

    @property
    def theme_list(self):
        if self._themes is None:
            result = {}
            for name, processor, spec, path in self._theme_discover():
                new_name = name
                c = 1
                while new_name in result:
                    new_name = '%s_%d' % (name, c)
                    c += 1
                result[new_name] = {
                    'processor': processor,
                    'spec': spec,
                    'path': path,
                }
            self._themes = result
        return self._themes

    def _theme_discover(self):
        processor = None
        current_path = os.path.abspath(os.path.join('.', 'themes'))
        user_home_path = os.path.join(os.path.expanduser('~'),
                                      'decorate', 'themes')
        default_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'themes')
        )
        for path in [current_path, user_home_path, default_path]:
            logger.debug("Searching for themes in %s", path)
            if not os.path.exists(path):
                logger.debug("Theme path does not exist. Ignoring")
                continue
            for name in os.listdir(path):
                fullpath = os.path.join(path, name)
                if not os.path.isdir(fullpath):
                    continue
                processor = self._get_processor(fullpath)
                if processor is None:
                    continue
                yield name, processor[0], processor[1], fullpath

    def _get_processor(self, path):
        for ext, processor in (('json', json), ('yaml', yaml), ('yml', yaml)):
            fullpath = os.path.join(path, 'spec.%s' % ext)
            if os.path.exists(fullpath):
                return processor, fullpath
        return None

    def _load_theme(self):
        if self.name not in self.theme_list:
            raise NotFoundThemeDecorateException()
        theme = self.theme_list[self.name]

        with open(theme['spec']) as fd:
            self._config = theme['processor'].load(fd)
            self._theme_path = theme['path']

    @property
    def config(self):
        if self._config is None:
            self._load_theme()
        return self._config

    def copy_assets(self, output):
        for asset in self.css + self.javascript:
            if not asset.startswith(('http://', 'https://')):
                shutil.copyfile(os.path.join(self._theme_path, asset), output)
        for asset in self._additional_css + self._additional_js:
            if not asset.startswith(('http://', 'https://')):
                filename = os.path.basename(asset)
                shutil.copyfile(asset, os.path.join(output, filename))
