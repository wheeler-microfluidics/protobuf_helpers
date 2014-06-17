from paver.easy import task, needs
from paver.setuputils import setup, install_distutils_tasks

import version


setup(name='protobuf_helpers',
      version=version.getVersion(),
      description='Helper functions and classes for the `protobuf` package, '
      'providing, e.g., automatic generation of RPC message types based on a '
      'C++ class definition from a header file.',
      keywords='c++ clang introspection protobuf rpc',
      author='Christian Fobel',
      url='https://github.com/wheeler-microfluidics/protobuf_helpers',
      license='GPL',
      install_requires=['clang_helpers'],
      packages=['protobuf_helpers', ],
      package_data={'protobuf_helpers': ['bin/*']})


@task
@needs('generate_setup', 'minilib', 'setuptools.command.sdist')
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass
