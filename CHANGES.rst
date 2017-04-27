=======
CHANGES
=======

4.0.0 (2017-04-27)
------------------

- Removed use of 'zope.testing.doctestunit' in favor of stdlib's doctest.

- Removed use of ``zope.app.testing`` in favor of ``zope.app.wsgi``.

- Add support for PyPy, Python 3.4, 3.5 and 3.6.


3.7.5 (2010-01-08)
------------------

- Move 'zope.ManageApplication' permission to zope.app.applicationcontrol

- Fix tests using a newer zope.publisher that requires zope.login.

3.7.3 (2009-11-29)
------------------

- provide a clean zope setup and move zope.app.testing to a test dependency

- removed unused dependencies like ZODB3 etc. from install_requires

3.7.2 (2009-09-10)
------------------

- Added data attribute to '_protections.zcml' for PersistentList
  and PersistentDict to accomodate UserList and UserDict behavior
  when they are proxied.

3.7.1 (2009-08-15)
------------------

- Changed globalmodules.zcml to avoid making declarations for
  deprecated standard modules, to avoid deprecation warnings.

  Note that globalmodules.zcml should be avoided.  It's better to make
  declarations for only what you actually need to use.

3.7.0 (2009-03-14)
------------------

- All interfaces, as well as some authentication-related helper classes and
  functions (checkPrincipal, PrincipalSource, PrincipalTerms, etc.) were moved
  into the new ``zope.authentication`` package. Backward-compatibility imports
  are provided.

- The "global principal registry" along with its zcml directives was moved into
  new "zope.principalregistry" package. Backward-compatibility imports are
  provided.

- The IPrincipal -> zope.publisher.interfaces.logginginfo.ILoggingInfo
  adapter was moved to ``zope.publisher``. Backward-compatibility import
  is provided.

- The PermissionsVocabulary and PermissionIdsVocabulary has been moved
  to the ``zope.security`` package. Backward-compatibility imports are
  provided.

- The registration of the "zope.Public" permission as well as some other
  common permissions, like "zope.View" have been moved to ``zope.security``.
  Its configure.zcml is now included by this package.

- The "protect" function is now a no-op and is not needed anymore, because
  zope.security now knows about i18n messages and __name__ and __parent__
  attributes and won't protect them by default.

- The addCheckerPublic was moved from zope.app.security.tests to
  zope.security.testing. Backward-compatibility import is provided.

- The ``LocalPermission`` class is now moved to new ``zope.app.localpermission``
  package. This package now only has backward-compatibility imports and
  zcml includes.

- Cleanup dependencies after refactorings. Also, don't depend on
  zope.app.testing for tests anymore.

- Update package's description to point about refactorings done.

3.6.2 (2009-03-10)
------------------

- The `Allow`, `Deny` and `Unset` permission settings was preferred to
  be imported from ``zope.securitypolicy.interfaces`` for a long time
  and now they are completely moved there from ``zope.app.security.settings``
  as well as the ``PermissionSetting`` class. The only thing left for
  backward compatibility is the import of Allow/Unset/Deny constants if
  ``zope.securitypolicy`` is installed to allow unpickling of security
  settings.

3.6.1 (2009-03-09)
------------------

- Depend on new ``zope.password`` package instead of ``zope.app.authentication``
  to get password managers for the authentication utility, thus remove
  dependency on ``zope.app.authentication``.

- Use template for AuthUtilitySearchView instead of ugly HTML
  constructing in the python code.

- Bug: The `sha` and `md5` modules has been deprecated in Python 2.6.
  Whenever the ZCML of this package was included when using Python 2.6,
  a deprecation warning had been raised stating that `md5` and `sha` have
  been deprecated. Provided a simple condition to check whether Python 2.6
  or later is installed by checking for the presense of `json` module
  thas was added only in Python 2.6 and thus optionally load the security
  declaration for `md5` and `sha`.

- Remove deprecated code, thus removing explicit dependency on
  zope.deprecation and zope.deferredimport.

- Cleanup code a bit, replace old __used_for__ statements by ``adapts``
  calls.

3.6.0 (2009-01-31)
------------------

- Changed mailing list address to zope-dev at zope.org, because
  zope3-dev is retired now. Changed "cheeseshop" to "pypi" in
  the package homepage.

- Moved the `protectclass` module to `zope.security` leaving only a
  compatibility module here that imports from the new location.

- Moved the <module> directive implementation to `zope.security`.

- Use `zope.container` instead of `zope.app.container`;.

3.5.3 (2008-12-11)
------------------

- use zope.browser.interfaces.ITerms instead of
  `zope.app.form.browser.interfaces`.

3.5.2 (2008-07-31)
------------------

- Bug: It turned out that checking for regex was not much better of an
  idea, since it causes deprecation warnings in Python 2.4. Thus let's
  look for a library that was added in Python 2.5.

3.5.1 (2008-06-24)
------------------

- Bug: The `gopherlib` module has been deprecated in Python 2.5. Whenever the
  ZCML of this package was included when using Python 2.5, a deprecation
  warning had been raised stating that `gopherlib` has been
  deprecated. Provided a simple condition to check whether Python 2.5 or later
  is installed by checking for the deleted `regex` module and thus optionally
  load the security declaration for `gopherlib`.

3.5.0 (2008-02-05)
------------------

- Feature:
  `zope.app.security.principalregistry.PrincipalRegistry.getPrincipal` returns
  `zope.security.management.system_user` when its id is used for the search
  key.

3.4.0 (2007-10-27)
------------------

- Initial release independent of the main Zope tree.
