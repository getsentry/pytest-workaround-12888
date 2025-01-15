from __future__ import annotations

import os.path

from setuptools.command.install import install as _install
from setuptools import setup


class install(_install):
    def initialize_options(self):
        _install.initialize_options(self)
        self.extra_path = (self.distribution.metadata.name, 'import readline')

    def finalize_options(self):
        _install.finalize_options(self)

        install_suffix = os.path.relpath(
            self.install_lib, self.install_libbase,
        )
        if install_suffix == '.':
            pass  # skipping install of .pth during easy-install
        elif install_suffix == self.extra_path[1]:
            self.install_lib = self.install_libbase
        else:
            raise AssertionError(
                'unexpected install_suffix',
                self.install_lib, self.install_libbase, install_suffix,
            )


setup(cmdclass={'install': install})
