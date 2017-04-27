##############################################################################
#
# Copyright (c) 2003 Zope Foundation and Contributors.
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
"""Persistent List functional tests.
"""

Let's check that we can access the data attribute of a proxied
PersistentList. This is to accomodate UserList operations which are
used when an isinstance call will correctly identify a persistent list
as a UserList. Some configurations may get incorrect behavior currently,
such that isinstance claims that a proxied UserList is not a UserList.
For these configurations this should not make a difference.

Because several UserList methods use this isinstance check before
accessing the data attribute we will simply try to get the data
attribute from a proxied example.
    
    >>> import persistent.list
    >>> import zope.security.tests.test_proxy
    >>> import zope.security.proxy

    >>> persistent_list = persistent.list.PersistentList()

    >>> proxied_list = zope.security.proxy.ProxyFactory(
    ...     persistent_list)

    >>> proxied_list.data
    []

We'll do the same with a persistent dict, which follows the same
behavior pattern with UserDict.

    >>> import persistent.dict
    >>> persistent_dict = persistent.dict.PersistentDict()

    >>> proxied_dict = zope.security.proxy.ProxyFactory(
    ...     persistent_dict)

    >>> proxied_dict.data
    {}
    
