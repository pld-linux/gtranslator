# TODO: gtranslator-2.91.6-1.x86_64 zaznaczył gettext-devel-0.18.2.1-2.x86_64 (wł. libgettextpo.so.0()(64bit))

Summary:	gtranslator - a comfortable po file editor with many bells and whistles
Summary(pl.UTF-8):	gtranslator - wygodny edytor plików po z różnymi wodotryskami
Name:		gtranslator
Version:	2.91.6
Release:	0.1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtranslator/2.91/%{name}-%{version}.tar.xz
# Source0-md5:	4a86eacdbc4bb0bc09191b8a110f6d39
URL:		http://gtranslator.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel >= 4.3
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gdl-devel >= 2.26.0
BuildRequires:	gettext-devel
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtranslator is a comfortable po file editor with many bells and
whistles. It features many useful function which ease the work of
translators of po files immenantly.

%description -l pl.UTF-8
gtranslator jest wygodnym edytorem plików po z wieloma wodotryskami.
Dostarcza dużo użytecznych funkcji ułatwiających pracę przy
tłumaczeniach plików po.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.{a,la}
# we don't need headers
rm $RPM_BUILD_ROOT%{_includedir}/gtranslator-3.0/gtranslator/*.h
# we don't need docs too
rm -fr $RPM_BUILD_ROOT%{_datadir}/gtk-doc/


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
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dtd
%{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/ui
%{_datadir}/glib-2.0/schemas/*.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
