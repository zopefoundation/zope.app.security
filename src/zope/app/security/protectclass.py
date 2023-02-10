##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
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
"""Backward compatibility: code was moved to zope.security.protectclass.
"""
from zope.security.checker import Checker
from zope.security.checker import CheckerPublic
from zope.security.checker import defineChecker
from zope.security.checker import getCheckerForInstancesOf
from zope.security.protectclass import protectLikeUnto
from zope.security.protectclass import protectName
from zope.security.protectclass import protectSetAttribute
