Summary: Browser default start page for GoOSe Linux
Name: goose-indexhtml
Version: 6
Release: 1%{?dist}
Source: %{name}-%{version}.tar.gz
License: BSD
Group: Documentation
BuildArchitectures: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Obsoletes: indexhtml <= 2:5-1
Provides: redhat-indexhtml

%description
The indexhtml package contains the welcome page shown by your Web browser,
which you'll see after you've successfully installed GoOSe Linux.

%prep
%setup -q -n HTML

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML
cp -a . $RPM_BUILD_ROOT/%{_defaultdocdir}/HTML/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_defaultdocdir}/HTML/*

%changelog
* Wed Aug 17 2011 Mike Adams <shalkie@gooselinux.org> 4-0.1
- initial build for GoOSe Linux 6
- Removed previous indexhtml tar file and wholly replaced.
