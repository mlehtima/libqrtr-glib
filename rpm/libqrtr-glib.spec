Name:    libqrtr-glib
Version: 1.2.0
Release: 1
Summary: Support library to use and manage the QRTR (Qualcomm IPC Router) bus.
License: LGPLv2+
URL:     http://freedesktop.org/software/libqrtr-glib
Source:  %{name}-%{version}.tar.xz

BuildRequires: kernel-headers
BuildRequires: meson >= 0.53
BuildRequires: pkgconfig(glib-2.0) >= 2.56.0
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gudev-1.0) >= 147

%description
This package contains the libraries that make it easier to use and
manage the QRTR (Qualcomm IPC Router) bus.

%package devel
Summary: Header files for adding QRTR support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel

%description devel
This package contains the header and pkg-config files for development
applications using QRTR functionality from applications that use glib.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%meson -Dgtk_doc=false
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS AUTHORS README.md
%{_libdir}/libqrtr-glib.so.*
%{_libdir}/girepository-1.0/Qrtr-1.0.typelib

%files devel
%{_includedir}/libqrtr-glib/
%{_libdir}/libqrtr-glib.so
%{_libdir}/pkgconfig/qrtr-glib.pc
%{_datadir}/gir-1.0/Qrtr-1.0.gir
