# $Revision: 1.1 $
Summary:	gtranslator is a comfortable po file editor with many bells and whistles.
Summary(pl):	gtranslator jest wygodnym edytorem plików po z ró¿nymi wodotryskami.
Name: 		gtranslator
Version: 	0.43
Release: 	1
License: 	GPL
Vendor: 	GNOME Project
Group: 		Development/Tools
Source:		http://www.gtranslator.org/download/releases/%{version}/%{name}-%{version}.tar.gz
URL: 		http://www.gtranslator.org
BuildRequires:	gal-devel >= 0.10.99
BuildRequires:	gnome-vfs-devel >= 0.4.1
BuildRequires:	imlib-devel
BuildRequires:	GConf-devel >= 1.0
BuildRequires:  glib-devel >= 1.2.8
BuildRequires:  gtk+-devel >= 1.2.8
BuildRequires:	gnome-libs-devel >= 1.2.8
BuildRequires:	ORBit-devel >= 0.5.3
BuildRequires:	libxml-devel => 1.8.9
BuildRequires:	gnome-doc-tools
BuildRequires:	docbook-utils
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	scrollkeeper
Prereq:		scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
gtranslator is a comfortable po file editor with many bells and whistles.
It features many useful function which ease the work of translators of po
files immenantly.

%description -l pl
gtranslator jest wygodnym edytorem plików po z wielma wodotryskami. 
Dostarcza du¿o u¿ytecznych funkcji u³atwiaj±cych pracê przy t³umazeniach
plików po.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
xml-i18n-toolize --copy --force
aclocal -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}
%{__make} check

%install

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Developmentdir=%{__applnkdir}/Development \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%post
scrollkeeper-update

%postun
scrollkeeper-update

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(0555, bin, bin)
%doc AUTHORS COPYING ChangeLog DEPENDS INSTALL NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/gtranslator/scripts/*

%defattr(0444, bin, bin, 0555)
%{_datadir}/gtranslator/colorschemes
%{_omf_dest_dir}/%{name}/*

%defattr(0444,root,root, 0555)
%{_mandir}/man1/gtranslator*
%{_mandir}/man1/pozilla*
%{_datadir}/gnome/help/gtranslator

%defattr(0755, bin, bin)
%{_libdir}/gtranslator/backends/*/*.la
%{_libdir}/gtranslator/backends/*/*.so

%defattr(-, root, root)
%{_libdir}/gtranslator/backends/*.xml
%{_datadir}/gtranslator/etspecs/*etspec
%{_datadir}/gnome/apps/Development/gtranslator*
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/gtranslator
%{_datadir}/mime-info/gtranslator.*
%{_datadir}/locale/*/LC_MESSAGES/gtranslator.mo
