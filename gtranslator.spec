Summary:	gtranslator - a comfortable po file editor with many bells and whistles
Summary(pl):	gtranslator - wygodny edytor plik�w po z r�nymi wodotryskami
Name:		gtranslator
Version:	1.1.4
Release:	1
Epoch:		1
License:	GPL
Vendor:		GNOME Project
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/gtranslator/%{name}-%{version}.tar.gz
# Source0-md5:	188a73d5e2cb9dce67b3168acdf0ff27
Patch0:		%{name}-configure_in.patch
Patch1:		%{name}-pl_po.patch
URL:		http://gtranslator.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-vfs2-devel
BuildRequires:	intltool
BuildRequires:	libbonoboui-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libxml2-devel >= 2.4.12
BuildRequires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtranslator is a comfortable po file editor with many bells and
whistles. It features many useful function which ease the work of
translators of po files immenantly.

%description -l pl
gtranslator jest wygodnym edytorem plik�w po z wieloma wodotryskami.
Dostarcza du�o u�ytecznych funkcji u�atwiaj�cych prac� przy
t�umaczeniach plik�w po.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
