====================  =================================================================================
Tests                 |travis| |coveralls|
--------------------  ---------------------------------------------------------------------------------
Downloads             |pip dm| |pip dw| |pip dd|
--------------------  ---------------------------------------------------------------------------------
About                 |pip license| |pip wheel| |pip pyversions| |pip implem|
--------------------  ---------------------------------------------------------------------------------
Status                |version| |status|
====================  =================================================================================

About Decorate
==============

Decorate_ takes an HTML and decorates it with style.

Currently it just support Bootstrap_, but it is built in order to allow any other framework.

MDL_ (`Material Design Lite`_) current support is very poor.


How does it work
================

It parses the HTML, uses a set of rules and creates a new HTML with new classes.

You can say: "Well... I could have done the same by using JavaScript", and you'd right. But there are some advantages in using it statically:

- It is faster. You have just to run it once.
- It can be used in third parties projects. Forget about the style from now on.
- Avoids the blink while javascript is being applied.


What was it intended for?
=========================

I was writting a static test runner, and I decided not to tie it to any style. This was a spin off. Indeed, it could be run as command line...

Usage
=====


Command line
------------

Please, run the help command with ``-h``.

Here you are a basic example::

  decorate my.html -t bootstrap -o output


Library
-------

Easy: just import and use it::

    from decorate import Decorate
    decorate = Decorate('bootstrap')
    with open('my.html') as fd:
      decorate.apply_to(fd.read(), 'output.html')

.. |travis| image:: https://img.shields.io/travis/magmax/decorate.svg
  :target: `Travis`_
  :alt: Travis results

.. |coveralls| image:: https://img.shields.io/coveralls/magmax/decorate.svg
  :target: `Coveralls`_
  :alt: Coveralls results_

.. |pip version| image:: https://img.shields.io/pypi/v/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Latest PyPI version

.. |pip dm| image:: https://img.shields.io/pypi/dm/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Last month downloads from pypi

.. |pip dw| image:: https://img.shields.io/pypi/dw/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Last week downloads from pypi

.. |pip dd| image:: https://img.shields.io/pypi/dd/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Yesterday downloads from pypi

.. |pip license| image:: https://img.shields.io/pypi/l/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: License

.. |pip wheel| image:: https://img.shields.io/pypi/wheel/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Wheel

.. |pip pyversions| image::  	https://img.shields.io/pypi/pyversions/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Python versions

.. |pip implem| image::  	https://img.shields.io/pypi/implementation/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Python interpreters

.. |status| image::	https://img.shields.io/pypi/status/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Status

.. |version| image:: https://img.shields.io/pypi/v/decorate.svg
    :target: https://pypi.python.org/pypi/decorate
    :alt: Status



.. _Travis: https://travis-ci.org/magmax/decorate
.. _Coveralls: https://coveralls.io/r/magmax/decorate

.. _@magmax9: https://twitter.com/magmax9

.. _Decorate: https://github.com/magmax/decorate
.. _Bootstrap: http://getbootstrap.com
.. _MDL: https://getmdl.io
.. _`Material Design Lite`: https://getmdl.io


