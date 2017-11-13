%global httpd httpd24u
%global module mod_myfixip

Summary:	Apache module to fix remote_ip
Name:		%{httpd}-%{module}
Version:	1.4
Release:	1.ius%{?dist}
Group:		System Environment/Daemons
License:	ASL 2.0
URL:		https://github.com/ggrandes/apache22-modules
Source0:	https://github.com/ggrandes/apache22-modules/raw/45702c92df432720b6af523930ce1386a7492466/%{module}.c
Source1:	10-myfixip.conf
BuildRequires:	%{httpd}-devel
Requires:	%{httpd}, httpd-mmn = %{_httpd_mmn}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Conflicts:	%{module}

%description
%{module} fixes "remote_ip" in HTTP/HTTPS (PROXY protocol, like ha-proxy and
Amazon ELB).

%prep
head -102 %{SOURCE0} >> README

%build
%{_httpd_apxs} -c %{SOURCE0}

%install
mkdir -p %{buildroot}/%{_httpd_moddir}
%{_httpd_apxs} -i -S LIBEXECDIR=%{buildroot}/%{_httpd_moddir} -n %{module} ../SOURCES/%{module}.la
mkdir -p %{buildroot}/%{_httpd_modconfdir}
cp -p %SOURCE1 %{buildroot}/%{_httpd_modconfdir}

%clean
rm -rf %{buildroot}

%files
%doc README
%config(noreplace) %{_httpd_modconfdir}/10-myfixip.conf
%{_httpd_moddir}/%{module}.so

%changelog
* Tue Nov 07 2017 Ben Harper <ben.harper@rackspace.com> - 1.4-1.ius
- initial package
