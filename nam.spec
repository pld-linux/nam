Summary:	Network Animator
Summary(pl.UTF-8):   Network Animator - sieciowe narzędzie animujące
Name:		nam
Version:	1.10
Release:	3
License:	Public Domain (?)
Group:		Applications/Networking
Source0:	http://www.isi.edu/nsnam/dist/%{name}-src-%{version}.tar.gz
# Source0-md5:	35efe4a43f1cc3dd03fb744c5603fc58
Source1:	http://www.isi.edu/nsnam/nam/nam-editor.ps
# Source1-md5:	30247511d4836c98eecad2d34baa285b
URL:		http://www.isi.edu/nsnam/
Patch0:		%{name}-install.patch
Patch1:		tcl-lib.patch
Patch2:		%{name}-link.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	otcl-devel
BuildRequires:	perl-base
BuildRequires:	tclcl-devel
BuildRequires:	tcl-devel >= 8.4
BuildRequires:	tk-devel >= 8.4
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nam is a Tcl/TK based animation tool for viewing network simulation
traces and real world packet traces. It supports topology layout,
packet level animation, and various data inspection tools.

%description -l pl.UTF-8
Nam jest opartym na Tcl/TK narzędziem animującym do oglądania
tras symulowanych oraz rzeczywistych pakietów. Wspiera przedstawianie
topologii, animowanie na poziomie pakietów i różne narzędzia obróbki
danych.

%package bin
Summary:	Various scripts from nam
Summary(pl.UTF-8):   Różne skrypty do nam
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description bin
Various scripts from nam.

%description bin -l pl.UTF-8
Różne skrypty do nam.

%package edu
Summary:	ns-scripts for Directed Research
Summary(pl.UTF-8):   Skrypty ns z rzeczywistych badań
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description edu
This package contains tcl files which are ns-scripts for Directed
Research with Dr. Heidemann. You could see the explanation about
those files at
http://www-scf.usc.edu/~hyunahpa/D-Research/DR-home.html

%description edu -l pl.UTF-8
Pakiet ten zawiera pliki tcl będące skryptami ns z badań Dr.
Heidemann. Wyjaśnienia do tych plików możesz znaleźć pod
http://www-scf.usc.edu/~hyunahpa/D-Research/DR-home.html

%package ex
Summary:	Examples
Summary(pl.UTF-8):   Przykłady
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description ex
Examples which have been collected from ns runs.

%description ex -l pl.UTF-8
Przykłady zebrane podczas pracy ns.

%package iecdemos
Summary:	Demos
Summary(pl.UTF-8):   Dema
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description iecdemos
Demos.

%description iecdemos -l pl.UTF-8
Dema.

%package tcl
Summary:	Tcl scripts
Summary(pl.UTF-8):   Skrypty Tcl
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description tcl
Some Tcl scripts from nam.

%description tcl -l pl.UTF-8
Skrypty Tcl z nam.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	--with-tcl-ver=8.4 \
	--with-tk-ver=8.4 \
	--with-zlib=%{_libdir}
%{__make} \
	CCOPT="%{rpmcflags}"

%{__perl} -pe 's|/usr/local/bin/tclsh7.6|/usr/bin/tclsh|' -i fix-script.tcl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/nam}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -r bin $RPM_BUILD_ROOT%{_datadir}/nam
cp -r edu $RPM_BUILD_ROOT%{_datadir}/nam
cp -r ex $RPM_BUILD_ROOT%{_datadir}/nam
cp -r iecdemos $RPM_BUILD_ROOT%{_datadir}/nam
cp -r tcl $RPM_BUILD_ROOT%{_datadir}/nam
gzip -9n $RPM_BUILD_ROOT%{_datadir}/nam/edu/*[!l]
gunzip $RPM_BUILD_ROOT%{_datadir}/nam/ex/*.gz
gzip -9n $RPM_BUILD_ROOT%{_datadir}/nam/ex/*

install *.t{cl,k} $RPM_BUILD_ROOT%{_datadir}/nam/bin

install nam.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.html TODO.html README nam-editor.ps
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/nam
%{_mandir}/man1/*

%files bin
%defattr(644,root,root,755)
%{_datadir}/nam/bin

%files edu
%defattr(644,root,root,755)
%{_datadir}/nam/edu

%files ex
%defattr(644,root,root,755)
%{_datadir}/nam/ex

%files iecdemos
%defattr(644,root,root,755)
%{_datadir}/nam/iecdemos

%files tcl
%defattr(644,root,root,755)
%{_datadir}/nam/tcl
