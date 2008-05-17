# TODO:
# - update pl,init script
Summary:	Serial connection daemon for Pocket PC devices
Summary(pl.UTF-8):	Demon połączenia szeregowego dla urządzeń Pocket PC
Name:		synce-vdccm
Version:	0.10.1
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/vdccm-%{version}.tar.gz
# Source0-md5:	43bca4c2fdb658f99b07549fa03832e0
Patch0:		%{name}-dont-chown.patch
Patch1:		%{name}-uint16_t.patch
URL:		http://synce.sourceforge.net/
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	glib2-devel >= 1:2.4
BuildRequires:	hal-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	synce-libsynce-devel >= %{version}
Conflicts:	synce-kde < 0.9.1-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vdccm is a daemon running as the user on the desktop machine, which
the Pocket PC connects to. This vdccm is a replacement of the original
dccm and the vdccm comming with SynCE-KDE.

%prep
%setup -q -n vdccm-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-libsynce=%{_prefix} \
	--enable-desktop-integration

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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
