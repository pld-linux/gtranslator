Summary:	gtranslator - a comfortable po file editor with many bells and whistles
Summary(pl.UTF-8):	gtranslator - wygodny edytor plików po z różnymi wodotryskami
Name:		gtranslator
Version:	1.9.8
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtranslator/1.9/%{name}-%{version}.tar.bz2
# Source0-md5:	8f8b967eda9f228c680375fd731d5c6f
Patch0:		%{name}-disable-desktop-update.patch
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
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	gtk-doc
BuildRequires:	gtksourceview2-devel
BuildRequires:	gtkspell-devel >= 2.0.2
BuildRequires:	intltool
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
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
%patch0 -p1

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

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gtranslator.schemas
%update_icon_cache hicolor
/usr/bin/scrollkeeper-update

%preun
%gconf_schema_uninstall gtranslator.schemas

%postun
%update_icon_cache hicolor
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEPENDS HACKING NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/gtranslator.schemas
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*.so
%attr(755,root,root) %{_libdir}/%{name}/plugins/gtr*.plugin
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dtd
%{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/ui
%{_datadir}/%{name}/po.lang
%{_datadir}/%{name}/*.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
