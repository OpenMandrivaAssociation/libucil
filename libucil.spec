%define major	2
%define libname	%mklibname ucil %{major}
%define devname	%mklibname -d ucil

Summary:	Library to render text and graphic overlays onto video images
Name:		libucil
Version:	0.9.10
Release:	6
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.unicap-imaging.org/
Source0:	http://www.unicap-imaging.org/downloads/%{name}-%{version}.tar.gz
Patch0:		libucil-0.9.8-bz627890.patch
Patch1:		libucil-0.9.10-leaks.patch
Patch2:		libucil-0.9.10-warnings.patch
BuildRequires:	intltool
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libunicap)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(theora)
BuildRequires:	pkgconfig(vorbis)

%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The related ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package -n %{libname}
Summary:	Dynamic libraries for libucil
Group:		System/Libraries

%description -n %{libname}
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The related ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package -n %{devname}
Summary:	Development libraries, include files for Ucil
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
The package includes header files and libraries necessary
for developing programs which use the ucil library. It contains the API
documentation of the library, too.

%prep
%setup -q
%apply_patches

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libucil.so.%{major}*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/libucil
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

