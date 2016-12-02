"""
Python API client for GOV.UK Notify
"""
import re
import ast
import pip.download
from pip.req import parse_requirements
from setuptools import setup, find_packages

# can't just import notifications_python_client.version as requirements may not be installed yet and imports will fail
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('notifications_python_client/version.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

def get_reqs(requirement_file):
    requirements = list(parse_requirements(requirement_file, session=pip.download.PipSession()))
    return [str(r.req) for r in requirements]

install_requires = get_reqs('requirements.txt')
tests_require = get_reqs('requirements_for_test.txt')
# for running pytest as `python setup.py test`, see
# http://doc.pytest.org/en/latest/goodpractices.html#integrating-with-setuptools-python-setup-py-test-pytest-runner
setup_requires = ['pytest-runner']

setup(
    name='notifications-python-client',
    version=version,
    url='https://github.com/alphagov/notifications-python-client',
    license='MIT',
    author='Government Digital Service',
    description='Python API client for GOV.UK Notify.',
    long_description=__doc__,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # TODO: Get tests running for other versions of python
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='gds govuk notify',

    packages=find_packages(),
    include_package_data=True,

    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
