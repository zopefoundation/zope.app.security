##############################################################################
#
# Copyright (c) 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Principals.

$Id: principal.py,v 1.6 2004/03/08 12:06:01 srichter Exp $
"""
from zope.exceptions import NotFoundError
from zope.app import zapi
from zope.app.services.servicenames import Authentication

def checkPrincipal(context, principal_id):

    try:
        if zapi.getService(context, Authentication).getPrincipal(principal_id):
            return
    except NotFoundError:
        pass
    
    raise ValueError("Undefined principal id", principal_id)
