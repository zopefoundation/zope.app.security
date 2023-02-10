##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
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
"""Backward compatibility imports for zope.app.localpermission.

"""
__docformat__ = 'restructuredtext'

# BBB: the functionality was moved to zope.app.localpermission
from zope.app.localpermission.permission import NULL_ID
from zope.app.localpermission.permission import LocalPermission
from zope.app.localpermission.permission import setIdOnActivation
from zope.app.localpermission.permission import unsetIdOnDeactivation
