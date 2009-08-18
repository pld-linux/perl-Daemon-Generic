#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Daemon
%define	pnam	Generic
Summary:	Daemon::Generic - framework to provide start/stop/reload for a daemon
#Summary(pl.UTF-8):	Daemon::Generic -
Name:		perl-Daemon-Generic
Version:	0.61
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Daemon/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	10f8581f21c84fc0b169a93ad8c0dd60
URL:		http://search.cpan.org/dist/Daemon-Generic/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Daemon::Generic provides a framework for starting, stopping,
reconfiguring daemon-like programs.  The framework provides
for standard commands that work for as init.d files and 
as apachectl-like commands.

Programs that use Daemon::Generic subclass Daemon::Generic
to override its behavior.  Almost everything that 
Genric::Daemon does can be overridden as needed.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%{perl_vendorlib}/Daemon/*.pm
%{perl_vendorlib}/Daemon/Generic
%{_mandir}/man3/*
