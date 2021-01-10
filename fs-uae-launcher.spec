Summary:	FS-UAE Launcher - graphical configuration frontend and launcher for FS-UAE
Summary(pl.UTF-8):	FS-UAE Launcher - graficzny interfejs do konfiguracji i uruchamiania FS-UAE
Name:		fs-uae-launcher
Version:	3.0.5
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	https://fs-uae.net/stable/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6fc4e026763d49fb3f5696f678c4c0e4
URL:		https://fs-uae.net/
BuildRequires:	python3 >= 1:3.2
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	python3-PyOpenGL
Requires:	python3-PyQt5
Requires:	python3-lhafile
Requires:	python3-oyoyo
Requires:	python3-requests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FS-UAE Launcher is a graphical configuration program and launcher for
FS-UAE.

%description -l pl.UTF-8
FS-UAE Launcher to graficzny program do konfiguracji i uruchamiania
FS-UAE.

%prep
%setup -q

%build
%py3_build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install \
	--install-lib=%{_datadir}/fs-uae-launcher

%{__make} install-data \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/fs-uae-launcher

# unbundle
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/fs-uae-launcher/{OpenGL,oyoyo}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/fs-uae-launcher
%{_datadir}/fs-uae-launcher
%{_desktopdir}/fs-uae-launcher.desktop
%{_iconsdir}/hicolor/*x*/apps/fs-uae-launcher.png
