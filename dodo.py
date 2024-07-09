import shutil
import subprocess
import sys
from os import environ, makedirs, walk
from pathlib import Path
from tempfile import NamedTemporaryFile

from doit.tools import Interactive


def task_check_style():
    def run_black():
        return 'poetry run black --check src'
    def run_isort():
        return 'poetry run isort --check src'

    return {
        'actions': [
            Interactive(run_black),
            Interactive(run_isort),
        ],
        'basename': 'check-style',
        'doc': 'Python code style conformity check for Python sources'
    }


def task_test():
    def test_action():
        return 'poetry run pytest --basetemp=out/ut tests'

    return {
        'actions': [
            Interactive(test_action)
        ],
        'doc': 'Run tests'
    }


def task_build_package():
    return {
        'basename': 'build',
        'actions': [
            Interactive('poetry build'),
        ],
        'doc': 'Build package'
    }


def task_publish_package():
    def publish_package_action() -> str:
        if 'CI_USER' not in environ:
            return 'echo "CI_USER environment variable is not set!" && exit 128'

        if 'CI_PASSWORD' not in environ:
            return 'echo "CI_PASSWORD environment variable is not set!" && exit 128'

        username = environ['CI_USER']
        password = environ['CI_PASSWORD']

        return f'echo poetry publish -r <some_pypi_repo> ' \
               f'-u "{username}" -p "{password}"'

    return {
        'basename': 'publish',
        'actions': [
            Interactive(publish_package_action)
        ],
        'doc': 'Publish package to local PyPI repository (use CI_USER and CI_PASSWORD to pass credentials)'
    }


def task_cleanup():
    def clean_action() -> str:
        return 'rm -rf out .doit*.db dist __pycache__ .pytest_cache'

    return {
        'basename': 'clean',
        'actions': [
            Interactive(clean_action)
        ],
        'doc': 'Remove project output files'
    }
