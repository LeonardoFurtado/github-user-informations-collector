import argparse
import logging
from decorate import Decorate


logger = logging.getLogger(__name__)


def configure_logging(level):
    LOG_LEVELS = [logging.WARNING, logging.INFO, logging.DEBUG]
    log_level = LOG_LEVELS[min(level, len(LOG_LEVELS) - 1)]
    logging.basicConfig(
        level=log_level,
        format='[%(asctime)-15s] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )


def main():
    parser = argparse.ArgumentParser(description='Decorate HTML with themes')
    parser.add_argument(
        'source',
        default='.',
        help='Path to be processed')
    parser.add_argument(
        '-o', '--output',
        default='output',
        help='Path to leave results')
    parser.add_argument(
        '-t', '--theme',
        default="basic",
        help="Theme to be used."
    )
    parser.add_argument(
        '-v', '--verbose',
        action='count',
        default=0,
        help="Increase verbosity."
    )
    parser.add_argument(
        'action',
        default='run',
        choices=['run', 'themes'],
        nargs='?',
        help="Action to be performed"
    )
    args = parser.parse_args()
    configure_logging(args.verbose)

    decorate = Decorate(args.theme)
    if args.action == 'run':
        decorate.apply_to_dir(args.source, args.output)
        return
    if args.action == 'themes':
        themes = decorate.theme_list
        for name, props in themes.items():
            print('{name:16.16s} {path}'.format(name=name, path=props['path']))
        return

if __name__ == '__main__':
    main()
