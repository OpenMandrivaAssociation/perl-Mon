%define upstream_name	 Mon
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:	Perl-Mon module
License: 	GPL
Group: 		Development/Perl
Url: 		http://www.kernel.org/software/mon/
Source0:	ftp://ftp.kernel.org/pub/software/admin/mon/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
   
%description
This is the Perl5 module for interfacing with the Mon system monitoring
package. Currently only the client interface is implemented, but more
things like special logging routines and persistent monitors are being
considered.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES  COPYRIGHT COPYING README VERSION
%{perl_vendorlib}/Mon
%{_mandir}/*/*
