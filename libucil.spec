%define lib_major	2
%define lib_name	%mklibname ucil %{lib_major}
%define develname	%mklibname -d ucil

Summary: Library to render text and graphic overlays onto video images
Name: libucil
Version: 0.9.10
Release: %mkrel 1
Source0: http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0: libucil-0.9.8-bz627890.patch
Patch1: libucil-0.9.10-leaks.patch
Patch2: libucil-0.9.10-warnings.patch
License: GPLv2+
Group: System/Libraries
Url: http://www.unicap-imaging.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: intltool
BuildRequires: gtk-doc
BuildRequires: libunicap-devel
BuildRequires: glib2-devel
BuildRequires: pango-devel
BuildRequires: alsa-lib-devel
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
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.%{lib_major}*

%files -n %{develname}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/libucil
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
