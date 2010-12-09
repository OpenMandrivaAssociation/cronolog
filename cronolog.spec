Summary:	A flexible log file rotation program for Apache
Name:		cronolog
Version:	1.6.2
Release:	%mkrel 8
License: 	Apache License
Group:		System/Servers
URL: 		http://cronolog.org/
Source0:	http://cronolog.org/download/%{name}-%{version}.tar.bz2
# http://cronolog.org/patches/cronolog-jumbo-patch.txt
Patch0:		cronolog-jumbo-patch.txt
# http://cronolog.org/mailing-list/msg00266.html
Patch1:		cronolog-1.6.2-filemode.diff
Requires(post): info-install
Requires(preun): info-install
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
"cronolog" is a simple program that reads log messages from its input and
writes them to a set of output files, the names of which are constructed using
template and the current date and time. The template uses the same format
specifiers as the Unix date command (which are the same as the standard C
strftime library function).

%prep

%setup -q -n %{name}-%{version}
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

%post
%_install_info %name

%preun
%_remove_install_info %name

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(0755,root,root) %{_sbindir}/cronolog
%attr(0755,root,root) %{_sbindir}/cronosplit
%attr(0755,root,root) %{_sbindir}/zip_send_rm
%attr(0644,root,root) %{_mandir}/man1/*.1*
%{_infodir}/cronolog*
