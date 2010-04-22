%define upstream_name    Games-Risk
%define upstream_version 3.101110

Name:       prisk
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Classical 'risk' board game
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Games/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Euclid)
BuildRequires: perl(Image::Imlib2)
BuildRequires: perl(Image::Size)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Loop::Tk)
BuildRequires: perl(Readonly)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tk)
BuildRequires: perl(Tk::Balloon)
BuildRequires: perl(Tk::Font)
BuildRequires: perl(Tk::JPEG)
BuildRequires: perl(Tk::PNG)
BuildRequires: perl(Tk::Pane)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(aliased)
BuildRequires: x11-server-xvfb

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Risk is a strategic turn-based board game. Players control armies, with
which they attempt to capture territories from other players. The goal of
the game is to control all the territories ('conquer the world') through
the elimination of the other players. Using area movement, Risk ignores
realistic limitations, such as the vast size of the world, and the
logistics of long campaigns.

This distribution implements a graphical interface for this game.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
xvfb-run ./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README META.yml Changes
%{_bindir}/prisk
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*

