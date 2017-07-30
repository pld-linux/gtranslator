Summary:	gtranslator - a comfortable po file editor with many bells and whistles
Summary(pl.UTF-8):	gtranslator - wygodny edytor plików po z różnymi wodotryskami
Name:		gtranslator
Version:	2.91.7
Release:	1
Epoch:		1
License:	GPL v3+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtranslator/2.91/%{name}-%{version}.tar.xz
# Source0-md5:	1607fc1fe0c4990ac348783baba32753
Patch0:		%{name}-pc.patch
URL:		http://gtranslator.sourceforge.net/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	db-devel >= 4.3
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdl-devel >= 3.6.0
# libgettextpo
BuildRequires:	gettext-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gobject-introspection-devel >= 0.9.3
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel >= 3.4.2
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gtksourceview3-devel >= 3.0.0
BuildRequires:	gtkspell3-devel >= 3.0.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	iso-codes >= 0.35
BuildRequires:	json-glib-devel >= 0.12.0
BuildRequires:	libgda5-devel >= 5.0
BuildRequires:	libgdict-devel >= 0.11.0
BuildRequires:	libpeas-gtk-devel >= 1.2.0
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	pkgconfig
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	gdl >= 3.6.0
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.4.2
Requires:	hicolor-icon-theme
Requires:	iso-codes >= 0.35
Requires:	json-glib >= 0.12.0
Requires:	libgdict >= 0.11.0
Requires:	libpeas-gtk >= 1.2.0
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
Summary:	Header files for gtranslator plugins development
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia wtyczek edytora gtranslator
Group:		Development/Tools
# libgettextpo
Requires:	gettext-devel
Requires:	glib2-devel >= 1:2.32.0
Requires:	gtk+3-devel >= 3.4.2
Requires:	gtksourceview3-devel >= 3.0.0

Requires:	gtksourceview2-devel >= 2.0
Requires:	libglade-devel >= 2.0

%description devel
Header files for gtranslator plugins development.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek edytora gtranslator.

%package apidocs
Summary:	API documentation for gtranslator
Summary(pl.UTF-8):	Dokumentacja API gtranslatora
Group:		Documentation

%description apidocs
API documentation for gtranslator.

%description apidocs -l pl.UTF-8
Dokumentacja API gtranslatora.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static \
	--with-dictionary \
	--with-gda=5.0 \
	--disable-gtk-doc-html \
	--with-gtkspell \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtranslator/*.la \
	$RPM_BUILD_ROOT%{_libdir}/gtranslator/plugins/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/charmap/*.py[co]

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/gtranslator
%dir %{_libdir}/%{name}
%{_libdir}/gtranslator/libgtranslator-private.so
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*.so
%{_libdir}/%{name}/plugins/gtr-*.plugin
%dir %{_libdir}/gtranslator/plugins/charmap
%{_libdir}/gtranslator/plugins/charmap/*.py
%dir %{_libdir}/%{name}/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/Gtranslator-3.0.typelib
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dtd
%{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/ui
%{_datadir}/appdata/gtranslator.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gtranslator*.gschema.xml
%{_iconsdir}/hicolor/*x*/apps/gtranslator.png
%{_iconsdir}/hicolor/scalable/apps/gtranslator.svg
%{_desktopdir}/gtranslator.desktop
%{_mandir}/man1/gtranslator.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gtranslator-3.0
# dir shared with base
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/gir-1.0
%{_datadir}/%{name}/gir-1.0/Gtranslator-3.0.gir
%{_pkgconfigdir}/gtranslator.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gtranslator
