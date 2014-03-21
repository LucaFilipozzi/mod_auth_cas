Name:           mod_auth_cas
Version:        X.Y.Z
Release:        1%{?dist}
Summary:        Apache 2.0/2.2 compliant module that supports the CASv1 and CASv2 protocols

Group:          System Environment/Daemons
License:        GPLv3+ with exceptions
URL:            https://github.com/LucaFilipozzi/mod_auth_cas
# git archive --format tar --prefix mod_auth_cas-X.Y.Z/ vX.Y.Z | gzip > ../mod_auth_cas-X.Y.Z.tar.gz
Source0:        mod_auth_cas-X.Y.Z.tar.gz
Source1:        auth_cas.conf

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  openssl-devel
BuildRequires:  httpd-devel
BuildRequires:  libcurl-devel

Requires:       httpd

%description
mod_auth_cas is an Apache 2.0/2.2 compliant module that supports the CASv1
and CASv2 protocols

%prep
%setup -q

%build
%configure --with-apxs=%{_sbindir}/apxs
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}/
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/auth_cas.conf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/httpd/modules/*.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf

%changelog
* Sun Mar 16 2014 <luca.filipozzi@gmail.com> - 1.0.10.ubc-1
- updated to mod_auth_cas-1.0.10.ubc.tar.gz

* Tue Nov 09 2011 <jehan.procaccia@it-sudparis.eu> - 1.0.9.1-1
- updated to mod_auth_cas-1.0.9.1.tar.gz
- updated build centos from openssl-1.0.0-4.el6_0.2.i686 to openssl-1.0.0-10.el6_1.5.i686

* Tue Jun 29 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-2
- Fixed svn export link, upstream changed canonical URL names.

* Wed Apr 28 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-1
- added requires of httpd 
- fixed mixed use of macros
- updated to latest version

* Fri Aug 07 2009 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8-1
- First attempt to package mod_auth_cas for Fedora

