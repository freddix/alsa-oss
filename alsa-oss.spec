Summary:	Advanced Linux Sound Architecture - OSS compatibility wrapper library & script
Name:		alsa-oss
Version:	1.0.28
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/oss-lib/%{name}-%{version}.tar.bz2
# Source0-md5:	91f57e8cee1ad4cc956caa8b62ac5d43
Patch0:		%{name}-path.patch
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the ALSA -> OSS compatibility library and simple
wrapper script which facilitates its use. This script just sets the
appropriate LD_PRELOAD path and then runs the command.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib{alsatoss,aoss}.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aoss
%attr(755,root,root) %ghost %{_libdir}/libalsatoss.so.0
%attr(755,root,root) %ghost %{_libdir}/libaoss.so.0
%attr(755,root,root) %{_libdir}/libalsatoss.so
%attr(755,root,root) %{_libdir}/libalsatoss.so.*.*.*
%attr(755,root,root) %{_libdir}/libaoss.so
%attr(755,root,root) %{_libdir}/libaoss.so.*.*.*
%{_mandir}/man1/aoss.1*

