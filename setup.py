##############################################################################
#
# Copyright (c) Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################

version = '4.0.1.dev0'

import os
from setuptools import setup, find_packages

def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()

test_requires = [
    'zope.app.wsgi',
    'zope.testrunner',
    'webtest',
]

setup(name='zope.app.security',
      version=version,
      author='Zope Foundation and Contributors',
      author_email='zope-dev@zope.org',
      description='ZMI Views For Zope3 Security Components',
      long_description=(
          read('README.rst')
          + '\n\n' +
          'Detailed Documentation\n' +
          '======================\n'
          + '\n\n' +
          read('src', 'zope', 'app', 'security', 'browser',
               'authutilitysearchview.rst')
          + '\n\n' +
          read('src', 'zope', 'app', 'security', 'browser', 'loginlogout.rst')
          + '\n\n' +
          read('CHANGES.rst')
          ),
      keywords="zope security authentication principal ftp http",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'
      ],
      url='http://github.com/zopefoundation/zope.app.security',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      extras_require={
          'test': test_requires,
      },
      tests_require=test_requires,
      install_requires=[
          'setuptools',
          'zope.app.localpermission',
          'zope.app.pagetemplate',
          'zope.app.publisher',
          'zope.authentication',
          'zope.i18n',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.principalregistry',
          'zope.publisher >= 4.3.1',
          'zope.security',
          'zope.securitypolicy',
          'zope.login',
      ],
      include_package_data=True,
      zip_safe=False,
)
