Summary:	Serial connection daemon for Pocket PC devices
Name:		synce-vdccm
Version:	0.10.0
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	f6fcb49297cf80a028bfe75a8e1bdc4d
Patch0:		%{name}-dont-chown.patch
Patch1:		%{name}-uint16_t.patch
URL:		http://synce.sourceforge.net/
BuildRequires:	dbus-glib-devel
BuildRequires:	hal-devel
BuildRequires:	libstdc++-devel
BuildRequires:	synce-libsynce-devel = %{version}
Conflicts:	synce-kde < 0.9.1-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vdccm is a daemon running as the user on the desktop machine, which
the Pocket PC connects to. This vdccm is a replacement of the original
dccm and the vdccm comming with SynCE-KDE.

%prep
%setup -q -n vdccm-%{version}
%patch0 -p0
%patch1 -p1

%build
%configure \
	--with-libsynce=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
