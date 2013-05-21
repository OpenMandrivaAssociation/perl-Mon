%define upstream_name	 Mon
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl-Mon module
License:	GPL
Group:		Development/Perl
Url:		http://www.kernel.org/software/mon/
Source0:	ftp://ftp.kernel.org/pub/software/admin/mon/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch
   
%description
This is the Perl5 module for interfacing with the Mon system monitoring
package. Currently only the client interface is implemented, but more
things like special logging routines and persistent monitors are being
considered.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES  COPYRIGHT COPYING README VERSION
%{perl_vendorlib}/Mon
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.110.0-4mdv2012.0
+ Revision: 765493
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.110.0-3
+ Revision: 763988
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.110.0-2
+ Revision: 667265
- mass rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 407807
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.11-12mdv2009.1
+ Revision: 351850
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.11-11mdv2009.0
+ Revision: 223832
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.11-10mdv2008.1
+ Revision: 180486
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.11-9mdv2007.0
+ Revision: 108471
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Mon

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.11-8mdk
- own dir
- rebuild

