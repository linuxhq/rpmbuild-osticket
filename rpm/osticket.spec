Name:          osTicket
Version:       1.9.16
Release:       1%{?dist}
Summary:       PHP-based electronic support ticket system
Group:         Applications/System
License:       GPLv2
URL:           http://osticket.com
Source0:       http://osticket.com/sites/default/files/download/%{name}-v%{version}.zip
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:      httpd, php, php-gd, php-imap, php-mysql, php-xml

%description
osTicket is a widely-used open source support ticket system.
It seamlessly integrates inquiries created via email, phone
and web-based forms into a simple easy-to-use multi-user web
interface.

%prep
%setup -n upload
%build

%install
%{__install} -d -m 0755 %{buildroot}%{_datadir}/%{name}/htdocs
%{__mv} -f * %{buildroot}%{_datadir}/%{name}/htdocs

%clean
%{__rm} -rf %{buildroot}

%files
%doc setup/scripts/
%defattr(-,root,root,-)
%attr(-,apache,apache) %{_datadir}/%{name}
%attr(755,apache,apache) %{_datadir}/%{name}/htdocs/api/pipe.php

%changelog
* Mon Dec 11 2017 Taylor Kimball <tkimball@linuxhq.org> - 1.9.16-1
- Update to release 1.9.16

* Fri May 27 2016 Taylor Kimball <tkimball@linuxhq.org> - 1.9.12-1
- Initial build
