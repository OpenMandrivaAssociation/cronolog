Summary:	A flexible log file rotation program for Apache
Name:		cronolog
Version:	1.6.2
Release:	10
License: 	Apache License
Group:		System/Servers
URL: 		https://cronolog.org/
Source0:	http://cronolog.org/download/%{name}-%{version}.tar.bz2
# http://cronolog.org/patches/cronolog-jumbo-patch.txt
Patch0:		cronolog-jumbo-patch.txt
# http://cronolog.org/mailing-list/msg00266.html
Patch1:		cronolog-1.6.2-filemode.diff

%description
"cronolog" is a simple program that reads log messages from its input and
writes them to a set of output files, the names of which are constructed using
template and the current date and time. The template uses the same format
specifiers as the Unix date command (which are the same as the standard C
strftime library function).

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
export CFLAGS="%{optflags} -DFILE_MODE=0640 -DDIR_MODE=0711"
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -m0755 src/zip_send_rm.sh %{buildroot}%{_sbindir}/zip_send_rm

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(0755,root,root) %{_sbindir}/cronolog
%attr(0755,root,root) %{_sbindir}/cronosplit
%attr(0755,root,root) %{_sbindir}/zip_send_rm
%attr(0644,root,root) %{_mandir}/man1/*.1*
%{_infodir}/cronolog*


%changelog
* Sun Jun 03 2012 Andrey Bondrov <abondrov@mandriva.org> 1.6.2-9
+ Revision: 802133
- Drop some legacy junk

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-8mdv2011.0
+ Revision: 617440
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.6.2-7mdv2010.0
+ Revision: 425295
- rebuild

* Tue Jun 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-6mdv2009.0
+ Revision: 222106
- fix dir mode (thanks Andre Nathan)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-5mdv2008.0
+ Revision: 81838
- rebuild


* Sun Aug 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-4mdv2007.0
- use tighter attribs
- fix url
- added one more patch

* Mon Mar 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-3mdk
- added the official "jumbo" patch (P0)

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1.6.2-2mdk
- rebuild

* Mon Dec 06 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.6.2-1mdk
- inital mandrake package
- used parts of the provided spec file

