%define app osTicket
%define pkg %(echo %{app} | tr A-Z a-z)
%define ver 1.10.2

Name:          %{pkg}
Version:       %{ver}
Release:       1%{?dist}
Summary:       PHP-based electronic support ticket system
Group:         Applications/System
License:       GPLv2
URL:           https://github.com/%{app}/%{app}
Source0:       https://github.com/%{app}/%{app}/archive/v%{version}.tar.gz#/%{name}-%{version}-%{release}.tar.gz
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:      httpd, php, php-gd, php-imap, php-mysql, php-xml

%description
osTicket is a widely-used open source support ticket system.
It seamlessly integrates inquiries created via email, phone
and web-based forms into a simple easy-to-use multi-user web
interface.

%setup -T
%install
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}/htdocs
%{__tar} -zxvf %{SOURCE0} --strip-components=1 -C %{buildroot}%{_datadir}/%{name}/htdocs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(-,apache,apache) %{_datadir}/%{name}
%attr(755,apache,apache) %{_datadir}/%{name}/htdocs/api/pipe.php

%changelog
* Sat Jun 23 2018 Taylor Kimball <tkimball@linuxhq.org> - 1.10.2-1
- Update to release 1.10.2

* Mon Dec 11 2017 Taylor Kimball <tkimball@linuxhq.org> - 1.9.16-1
- Update to release 1.9.16

* Fri May 27 2016 Taylor Kimball <tkimball@linuxhq.org> - 1.9.12-1
- Initial build
