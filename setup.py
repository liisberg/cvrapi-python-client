try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

reqs = ['requests']

setup(
    name='cvrapi-python-client',
    version='1.0',
    description='Python client for CVRAPI',
    author='Christian Liisberg',
    url='https://github.com/cliisberg/cvrapi-python-client',
    packages=['cvrapi_client'],
    license='MIT',
    install_requires=reqs)
