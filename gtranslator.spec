#
# Conditional build:
%bcond_without	apidocs	# API documentation

Summary:	gtranslator - a comfortable po file editor with many bells and whistles
Summary(pl.UTF-8):	gtranslator - wygodny edytor plików po z różnymi wodotryskami
Name:		gtranslator
Version:	46.1
Release:	1
Epoch:		1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://download.gnome.org/sources/gtranslator/46/%{name}-%{version}.tar.xz
# Source0-md5:	87a2f179182e9ae95f43c10863876935
Patch0:		%{name}-gtk-doc.patch
URL:		https://wiki.gnome.org/Apps/Gtranslator
BuildRequires:	docbook-dtd412-xml
# libgettextpo
BuildRequires:	gettext-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.71.3
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gspell-devel >= 1.2.0
BuildRequires:	gtk4-devel >= 4.12.0
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.28}
BuildRequires:	gtksourceview5-devel >= 5.4.0
BuildRequires:	itstool
BuildRequires:	json-glib-devel >= 1.2.0
BuildRequires:	libadwaita-devel >= 1.5
BuildRequires:	libgda6-devel >= 6.0
BuildRequires:	libsoup3-devel >= 3.0
BuildRequires:	libspelling-devel
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.71.3
Requires:	gspell >= 1.2.0
Requires:	gtk4 >= 4.12.0
Requires:	gtksourceview5 >= 5.4.0
Requires:	hicolor-icon-theme
Requires:	json-glib >= 1.2.0
Requires:	libadwaita >= 1.5
Requires:	libxml2 >= 2.4.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtranslator is a comfortable po file editor with many bells and
whistles. It features many useful function which ease the work of
translators of po files immenantly.

%description -l pl.UTF-8
gtranslator jest wygodnym edytorem plików po z wieloma wodotryskami.
Dostarcza dużo użytecznych funkcji ułatwiających pracę przy
tłumaczeniach plików po.

%package devel
Summary:	Header file for gtranslator plugins development
Summary(pl.UTF-8):	Plik nagłówkowy do tworzenia wtyczek edytora gtranslator
Group:		Development/Tools
Requires:	glib2-devel >= 1:2.71.3
BuildArch:	noarch

%description devel
Header file for gtranslator plugins development.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia wtyczek edytora gtranslator.

%package apidocs
Summary:	API documentation for gtranslator
Summary(pl.UTF-8):	Dokumentacja API gtranslatora
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for gtranslator.

%description apidocs -l pl.UTF-8
Dokumentacja API gtranslatora.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	%{?with_apidocs:-Dgtk_doc=true}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc (as of 2.38)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md THANKS
%attr(755,root,root) %{_bindir}/gtranslator
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.Gtranslator.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gtranslator.plugins.translation-memory.gschema.xml
%{_datadir}/gtksourceview-5/language-specs/gtranslator.lang
%{_datadir}/metainfo/org.gnome.Gtranslator.appdata.xml
%{_desktopdir}/org.gnome.Gtranslator.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Gtranslator.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Gtranslator-symbolic.svg
%{_mandir}/man1/gtranslator.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gtr-marshal.h

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtranslator
%endif
