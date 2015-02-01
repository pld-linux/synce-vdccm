# NOTE: deprecated in favour of generic dccm support in synce-core
# TODO:
# - remove in favor of synce-core?
# - update init script
#
# Conditional build:
%bcond_with	hal	# HAL support

Summary:	Serial connection daemon for Pocket PC devices
Summary(pl.UTF-8):	Demon połączenia szeregowego dla urządzeń Pocket PC
Name:		synce-vdccm
Version:	0.10.1
Release:	2
License:	MIT
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/synce/vdccm-%{version}.tar.gz
# Source0-md5:	43bca4c2fdb658f99b07549fa03832e0
Patch0:		%{name}-dont-chown.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-uint16_t.patch
Patch3:		gcc.patch
Patch4:		%{name}-gcc47.patch
Patch5:		%{name}-errors.patch
URL:		http://synce.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	synce-libsynce-devel >= %{version}
%if %{with hal}
BuildRequires:	dbus-devel >= 0.61
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	hal-devel
Requires:	dbus >= 0.61
Requires:	dbus-glib >= 0.61
Requires:	glib2 >= 1:2.4
%endif
Requires:	synce-libsynce >= %{version}
Conflicts:	synce-kde < 0.9.1-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vdccm is a daemon running as the user on the desktop machine, which
the Pocket PC connects to. This vdccm is a replacement of the original
dccm and the vdccm comming with SynCE-KDE.

%description -l pl.UTF-8
vdccm to demon działający jako użytkownik na maszynie użytkownika, z
którą połączony jest Pocket PC. Jest zamiennikiem oryginalnego dccm i
vdccm dołączanego do SynCE-KDE.

%prep
%setup -q -n vdccm-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_hal:--enable-desktop-integration}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/triggerconnection
%attr(755,root,root) %{_bindir}/vdccm
%{_mandir}/man1/triggerconnection.1*
%{_mandir}/man1/vdccm.1*
