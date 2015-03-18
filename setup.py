#!/usr/bin/env python
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from distutils.core import setup, Command

import yapf
import yapftests


class RunTests(Command):
  user_options = []

  def initialize_options(self):
    pass

  def finalize_options(self):
    pass

  def run(self):
    tests = unittest.TestSuite(yapftests.suite())
    runner = unittest.TextTestRunner()
    runner.run(tests)


with open('README.rst', 'r') as fd:
  setup(
      name='yapf',
      version=yapf.__version__,
      description='A formatter for Python code.',
      long_description=fd.read(),
      license='Apache License, Version 2.0',
      author='Google Inc.',
      maintainer='Bill Wendling',
      maintainer_email='morbo@google.com',
      packages=['yapf', 'yapf.yapflib'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Quality Assurance',
      ],
      cmdclass={
          'test': RunTests,
      },
  )