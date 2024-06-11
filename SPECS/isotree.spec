Name:           isotree
Version:        0.6.1
Release:        1%{?dist}
Summary:        Isolation Forest and variations such as SCiForest and EIF

License:        BSD-2
URL:            https://github.com/netxms/isotree
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Fast and multi-threaded implementation of Isolation Forest (a.k.a. iForest)
and variations of it such as Extended Isolation Forest (EIF), Split-Criterion
iForest (SCiForest), Fair-Cut Forest (FCF), Robust Random-Cut Forest (RRCF),
and other customizable variants, aimed at outlier/anomaly detection plus
additions for imputation of missing values, distance/similarity calculation
between observations, and handling of categorical data. Written in C++.

%package devel
Summary: Development files for isotree
Requires: %{name} = %{version}-%{release}

%description devel
isotree development files.

%prep
%setup -q

%build
%cmake --no-warn-unused-cli -DNO_TEMPLATED_VERSIONS=1 .
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libisotree.so.0.6.1
%{_libdir}/libisotree.so.0
%{_libdir}/libisotree.so

%files devel
%{_libdir}/libisotree.so
%{_includedir}/isotree.hpp
%{_includedir}/isotree_c.h
%{_includedir}/isotree_oop.hpp
%{_datadir}/pkgconfig/isotree.pc

%changelog
* Tue Jun 11 2024 Alex Kirhenshtein <alk@netxms.org> - 0.6.1-1
- Initial package
