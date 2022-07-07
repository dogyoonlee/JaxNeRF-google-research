# coding=utf-8
# Copyright 2022 The Google Research Authors.
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

from setuptools import setup
from distutils.command.build import build
from setuptools.command.install import install

from setuptools.command.develop import develop

import os
BASEPATH = os.path.dirname(os.path.abspath(__file__))

setup(
    name='ebp',
    py_modules=['ebp'],
    install_requires=[
        'dm-sonnet==1.23',
        'tensorflow==2.7.2',
        'numpy',
        'tqdm',
        'scipy',
        'matplotlib',
    ])
