Summary:	SynCE: Communication application
Name:		synce-vdccm
Version:	0.10.0
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	f6fcb49297cf80a028bfe75a8e1bdc4d
Patch0:		%{name}-dont-chown.patch
URL:		http://synce.sourceforge.net/
BuildRequires:	hal-devel
BuildRequires:	synce-libsynce-devel = %{version}
Conflicts:	synce-kde < 0.9.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vdccm is part of the SynCE project

%prep
%setup -q -n vdccm-%{version}
%patch0 -p0

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
