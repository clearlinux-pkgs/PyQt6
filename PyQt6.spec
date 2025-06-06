#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v24
# autospec commit: a88ffdc
#
Name     : PyQt6
Version  : 6.9.0
Release  : 8
URL      : https://files.pythonhosted.org/packages/32/de/102e8e66149085acf38bbf01df572a2cd53259bcd99b7d8ecef0d6b36172/pyqt6-6.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/32/de/102e8e66149085acf38bbf01df572a2cd53259bcd99b7d8ecef0d6b36172/pyqt6-6.9.0.tar.gz
Summary  : Python bindings for the Qt cross platform application toolkit
Group    : Development/Tools
License  : GPL-3.0
Requires: PyQt6-bin = %{version}-%{release}
Requires: PyQt6-lib = %{version}-%{release}
Requires: PyQt6-license = %{version}-%{release}
Requires: PyQt6-python = %{version}-%{release}
Requires: PyQt6-python3 = %{version}-%{release}
BuildRequires : buildreq-kde
BuildRequires : dbus-python
BuildRequires : dbus-python-dev
BuildRequires : mesa-dev
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pypi(pyqt_builder)
BuildRequires : pypi(pyqtbuild)
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qscintilla
BuildRequires : qscintilla-dev
BuildRequires : qt6base-dev
BuildRequires : qt6charts-dev
BuildRequires : qt6connectivity-dev
BuildRequires : qt6declarative-dev
BuildRequires : qt6imageformats-dev
BuildRequires : qt6multimedia-dev
BuildRequires : qt6scxml-dev
BuildRequires : qt6sensors-dev
BuildRequires : qt6serialbus-dev
BuildRequires : qt6serialport-dev
BuildRequires : qt6svg-dev
BuildRequires : qt6tools-dev
BuildRequires : qt6translations
BuildRequires : qt6virtualkeyboard-dev
BuildRequires : qt6webchannel-dev
BuildRequires : qt6webengine-dev
BuildRequires : qt6websockets-dev
BuildRequires : sip
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# PyQt6 - Comprehensive Python Bindings for Qt v6
Qt is set of cross-platform C++ libraries that implement high-level APIs for
accessing many aspects of modern desktop and mobile systems.  These include
location and positioning services, multimedia, NFC and Bluetooth connectivity,
a Chromium based web browser, as well as traditional UI development.

%package bin
Summary: bin components for the PyQt6 package.
Group: Binaries
Requires: PyQt6-license = %{version}-%{release}

%description bin
bin components for the PyQt6 package.


%package lib
Summary: lib components for the PyQt6 package.
Group: Libraries
Requires: PyQt6-license = %{version}-%{release}

%description lib
lib components for the PyQt6 package.


%package license
Summary: license components for the PyQt6 package.
Group: Default

%description license
license components for the PyQt6 package.


%package python
Summary: python components for the PyQt6 package.
Group: Default
Requires: PyQt6-python3 = %{version}-%{release}
Provides: pyqt6-python

%description python
python components for the PyQt6 package.


%package python3
Summary: python3 components for the PyQt6 package.
Group: Default
Requires: python3-core
Requires: pypi-pyqt6_sip

%description python3
python3 components for the PyQt6 package.


%prep
%setup -q -n pyqt6-6.9.0
cd %{_builddir}/pyqt6-6.9.0

%build
## build_prepend content
export PATH="/usr/lib64/qt6/bin:$PATH"
sip-build --no-make --confirm-license
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744123370
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
## make_prepend content
cd build
## make_prepend end
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744123370
rm -rf %{buildroot}
## install_prepend content
cd build
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/PyQt6
cp %{_builddir}/pyqt6-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/PyQt6/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
find %{buildroot} -name '*.so' -print0 | xargs -rt0 chmod 755 --
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pylupdate6
/usr/bin/pyuic6

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/plugins/PyQt6/libpyqt6qmlplugin.so
/usr/lib64/qt6/plugins/designer/libpyqt6.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyQt6/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
