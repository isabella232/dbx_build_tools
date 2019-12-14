# @generated: This file was generated by bzl. Do not modify!
# Argument overrides and custom targets should be specified in BUILD.in.

package(default_visibility = ["//visibility:public"])

load("//build_tools/py:py.bzl", "dbx_py_library", "dbx_py_pypi_piplib")

dbx_py_pypi_piplib(
    name = "pytest",
    testonly = True,
    contents = {
        "cpython-27": [
            "_pytest/__init__.py",
            "_pytest/_argcomplete.py",
            "_pytest/_code/__init__.py",
            "_pytest/_code/_py2traceback.py",
            "_pytest/_code/code.py",
            "_pytest/_code/source.py",
            "_pytest/_io/__init__.py",
            "_pytest/_io/saferepr.py",
            "_pytest/_version.py",
            "_pytest/assertion/__init__.py",
            "_pytest/assertion/rewrite.py",
            "_pytest/assertion/truncate.py",
            "_pytest/assertion/util.py",
            "_pytest/cacheprovider.py",
            "_pytest/capture.py",
            "_pytest/compat.py",
            "_pytest/config/__init__.py",
            "_pytest/config/argparsing.py",
            "_pytest/config/exceptions.py",
            "_pytest/config/findpaths.py",
            "_pytest/debugging.py",
            "_pytest/deprecated.py",
            "_pytest/doctest.py",
            "_pytest/fixtures.py",
            "_pytest/freeze_support.py",
            "_pytest/helpconfig.py",
            "_pytest/hookspec.py",
            "_pytest/junitxml.py",
            "_pytest/logging.py",
            "_pytest/main.py",
            "_pytest/mark/__init__.py",
            "_pytest/mark/evaluate.py",
            "_pytest/mark/legacy.py",
            "_pytest/mark/structures.py",
            "_pytest/monkeypatch.py",
            "_pytest/nodes.py",
            "_pytest/nose.py",
            "_pytest/outcomes.py",
            "_pytest/pastebin.py",
            "_pytest/pathlib.py",
            "_pytest/pytester.py",
            "_pytest/python.py",
            "_pytest/python_api.py",
            "_pytest/recwarn.py",
            "_pytest/reports.py",
            "_pytest/resultlog.py",
            "_pytest/runner.py",
            "_pytest/setuponly.py",
            "_pytest/setupplan.py",
            "_pytest/skipping.py",
            "_pytest/stepwise.py",
            "_pytest/terminal.py",
            "_pytest/tmpdir.py",
            "_pytest/unittest.py",
            "_pytest/warning_types.py",
            "_pytest/warnings.py",
            "pytest-4.6.6.dist-info/LICENSE",
            "pytest-4.6.6.dist-info/METADATA",
            "pytest-4.6.6.dist-info/RECORD",
            "pytest-4.6.6.dist-info/WHEEL",
            "pytest-4.6.6.dist-info/entry_points.txt",
            "pytest-4.6.6.dist-info/top_level.txt",
            "pytest.py",
        ],
        "cpython-37": [
            "_pytest/__init__.py",
            "_pytest/_argcomplete.py",
            "_pytest/_code/__init__.py",
            "_pytest/_code/_py2traceback.py",
            "_pytest/_code/code.py",
            "_pytest/_code/source.py",
            "_pytest/_io/__init__.py",
            "_pytest/_io/saferepr.py",
            "_pytest/_version.py",
            "_pytest/assertion/__init__.py",
            "_pytest/assertion/rewrite.py",
            "_pytest/assertion/truncate.py",
            "_pytest/assertion/util.py",
            "_pytest/cacheprovider.py",
            "_pytest/capture.py",
            "_pytest/compat.py",
            "_pytest/config/__init__.py",
            "_pytest/config/argparsing.py",
            "_pytest/config/exceptions.py",
            "_pytest/config/findpaths.py",
            "_pytest/debugging.py",
            "_pytest/deprecated.py",
            "_pytest/doctest.py",
            "_pytest/fixtures.py",
            "_pytest/freeze_support.py",
            "_pytest/helpconfig.py",
            "_pytest/hookspec.py",
            "_pytest/junitxml.py",
            "_pytest/logging.py",
            "_pytest/main.py",
            "_pytest/mark/__init__.py",
            "_pytest/mark/evaluate.py",
            "_pytest/mark/legacy.py",
            "_pytest/mark/structures.py",
            "_pytest/monkeypatch.py",
            "_pytest/nodes.py",
            "_pytest/nose.py",
            "_pytest/outcomes.py",
            "_pytest/pastebin.py",
            "_pytest/pathlib.py",
            "_pytest/pytester.py",
            "_pytest/python.py",
            "_pytest/python_api.py",
            "_pytest/recwarn.py",
            "_pytest/reports.py",
            "_pytest/resultlog.py",
            "_pytest/runner.py",
            "_pytest/setuponly.py",
            "_pytest/setupplan.py",
            "_pytest/skipping.py",
            "_pytest/stepwise.py",
            "_pytest/terminal.py",
            "_pytest/tmpdir.py",
            "_pytest/unittest.py",
            "_pytest/warning_types.py",
            "_pytest/warnings.py",
            "pytest-4.6.6.dist-info/LICENSE",
            "pytest-4.6.6.dist-info/METADATA",
            "pytest-4.6.6.dist-info/RECORD",
            "pytest-4.6.6.dist-info/WHEEL",
            "pytest-4.6.6.dist-info/entry_points.txt",
            "pytest-4.6.6.dist-info/top_level.txt",
            "pytest.py",
        ],
    },
    pip_main = "py.test",
    pip_version = "4.6.6",
    python2_compatible = True,
    python3_compatible = True,
    setup_requires = ["//pip/setuptools_scm"],
    deps = [
        "//pip/atomicwrites",
        "//pip/attrs",
        "//pip/funcsigs",
        "//pip/importlib-metadata",
        "//pip/more_itertools",
        "//pip/packaging",
        "//pip/pathlib2",
        "//pip/pluggy",
        "//pip/py",
        "//pip/six",
        "//pip/wcwidth",
    ],
)

# Library used in dbx_py_pytest_test to prevent duplicate deps.
dbx_py_library(
    name = "pytest_fake",
    testonly = True,
    srcs = [],
    autogen_deps = False,
    python2_compatible = True,
    python3_compatible = True,
    validate = "strict",
    deps = [":pytest"],
)