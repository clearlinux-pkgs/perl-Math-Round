#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Math-Round
Version  : 0.07
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/G/GR/GROMMEL/Math-Round-0.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GR/GROMMEL/Math-Round-0.07.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmath-round-perl/libmath-round-perl_0.07-1.debian.tar.xz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Math-Round-license
Requires: perl-Math-Round-man

%description
Math::Round -- Perl extension for rounding numbers
Math::Round is a Perl module.  It supplies functions to round numbers,
both positive and negative, in various ways.  This may seem like an
odd thing to write a whole module for, but rounding can sometimes be
a little tricky, so I thought some people might find this useful.

%package license
Summary: license components for the perl-Math-Round package.
Group: Default

%description license
license components for the perl-Math-Round package.


%package man
Summary: man components for the perl-Math-Round package.
Group: Default

%description man
man components for the perl-Math-Round package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Math-Round-0.07
mkdir -p %{_topdir}/BUILD/Math-Round-0.07/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Math-Round-0.07/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Math-Round
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-Math-Round/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Math/Round.pm
/usr/lib/perl5/site_perl/5.26.1/auto/Math/Round/autosplit.ix

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Math-Round/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Math::Round.3
