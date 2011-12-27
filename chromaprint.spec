Name:           chromaprint
Version:        0.6
Release:        1%{?dist}
Summary:        Library implementing the AcoustID fingerprinting

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.acoustid.org/chromaprint/
Source:         https://github.com/downloads/lalinsky/chromaprint/%{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake
BuildRequires:  fftw-devel >= 3

%description
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

The library exposes a simple C API and the package also includes bindings for
the Python language. The documentation for the C API can be found in the main
header file.

%package -n libchromaprint
Summary:        Library implementing the AcoustID fingerprinting
Group:          Development/Libraries

%description -n libchromaprint
Chromaprint library is the core component of the AcoustID project. It's a 
client-side library that implements a custom algorithm for extracting 
fingerprints from raw audio sources.

The library exposes a simple C API and the package also includes bindings for
the Python language. The documentation for the C API can be found in the main
header file.

%package -n libchromaprint-devel
Summary:        Headers for developing programs that will use %{name} 
Group:          Development/Libraries

Requires:       libchromaprint%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n libchromaprint-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}. 

Requires:       libchromaprint%{?_isa} = %{version}-%{release}

%prep
%setup -q

# examples require ffmpeg, so turn off examples
%{cmake} -DBUILD_EXAMPLES=off -DBUILD_TESTS=off

%build
make %{?_smp_mflags}

%install
rm  -rf %{buildroot}

make install DESTDIR=%{buildroot}

rm  -f %{buildroot}%{_libdir}/lib*.la


%clean
rm  -rf %{buildroot}


%post -n libchromaprint -p /sbin/ldconfig

%postun -n libchromaprint -p /sbin/ldconfig

%files -n libchromaprint
%defattr(-,root,root,-)
%doc CHANGES.txt COPYING.txt NEWS.txt README.txt
%{_libdir}/lib*.so.*

%files -n libchromaprint-devel
%defattr(-,root,root,-)
%{_includedir}/chromaprint.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Dec 27 2011 Ismael Olea <ismael@olea.org> - 0.6-1
- update to 0.6
- python bindings removed
- python not a requirment now

* Wed Dec 07 2011 Ismael Olea <ismael@olea.org> - 0.5-4
- minor spec enhancements

* Mon Dec 05 2011 Ismael Olea <ismael@olea.org> - 0.5-3
- Macro cleaning at spec

* Thu Nov 18 2011 Ismael Olea <ismael@olea.org> - 0.5-2
- first version for Fedora

* Thu Nov 10 2011 Ismael Olea <ismael@olea.org> - 0.5-1
- update to 0.5
- subpackage for fpcalc 

* Sat Aug 06 2011 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.4-1
- Initial package
