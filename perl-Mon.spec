%define version	0.11
%define release	%mkrel 9
%define name 	perl-Mon
%define realname	Mon

Summary:	Perl-Mon module
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source: 	ftp://ftp.kernel.org/pub/software/admin/mon/%{realname}-%{version}.tar.bz2
URL: 		http://www.kernel.org/software/mon/
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-root/
Requires: 	perl
   
%description
This is the Perl5 module for interfacing with the Mon system monitoring
package. Currently only the client interface is implemented, but more
things like special logging routines and persistent monitors are being
considered.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%{perl_vendorlib}/Mon
%{_mandir}/*/*
%doc CHANGES  COPYRIGHT COPYING README VERSION

%clean
rm -rf $RPM_BUILD_ROOT


