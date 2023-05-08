#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Round
Version  : 0.07
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/G/GR/GROMMEL/Math-Round-0.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GR/GROMMEL/Math-Round-0.07.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-round-perl/libmath-round-perl_0.07-1.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Math-Round-license = %{version}-%{release}
Requires: perl-Math-Round-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Math::Round -- Perl extension for rounding numbers
Math::Round is a Perl module.  It supplies functions to round numbers,
both positive and negative, in various ways.  This may seem like an
odd thing to write a whole module for, but rounding can sometimes be
a little tricky, so I thought some people might find this useful.

%package dev
Summary: dev components for the perl-Math-Round package.
Group: Development
Provides: perl-Math-Round-devel = %{version}-%{release}
Requires: perl-Math-Round = %{version}-%{release}

%description dev
dev components for the perl-Math-Round package.


%package license
Summary: license components for the perl-Math-Round package.
Group: Default

%description license
license components for the perl-Math-Round package.


%package perl
Summary: perl components for the perl-Math-Round package.
Group: Default
Requires: perl-Math-Round = %{version}-%{release}

%description perl
perl components for the perl-Math-Round package.


%prep
%setup -q -n Math-Round-0.07
cd %{_builddir}
tar xf %{_sourcedir}/libmath-round-perl_0.07-1.debian.tar.xz
cd %{_builddir}/Math-Round-0.07
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Math-Round-0.07/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Math-Round
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Math-Round/bbfe6df01982604309865e2564e565f5f47fff0a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Round.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Math-Round/bbfe6df01982604309865e2564e565f5f47fff0a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
