
%define		snap		20030112

Summary:	gtranslator is a comfortable po file editor with many bells and whistles
Summary(pl):	gtranslator jest wygodnym edytorem plików po z ró¿nymi wodotryskami
Name:		gtranslator
Version:	0.99
Release:	%{snap}
License:	GPL
Vendor:		GNOME Project
Group:		Development/Tools
Source0:	http://www.gtranslator.org/download/releases/%{version}/%{name}-%{version}-%{snap}.tar.bz2
URL:		http://www.gtranslator.org/
Patch0:		%{name}-configure_in.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel
BuildRequires:	libbonoboui-devel
BuildRequires:	intltool
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libxml2-devel >= 2.4.12
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
%patch -p1

%build
glib-gettextize --copy --force
intltoolize
%{__aclocal} -I /usr/share/aclocal/gnome2-macros
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
	Applicationdir=%{_datadir}/applications

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEPENDS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gtranslator
%{_datadir}/gtranslator/colorschemes
%dir %{_datadir}/gtranslator/etspecs
%{_datadir}/gtranslator/etspecs/*etspec
%attr(755,root,root) %{_datadir}/gtranslator/scripts
%{_datadir}/mime-info/gtranslator.*
%{_pixmapsdir}/*.png
%{_pixmapsdir}/gtranslator
%{_datadir}/applications/gtranslator*
%{_mandir}/man1/gtranslator*
%{_mandir}/man1/pozilla*
