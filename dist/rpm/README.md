# How To Build an RPM Package

* determine which release, X.Y.Z, to package
* extract the release with `git archive --format tar --prefix mod_auth_cas-X.Y.Z/ vX.Y.Z | gzip > ~/rpmbuild/SOURCES/mod_auth_cas-X.Y.Z.tar.gz`
* copy the template, mod_auth_cas.spec to ~/rpmbuild/SPECS/mod_auth_cas-X.Y.Z.spec
* edit ~/rpmbuild/SPECS/mod_auth_cas-X.Y.Z.spec, changing X.Y.Z internally as necessary
* copy the configuration file, auth_cas.conf to ~/rpmbuild/SOURCES/auth_cas.conf
* build the source and binary packages with `rpmbuild -ba ~/rpmbuild/SPECS/mod_auth_cas-X.Y.Z.spec`
* on RHEL6, it may be necessary to provide symlinks (arguably, mod_auth_cas' autofu could be updated/improved):
    * from aclocal-1.12 to aclocal-1.11: `ln -s /usr/bin/aclocal-1.11 /usr/bin/aclocal-1.12` 
    * from automake-1.12 to automake-1.11: `ln -s /usr/bin/automake-1.11 /usr/bin/automake-1.12`
