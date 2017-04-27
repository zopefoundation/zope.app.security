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
"""Login and Logout screens
"""

try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote

from zope import component
from zope.app.pagetemplate import ViewPageTemplateFile
from zope.app.publisher.interfaces.http import ILogin
from zope.authentication.interfaces import IAuthentication
from zope.authentication.interfaces import IUnauthenticatedPrincipal
from zope.authentication.interfaces import ILogout, ILogoutSupported
from zope.i18n import translate
from zope.interface import implementer

from zope.app.security.i18n import _


class AuthUtilitySearchView(object):

    template = ViewPageTemplateFile('authutilitysearchview.pt')
    searchTitle = u'principals.zcml'

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def render(self, name):
        return self.template(title=self.searchTitle, name=name)

    def results(self, name):
        if (name + '.search') not in self.request:
            return None
        searchstring = self.request[name + '.searchstring']
        return [principal.id
                for principal in self.context.getPrincipals(searchstring)]

@implementer(ILogin)
class HTTPAuthenticationLogin(object):

    confirmation = ViewPageTemplateFile('login.pt')

    failed = ViewPageTemplateFile('login_failed.pt')

    def login(self, nextURL=None):
        # we don't want to keep challenging if we're authenticated
        if IUnauthenticatedPrincipal.providedBy(self.request.principal):
            component.getUtility(IAuthentication).unauthorized(
                self.request.principal.id, self.request)
            return self.failed()
        else:
            return self._confirm(nextURL)

    def _confirm(self, nextURL):
        if nextURL is None:
            return self.confirmation()
        self.request.response.redirect(nextURL)


class HTTPBasicAuthenticationLogin(HTTPAuthenticationLogin):
    """Issues a challenge to the browser to get basic auth credentials.

    This view can be used as a fail safe login in the even the normal login
    fails because of an improperly configured authentication utility.

    The failsafeness of this view relies on the fact that the global principal
    registry, which typically contains an adminitrator principal, uses basic
    auth credentials to authenticate.
    """

    def login(self, nextURL=None):
        # we don't want to keep challenging if we're authenticated
        if IUnauthenticatedPrincipal.providedBy(self.request.principal):
            # hard-code basic auth challenge
            self.request.unauthorized('basic realm="Zope"')
            return self.failed()
        else:
            return self._confirm(nextURL)

@implementer(ILogout)
class HTTPAuthenticationLogout(object):
    """Since HTTP Authentication really does not know about logout, we are
    simply challenging the client again."""

    confirmation = ViewPageTemplateFile('logout.pt')

    redirect = ViewPageTemplateFile('redirect.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def logout(self, nextURL=None):
        if not IUnauthenticatedPrincipal.providedBy(self.request.principal):
            auth = component.getUtility(IAuthentication)
            ILogout(auth).logout(self.request)
            if nextURL:
                return self.redirect()
        if nextURL is None:
            return self.confirmation()
        else:
            return self.request.response.redirect(nextURL)


class LoginLogout(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        if IUnauthenticatedPrincipal.providedBy(self.request.principal):
            return u'<a href="@@login.html?nextURL=%s">%s</a>' % (
                quote(self.request.getURL()),
                translate(_('[Login]'), context=self.request,
                          default='[Login]'))

        if ILogoutSupported(self.request, None) is not None:
            return u'<a href="@@logout.html?nextURL=%s">%s</a>' % (
                quote(self.request.getURL()),
                translate(_('[Logout]'), context=self.request,
                          default='[Logout]'))

        return None
