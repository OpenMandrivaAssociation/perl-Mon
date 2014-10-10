%define modname	Mon
%define modver	0.11

Summary:	Perl-Mon module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2
Group:		Development/Perl
Url:		http://www.kernel.org/software/mon/
Source0:	ftp://ftp.kernel.org/pub/software/admin/mon/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
   
%description
This is the Perl5 module for interfacing with the Mon system monitoring
package. Currently only the client interface is implemented, but more
things like special logging routines and persistent monitors are being
considered.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES  COPYRIGHT COPYING README VERSION
%{perl_vendorlib}/Mon
%{_mandir}/man3/*

