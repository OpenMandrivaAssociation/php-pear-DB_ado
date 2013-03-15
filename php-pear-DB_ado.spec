%define		_class		DB
%define		_subclass	ado
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.1
Release:	8
Summary:	DB driver which use MS ADODB library
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/DB_ado/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
DB_ado is a database independent query interface definition for
Microsoft's ADODB library using PHP's COM extension. This class allows
you to connect to different data sources like MS Access, MS SQL
Server, Oracle and other RDBMS on a Win32 operating system. Moreover
the possibility exists to use MS Excel spreadsheets, XML, text files
and other not relational data as data source.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-6mdv2012.0
+ Revision: 741846
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-5
+ Revision: 679290
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.1-4mdv2011.0
+ Revision: 613631
- the mass rebuild of 2010.1 packages

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-3mdv2010.1
+ Revision: 479286
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.3.1-2mdv2010.0
+ Revision: 440971
- rebuild

* Thu Mar 19 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-1mdv2009.1
+ Revision: 357906
- update to new version 1.3.1

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3-9mdv2009.1
+ Revision: 321960
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3-8mdv2009.0
+ Revision: 236827
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.3-7mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-7mdv2007.0
+ Revision: 81540
- Import php-pear-DB_ado

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdk
- initial Mandriva package (PLD import)

