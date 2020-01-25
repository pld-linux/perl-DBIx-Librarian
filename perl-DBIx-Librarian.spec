#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	DBIx
%define		pnam	Librarian
Summary:	DBIx::Librarian - manage SQL in repository outside code
Summary(pl.UTF-8):	DBIx::Librarian - zarządzanie SQL w repozytorium poza kodem
Name:		perl-DBIx-Librarian
Version:	0.6
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8da6b1d5a28ec8bbbd32c89bff942a5d
URL:		http://search.cpan.org/dist/DBIx-Librarian/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Virtual
BuildRequires:	perl-DBI
BuildRequires:	perl-Data-Library
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is for data manipulation (SELECT, INSERT, UPDATE, DELETE), not
for data definition (CREATE, DROP, ALTER). Some DDL statements may
work inside this module, but correct behavior is not guaranteed.

%description -l pl.UTF-8
Ten moduł służy do operacji na danych (SELECT, INSERT, UPDATE,
DELETE), ale nie do definiowania danych (CREATE, DROP, ALTER).
Niektóre wyrażenia DDL mogą działać wewnątrz tego modułu, ale
prawidłowe zachowanie nie jest gwarantowane.

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
