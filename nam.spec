Summary:	Network Animator
Summary(pl):	Network Animator
Name:		nam
Version:	1.9
Release:	1
License:	Public domain (?)
Group:		Applications/Networking
Source0:	http://www.isi.edu/nsnam/dist/%{name}-src-%{version}.tar.gz
# Source0-md5:	7505017f344ab5bf5eb9632bc6091dce
Source1:	http://www.isi.edu/nsnam/nam/nam-editor.ps
# Source1-md5:	30247511d4836c98eecad2d34baa285b
URL:		http://www.isi.edu/nsnam/
Patch0:		%{name}-install.patch
Patch1:		%{name}-gcc33.patch
BuildRequires:	autoconf
BuildRequires:	otcl-devel
BuildRequires:	tclcl-static
BuildRequires:	tcl-devel = 8.4.4
BuildRequires:	tk-devel = 8.4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nam is a Tcl/TK based animation tool for viewing network simulation
traces and real world packet traces. It supports topology layout,
packet level animation, and various data inspection tools.

%description -l pl
Nam jest opartym na Tcl/TK narzêdziem animuj±cym do ogl±dania
¶ladów symulacji oraz rzeczywistych pakietów. Wspiera topologie,
animowanie pakietów i ró¿ne narzêdzia obróbki danych.

%package bin
Summary:	Various scripts from nam
Summary(pl):	Ró¿ne skrypty do nam
Group:		Applications/Networking
Requires:	%{name} = %{version}

%description bin
Various scripts from nam.

%description bin -l pl
Ró¿ne skrypty do nam.

%package edu
Summary:	ns-scripts for Directed Research
Summary(pl):	Skrypty ns z rzeczywistych badañ
Group:		Applications/Networking
Requires:	%{name} = %{version}

%description edu
This package contains tcl files which are ns-scripts for Directed
Research with Dr. Heidemann. You could see the explanation about
those files at
http://www-scf.usc.edu/~hyunahpa/D-Research/DR-home.html

%description edu -l pl
Pakiet ten zawiera pliki tcl bêd±ce skryptami ns z badañ Dr.
Heidemann. Wyja¶nienia do tych plików mo¿esz znale¼æ pod
http://www-scf.usc.edu/~hyunahpa/D-Research/DR-home.html

%package ex
Summary:	Examples
Summary(pl):	Przyk³ady
Group:		Applications/Networking
Requires:	%{name} = %{version}

%description ex
Examples which have been collected from ns runs.

%description ex -l pl
Przyk³ady zebrane podczas pracy ns.

%package iecdemos
Summary:	Demos
Summary(pl):	Dema
Group:		Applications/Networking
Requires:	%{name} = %{version}

%description iecdemos
Demos.

%description iecdemos -l pl
Dema.

%package tcl
Summary:	Tcl scripts
Summary(pl):	Skrypty Tcl
Group:		Applications/Networking
Requires:	%{name} = %{version}

%description tcl
Some Tcl scripts from nam.

%description tcl -l pl
Skrypty Tcl z nam.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure \
	--with-tcl-ver=8.4.4 \
	--with-tk-ver=8.4.4
%{__make} \
	CCOPT="%{rpmcflags}"

perl -pe 's|/usr/local/bin/tclsh7.6|/usr/bin/tclsh|' -i fix-script.tcl

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
gzip $RPM_BUILD_ROOT%{_datadir}/nam/edu/*[^l]
gunzip $RPM_BUILD_ROOT%{_datadir}/nam/ex/*.gz
gzip $RPM_BUILD_ROOT%{_datadir}/nam/ex/*

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
