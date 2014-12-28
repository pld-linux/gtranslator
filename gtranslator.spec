Summary:	gtranslator - a comfortable po file editor with many bells and whistles
Summary(pl.UTF-8):	gtranslator - wygodny edytor plików po z różnymi wodotryskami
Name:		gtranslator
Version:	2.91.6
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtranslator/2.91/%{name}-%{version}.tar.xz
# Source0-md5:	4a86eacdbc4bb0bc09191b8a110f6d39
Patch0:		%{name}-gtkspell3.patch
URL:		http://gtranslator.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel >= 4.3
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdl-devel >= 2.26.0
BuildRequires:	gettext-tools
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gtk+3-devel
BuildRequires:	gtk-doc
BuildRequires:	gtksourceview3-devel
BuildRequires:	gtkspell3-devel
BuildRequires:	intltool
BuildRequires:	json-glib-devel
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	libgda5-devel
BuildRequires:	libgdict-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libpeas-gtk-devel
BuildRequires:	libunique-devel >= 1.0
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Provides:	%{name} = %{version}-%{release}
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
Summary:	A GNOME po file editor with many bells and whistles
Summary(pl.UTF-8):	Pliki programistyczne edytora gtranslator
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for gtranslator libraries.

%description devel -l pl.UTF-8
Pliki programistyczne dla bibliotek granslatora.


%prep
%setup -q
%patch -p1

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-static \
	--with-dictionary \
	--with-gda=5.0 \
	--disable-gtk-doc-html \
	--with-gtkspell

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/charmap/*.py[co]
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
/usr/bin/scrollkeeper-update

%postun
%update_icon_cache hicolor
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README THANKS
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/gtranslator/libgtranslator-private.so
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/gtr*.plugin
%dir %{_libdir}/gtranslator/plugins/charmap
%{_libdir}/gtranslator/plugins/charmap/*.py
%dir %{_libdir}/%{name}/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/Gtranslator-3.0.typelib
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dtd
%{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/ui
%{_datadir}/glib-2.0/schemas/*.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_desktopdir}/*.desktop
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/gtranslator-3.0
%dir %{_includedir}/gtranslator-3.0/gtranslator
%{_includedir}/gtranslator-3.0/gtranslator/*.h
%{_pkgconfigdir}/gtranslator.pc
%{_libdir}/gtranslator/libgtranslator-private.la
%{_libdir}/gtranslator/plugins/*.la
%dir %{_datadir}/%{name}/gir-1.0
%{_datadir}/%{name}/gir-1.0/*
