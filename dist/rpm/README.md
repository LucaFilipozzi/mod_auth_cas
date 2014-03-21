# How To Build an RPM Package

* determine which release, X.Y.Z, to package
* extract the release with `git archive --format tar --prefix mod_auth_cas-X.Y.Z/ vX.Y.Z | gzip > ~/rpmbuild/SOURCES/mod_auth_cas-X.Y.Z.tar.gz`
* copy the template, mod_auth_cas.spec to ~/rpmbuild/SPECS/mod_auth_cas-X.Y.Z.spec
* edit ~/rpmbuild/SPECS/mod_auth_cas-X.Y.Z.spec, changing X.Y.Z internally as necessary
* copy the configuration file, auth_cas.conf to ~/rpmbuild/SOURCES/auth_cas.conf
* build the source and binary packages with `rpmbuild -ba ~/rpmbuild/SPECS/mod_auth_cas-X.Y.Z.spec`
