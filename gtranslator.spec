# $Revision: 1.3 $
Summary:	gtranslator is a comfortable po file editor with many bells and whistles
Summary(pl):	gtranslator jest wygodnym edytorem plików po z ró¿nymi wodotryskami
Name: 		gtranslator
Version: 	0.43
Release: 	1
License: 	GPL
Vendor: 	GNOME Project
Group: 		Development/Tools
Source:		http://www.gtranslator.org/download/releases/%{version}/%{name}-%{version}.tar.gz
URL: 		http://www.gtranslator.org/
BuildRequires:	GConf-devel >= 1.0
BuildRequires:	ORBit-devel >= 0.5.3
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-utils
BuildRequires:	gal-devel >= 0.10.99
BuildRequires:  glib-devel >= 1.2.8
BuildRequires:	gnome-doc-tools
BuildRequires:	gnome-libs-devel >= 1.2.8
BuildRequires:	gnome-print-devel
BuildRequires:	gnome-vfs-devel >= 0.4.1
BuildRequires:  gtk+-devel >= 1.2.8
BuildRequires:	imlib-devel
BuildRequires:	intltool
BuildRequires:	libxml-devel => 1.8.9
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define 	_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
gtranslator is a comfortable po file editor with many bells and
whistles. It features many useful function which ease the work of
translators of po files immenantly.

%description -l pl
gtranslator jest wygodnym edytorem plików po z wielma wodotryskami. 
Dostarcza du¿o u¿ytecznych funkcji u³atwiaj±cych pracê przy
t³umaczeniach plików po.

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
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Developmentdir=%{__applnkdir}/Development \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEPENDS INSTALL NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/gtranslator
%dir %{_libdir}/gtranslator/backends
%{_libdir}/gtranslator/backends/*.xml
%attr(755,root,root) %{_libdir}/gtranslator/backends/docbook
%attr(755,root,root) %{_libdir}/gtranslator/backends/text
%dir %{_datadir}/gtranslator
%{_datadir}/gtranslator/colorschemes
%dir %{_datadir}/gtranslator/etspecs
%{_datadir}/gtranslator/etspecs/*etspec
%attr(755,root,root) %{_datadir}/gtranslator/scripts
%{_omf_dest_dir}/%{name}
%{_datadir}/mime-info/gtranslator.*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/gtranslator
%{_datadir}/gnome/help/gtranslator
%{_datadir}/gnome/apps/Development/gtranslator*
%{_mandir}/man1/gtranslator*
%{_mandir}/man1/pozilla*
