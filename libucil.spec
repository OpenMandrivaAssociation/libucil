%define lib_major	2
%define lib_name	%mklibname ucil %{lib_major}
%define develname	%mklibname -d ucil

Summary: Library to render text and graphic overlays onto video images
Name: libucil
Version: 0.9.10
Release: 3
Source0: http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0: libucil-0.9.8-bz627890.patch
Patch1: libucil-0.9.10-leaks.patch
Patch2: libucil-0.9.10-warnings.patch
License: GPLv2+
Group: System/Libraries
Url: http://www.unicap-imaging.org/
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: libunicap-devel
BuildRequires: glib2-devel
BuildRequires: pango-devel
BuildRequires: pkgconfig(pangoft2)
BuildRequires: pkgconfig(alsa)
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libtheora-devel
BuildRequires: libogg-devel
BuildRequires: libvorbis-devel
BuildRequires: libpng-devel

%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The related ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package -n %{lib_name}
Summary:	Dynamic libraries for libucil
Group:		System/Libraries
Conflicts:	%{_lib}unicap2 < 0.9.12

%description -n %{lib_name}
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The related ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package -n %{develname}
Summary:	Development libraries, include files for Ucil
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Conflicts:	%{_lib}unicap-devel < 0.9.12

%description -n %{develname}
The package includes header files and libraries necessary
for developing programs which use the ucil library. It contains the API
documentation of the library, too.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_5x --disable-static --disable-rpath
%make

%install
rm -rf %{buildroot}

%makeinstall_std

#%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.%{lib_major}*

%files -n %{develname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/libucil
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so


%changelog
* Tue May 10 2011 Funda Wang <fwang@mandriva.org> 0.9.10-1mdv2011.0
+ Revision: 673177
- add conflicts to ease upgrade
- new version 0.9.10
- cp old package

* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 0.9.5-4
+ Revision: 672756
- br intltool
- disable v4l1

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-3mdv2011.0
+ Revision: 608105
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-2mdv2010.1
+ Revision: 524303
- rebuilt for 2010.1

* Wed Jun 17 2009 Frederik Himpe <fhimpe@mandriva.org> 0.9.5-1mdv2010.0
+ Revision: 386803
- Update to new version 0.9.5
- Remove string format patch: not needed anymore

* Sun Mar 15 2009 Funda Wang <fwang@mandriva.org> 0.9.3-1mdv2009.1
+ Revision: 355209
- New version 0.9.3

* Mon Dec 29 2008 Funda Wang <fwang@mandriva.org> 0.9.1-2mdv2009.1
+ Revision: 320826
- fix str fmt

* Tue Sep 02 2008 Frederic Crozat <fcrozat@mandriva.com> 0.9.1-1mdv2009.0
+ Revision: 278869
- Release 0.9.1
- Patch0: fix build with undefined ldflags
- Patch1: ensure plugins are build as unversioned modules (fix provides conflicting with libv4l)

* Thu Jul 03 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.2.23-6mdv2009.0
+ Revision: 231056
- Added 2 BuildRequires: libtheora-devel and libvorbis-devel

* Tue Jul 01 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.2.23-5mdv2009.0
+ Revision: 230503
- Added libalsa-devel as BuildRequires for ucil_alsa.h

* Fri Jun 27 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.2.23-4mdv2009.0
+ Revision: 229555
- Fixing some package errors

* Thu Jun 26 2008 Rodrigo Gonçalves de Oliveira <rodrigo@mandriva.com> 0.2.23-3mdv2009.0
+ Revision: 229284
- Updating the unicap lib to 2.23 version

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.13-2mdv2008.1
+ Revision: 171153
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Aug 04 2007 Funda Wang <fwang@mandriva.org> 0.2.13-1mdv2008.0
+ Revision: 58893
- BR gtk-doc
- Remove unused devel files
- New major
- Patch against Makefile.in rather than Makefile.am
- New verison 0.2.13
- Rediff patch0


* Tue Jan 23 2007 Frederic Crozat <fcrozat@mandriva.com> 0.2.1-1mdv2007.0
+ Revision: 112500
-Patch0: fix libdir for biarch
- Import unicap

