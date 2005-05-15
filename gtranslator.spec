Summary:	gtranslator - a comfortable po file editor with many bells and whistles
Summary(pl):	gtranslator - wygodny edytor plików po z ró¿nymi wodotryskami
Name:		gtranslator
Version:	1.1.6
Release:	2
Epoch:		1
License:	GPL
Vendor:		GNOME Project
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtranslator/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	e3aab4a220ab4a3a88e08dde9e1c461c
Patch0:		%{name}-configure_in.patch
Patch1:		%{name}-locale_names.patch
URL:		http://gtranslator.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	gtkspell-devel >= 2.0.2
BuildRequires:	intltool
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtranslator is a comfortable po file editor with many bells and
whistles. It features many useful function which ease the work of
translators of po files immenantly.

%description -l pl
gtranslator jest wygodnym edytorem plików po z wieloma wodotryskami.
Dostarcza du¿o u¿ytecznych funkcji u³atwiaj±cych pracê przy
t³umaczeniach plików po.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po
sed -i 's/Categories=.*/Categories=GTK;GNOME;Development;Translation;/' data/desktop/gtranslator.desktop.in

%build
glib-gettextize --copy --force
intltoolize
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationdir=%{_desktopdir}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEPENDS HACKING NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/colorschemes
%{_datadir}/%{name}/dtd
%attr(755,root,root) %{_datadir}/%{name}/scripts
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
