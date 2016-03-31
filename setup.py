# Auto generated by ct-mksetup
# Do not edit this file, edit ./project.py instead

from setuptools import setup
setup(
    **{   'author': 'Tim Diels',
    'author_email': 'timdiels.m@gmail.com',
    'classifiers': [   'Natural Language :: English',
                       'Intended Audience :: Developers',
                       'Development Status :: 3 - Alpha',
                       'Topic :: Software Development',
                       'Topic :: Software Development :: Libraries',
                       'Operating System :: POSIX',
                       'Operating System :: POSIX :: AIX',
                       'Operating System :: POSIX :: BSD',
                       'Operating System :: POSIX :: BSD :: BSD/OS',
                       'Operating System :: POSIX :: BSD :: FreeBSD',
                       'Operating System :: POSIX :: BSD :: NetBSD',
                       'Operating System :: POSIX :: BSD :: OpenBSD',
                       'Operating System :: POSIX :: GNU Hurd',
                       'Operating System :: POSIX :: HP-UX',
                       'Operating System :: POSIX :: IRIX',
                       'Operating System :: POSIX :: Linux',
                       'Operating System :: POSIX :: Other',
                       'Operating System :: POSIX :: SCO',
                       'Operating System :: POSIX :: SunOS/Solaris',
                       'Operating System :: Unix',
                       'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                       'Programming Language :: Python',
                       'Programming Language :: Python :: 3',
                       'Programming Language :: Python :: 3 :: Only',
                       'Programming Language :: Python :: 3.2',
                       'Programming Language :: Python :: 3.3',
                       'Programming Language :: Python :: 3.4',
                       'Programming Language :: Python :: 3.5',
                       'Programming Language :: Python :: Implementation',
                       'Programming Language :: Python :: Implementation :: CPython',
                       'Programming Language :: Python :: Implementation :: Stackless'],
    'description': 'Python 3 utility library',
    'extras_require': {   'algorithms': ['numpy', 'scipy', 'scikit-learn', 'collections-extended'],
                          'cli': ['click'],
                          'data_frame': ['numpy', 'pandas'],
                          'debug': ['psutil'],
                          'dev': ['sphinx-rtd-theme', 'sphinx', 'numpydoc'],
                          'dict': ['more-itertools'],
                          'http': ['requests'],
                          'pymysql': ['pymysql'],
                          'pyqt': [],
                          'test': [   'pytest',
                                      'pytest-xdist',
                                      'pytest-env',
                                      'pytest-cov',
                                      'coverage-pth',
                                      'pytest-mock',
                                      'pytest-localserver',
                                      'pytest-capturelog']},
    'human_friendly_name': 'Chicken Turtle Util',
    'install_requires': [],
    'keywords': 'development util library',
    'license': 'LGPL3',
    'long_description': 'Chicken Turtle Util (CTU) provides an API of various Python utility\n'
                        'functions.\n'
                        '\n'
                        'Chicken Turtle Util is alpha. None of the interface is stable (yet),\n'
                        'meaning it may change in the future.\n'
                        '\n'
                        'Chicken Turtle Util offers a variety of features, as such we kept most\n'
                        'dependencies optional. When using a module, add/install its\n'
                        'dependencies, listed in its corresponding ``*_requirements.in`` file\n'
                        'found in the root of the project; e.g.\n'
                        '`cli\\_requirements.in '
                        '<https://github.com/timdiels/chicken_turtle_util/blob/master/cli_requirements.in>`__\n'
                        'lists the dependencies of ``chicken_turtle_util.cli``.\n'
                        '\n'
                        'Feature overview:\n'
                        '\n'
                        '-  ``algorithms.spread_points_in_hypercube``: Place ``n`` points in a\n'
                        '   unit hypercube such that the minimum distance between points is\n'
                        '   approximately maximal\n'
                        '-  ``algorithms.multi_way_partitioning``: Greedily divide weighted items\n'
                        '   equally across bins (multi-way partition problem)\n'
                        '-  ``data_frame`` and ``series``: `pandas <http://pandas.pydata.org/>`__\n'
                        '   utility functions\n'
                        '-  ``data_frame.replace_na_with_none``: Replace ``NaN`` values in\n'
                        '   ``DataFrame`` with ``None``\n'
                        '-  ``data_frame.split_array_like``: Split cells with ``array_like``\n'
                        '   values along row axis.\n'
                        '-  ``series.invert``: Swap index with values of series\n'
                        '-  ``dict``: dictionary utilities:\n'
                        '-  ``invert``: Invert dict by swapping each value with its key\n'
                        '-  ``DefaultDict``: Like ``collections.defaultdict``, but its value\n'
                        '   factory function takes a key argument, e.g.\n'
                        '   ``DefaultDict(lambda key: MyClass(key))``\n'
                        "-  ``pretty_print_head``: Pretty print the 'first' lines of a dict\n"
                        '-  ``function.compose``: Compose functions\n'
                        '-  ``http.download``: Download http resource (using ``requests``) and\n'
                        '   save to file name suggested by HTTP server\n'
                        '-  ``iterable.sliding_window``: Iterate using a sliding window\n'
                        '-  ``iterable.partition``: Split iterable into partitions\n'
                        '-  ``iterable.is_sorted``: Get whether iterable is sorted ascendingly\n'
                        '-  ``iterable.flatten``: Flatten shallowly zero or more times\n'
                        '-  ``set.merge_by_overlap``: Of a list of sets, merge those that\n'
                        '   overlap, in place\n'
                        '-  ``logging.set_level``: Context manager to temporarily change log\n'
                        '   level of logger\n'
                        '-  ``cli``: extensions to `click <http://click.pocoo.org/>`__ for\n'
                        '   building CLI applications\n'
                        '-  ``pyqt.block_signals``: Context manager to temporarily turn on\n'
                        '   ``QObject.blockSignals``\n'
                        '-  ``sqlalchemy.log_sql``: Context manager to temporarily log sql\n'
                        '   statements emitted by `sqlalchemy <http://www.sqlalchemy.org/>`__\n'
                        '-  ``various.Object``: Like ``object``, but does not raise given args to\n'
                        '   ``__init__``\n'
                        '\n'
                        'Links\n'
                        '-----\n'
                        '\n'
                        '-  `Documentation <http://pythonhosted.org/chicken_turtle_util/>`__\n'
                        '-  `PyPI <https://pypi.python.org/pypi/chicken_turtle_util/>`__\n'
                        '-  `GitHub <https://github.com/timdiels/chicken_turtle_util/>`__\n'
                        '\n'
                        'Developer guide\n'
                        '---------------\n'
                        '\n'
                        'Docstrings type language\n'
                        '~~~~~~~~~~~~~~~~~~~~~~~~\n'
                        '\n'
                        'Docstrings must follow `NumPy\n'
                        'style <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt#sections>`__\n'
                        '\n'
                        "When using someone else's code or idea, give credit in a comment in the\n"
                        'source file, not in the documentation.\n'
                        '\n'
                        'When describing a type (e.g. in the Parameters section), do so in the\n'
                        'type language described below.\n'
                        '\n'
                        'You can use these pseudo-types:\n'
                        '\n'
                        '-  iterable: something you can iterate over once (or more) using\n'
                        '   ``iter``\n'
                        '-  iterator: something you can call ``next`` on\n'
                        '-  collection: something you can iterate over multiple times\n'
                        '\n'
                        'The rest of the type language is described by example::\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    pathlib.Path\n'
                        '\n'
                        'Expects a ``pathlib.Path``-like, i.e. anything that looks like a\n'
                        '``pathlib.Path`` (duck typing) is allowed. None is not allowed.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    exact(pathlib.Path)\n'
                        '\n'
                        'Expects a ``Path`` or derived class instance, so no duck typing (and no\n'
                        'None).\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    pathlib.Path or None\n'
                        '\n'
                        'Expect a ``pathlib.Path``-like or None. When None is allowed it must be\n'
                        'explicitly specified like this.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    bool or int\n'
                        '\n'
                        'Expect a boolean or an int.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    {bool}\n'
                        '\n'
                        'A set of booleans.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    {any}\n'
                        '\n'
                        'A set of anything.\n'
                        '\n'
                        '::\n'
                        '\n'
                        "    {'apples' => bool, 'name' => str}\n"
                        '\n'
                        "A dictionary with keys 'apples' and 'name' which respectively have a\n"
                        'boolean and a string as value. (Note that the ``:`` token is already\n'
                        'used by Sphinx, and ``->`` is usually used for lambdas, so we use ``=>``\n'
                        'instead)\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    dict(apples=bool, name=str)\n'
                        '\n'
                        'Equivalent to the previous example.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    Parameters\n'
                        '    ----------\n'
                        '    field : str\n'
                        '    dict_ : {field => bool}\n'
                        '\n'
                        'A dictionary with one key, specified by the value of ``field``, another\n'
                        'parameter (but can be any expression, e.g. a global).\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    {apples => bool, name => str}\n'
                        '\n'
                        'Not equivalent to the apples dict earlier. ``apples`` and ``name`` are\n'
                        'references to the value used as a key.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    (bool,)\n'
                        '\n'
                        'Tuple of a single bool.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    [bool]\n'
                        '\n'
                        'List of 0 or more booleans.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    [(bool, bool)]\n'
                        '\n'
                        'List of tuples of boolean pairs.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    [(first :: bool, second :: bool)]\n'
                        '\n'
                        'Equivalent type compared to the previous example, but you can more\n'
                        'easily refer to the first and second bool in your parameter description\n'
                        'this way.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    {item :: int}\n'
                        '\n'
                        'Set of int. We can refer to the set elements as ``item``.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    iterable(bool)\n'
                        '\n'
                        'Iterable of bool. Something you can call ``iter`` on.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    iterator(bool)\n'
                        '\n'
                        'Iterator of bool. Something you can call ``next`` on.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    type_of(expression)\n'
                        '\n'
                        'Type of expression, avoid when possible in order to be as specific as\n'
                        'possible.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    Parameters\n'
                        '    ----------\n'
                        '    a : SomeType\n'
                        '    b : type_of(a.nodes[0].key_function)\n'
                        '\n'
                        '``b`` has the type of the retrieved function.\n'
                        '\n'
                        '::\n'
                        '\n'
                        '    (int, str, k=int) -> bool\n'
                        '\n'
                        'Function that takes an int and a str as positional args, an int as\n'
                        "keyword arg named 'k' and returns a bool.\n"
                        '\n'
                        '::\n'
                        '\n'
                        '    func :: int -> bool\n'
                        '\n'
                        'Function that takes an int and returns a bool. We can refer to it as\n'
                        '``func``.\n'
                        '\n'
                        'Project decisions\n'
                        '~~~~~~~~~~~~~~~~~\n'
                        '\n'
                        'API design\n'
                        '^^^^^^^^^^\n'
                        '\n'
                        "If it's a path, expect a ``pathlib.Path``, not a ``str``.\n"
                        '\n'
                        'If extending a module from another project, e.g. ``pandas``, use the\n'
                        'same name as the module. While a ``from pandas import *`` would allow\n'
                        'the user to access functions of the real pandas module through the\n'
                        'extended module, we have no control over additions to the real pandas,\n'
                        "which could lead to name clashes later on, so don't.\n"
                        '\n'
                        'Decorators and context managers should not be provided directly but\n'
                        'should be returned by a function. This avoids confusion over whether or\n'
                        'not parentheses should be used ``@f`` vs ``@f()``, and parameters can\n'
                        'easily be added in the future.\n'
                        '\n'
                        'If a module is a collection of instances of something, give it a plural\n'
                        'name, else make it singular. E.g. ``exceptions`` for a collection of\n'
                        '``Exception`` classes, but ``function`` for a set of related functions\n'
                        'operating on functions.\n'
                        '\n'
                        'API implementation\n'
                        '^^^^^^^^^^^^^^^^^^\n'
                        '\n'
                        'Do not prefix imports with underscore. When importing things, they also\n'
                        'are exported, but ``help`` or Sphinx documentation will not include them\n'
                        'and thus a user should realise they should not be used. E.g.\n'
                        '``import numpy as np`` in ``module.py`` can be accessed with\n'
                        "``module.np``, but it isn't mentioned in ``help(module)`` or Sphinx\n"
                        'documentation.\n',
    'name': 'chicken_turtle_util',
    'package_data': {},
    'packages': ['chicken_turtle_util', 'chicken_turtle_util.test'],
    'url': 'https://github.com/timdiels/chicken_turtle_util',
    'version': '0.0.0'}
)
