#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Librarian
Summary:	DBIx::Librarian - manage SQL in repository outside code
Summary(pl):	DBIx::Librarian - zarz±dzanie SQL w repozytorium poza kodem
Name:		perl-DBIx-Librarian
Version:	0.4
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	08b2d0e010853a54a595e32c46db70b2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DBI
BuildRequires:	perl-Data-Library
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is for data manipulation (SELECT, INSERT, UPDATE, DELETE), not
for data definition (CREATE, DROP, ALTER).  Some DDL statements may
work inside this module, but correct behavior is not guaranteed.

%description -l pl
Ten modu³ s³u¿y do operacji na danych (SELECT, INSERT, UPDATE,
DELETE), ale nie do definiowania danych (CREATE, DROP, ALTER). Niektóre
wyra¿enia DDL mog± dzia³aæ wewn±trz tego modu³u, ale prawid³owe
zachowanie nie jest gwarantowane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
