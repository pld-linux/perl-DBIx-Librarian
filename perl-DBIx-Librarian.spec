%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Librarian
Summary:	DBIx::Librarian - Manage SQL in repository outside code
Summary(pl):	DBIx::Librarian - zarz�dzanie SQL w repozytorium poza kodem
Name:		perl-DBIx-Librarian
Version:	0.3
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is for data manipulation (SELECT, INSERT, UPDATE, DELETE), not
for data definition (CREATE, DROP, ALTER).  Some DDL statements may
work inside this module, but correct behavior is not guaranteed.

%description -l pl
Ten modu� s�u�y do operacji na danych (SELECT, INSERT, UPDATE,
DELETE), ale nie do definiowania danych (CREATE, DROP, ALTER). Niekt�re
wyra�enia DDL mog� dzia�a� wewn�trz tego modu�u, ale prawid�owe
zachowanie nie jest gwarantowane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
