%define tag_version 0.9.2

Summary: Enhanced version of tapdisk
Name:    blktap
Version: 2.0.90
Release: 9%{?dist}
License: LGPL+linking exception
URL:  https://github.com/xapi-project/blktap
Source0: https://github.com/xapi-project/%{name}/archive/%{tag_version}/%{name}-%{tag_version}.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libaio-devel
BuildRequires: libtool
BuildRequires: libuuid-devel
BuildRequires: xen-devel
BuildRequires: openssl-devel

%description
Enhanced version of tapdisk with support for storage mirroring.

%package devel
Summary: BlkTap Development Headers and Libraries
Requires: blktap = %{version}
Group: Development/Libraries

%description devel
This package contains the blktap development libraries and header files.

%prep
%setup -q -n %{name}-%{tag_version}

%build
sh autogen.sh
%configure --disable-static
%{__make} USE_SYSTEM_LIBRARIES=y

%install
%{__make} install USE_SYSTEM_LIBRARIES=y \
                  DESTDIR=$RPM_BUILD_ROOT \
                  LIBDIR=%{_libdir} \
                  SBINDIR=%{_sbindir} \
                  SYSCONFDIR=%{_sysconfdir} \
                  -Wno-format
#removing .la file
rm -rf $RPM_BUILD_ROOT%{_libdir}/libblktapctl.la

%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/libvhd.so*
%{_libdir}/libvhdio.so*
%{_libdir}/libblktapctl.so*
%{_bindir}/vhd-*
%{_sbindir}/lvm-util
%{_sbindir}/part-util
%{_sbindir}/tap-ctl
%{_sbindir}/td-rated
%{_sbindir}/td-util
%{_sbindir}/vhdpartx
%{_libexecdir}/tapdisk
%{_sysconfdir}/udev/rules.d/blktap.rules
%{_sysconfdir}/cron.daily/blktap-log-cleanup
%{_sysconfdir}/logrotate.d/blktap

%files devel
%defattr(-,root,root,-)
%{_includedir}/blktap/*
%{_includedir}/vhd/*
%{_libdir}/libvhd*


%changelog
* Thu Jun 05 2014 Jason Kölker <jason@koelker.net> - 0.9.2-2
- Split devel into separate package
- Use epoch hammer to handle upgrade from fedora versioning

* Wed Jun 04 2014 Bob Ball <bob.ball@citrix.com> - 0.9.2-1
- Update blktap to latest release

* Wed Mar 12 2014 Bob Ball <bob.ball@citrix.com> - 0.9.1-1
- Update blktap to avoid Debian Jessie compile failure 

* Fri Jan 17 2014 Euan Harris <euan.harris@citrix.com> - 0.9.0-2
- Change to upstream source repository

* Thu Oct 24 2013 David Scott <dave.scott@eu.citrix.com> - 0.9.0-1
- Initial package
