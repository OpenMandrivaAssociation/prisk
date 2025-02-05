%define upstream_name    Games-Risk
%define upstream_version 3.103040

Name:       prisk
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:    Classical 'risk' board game
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Games/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Getopt::Euclid)
BuildRequires: perl(Image::Magick)
BuildRequires: perl(Image::Size)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Locale::TextDomain)
BuildRequires: perl(MIME::Base64)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(MooseX::POE)
BuildRequires: perl(MooseX::SemiAffordanceAccessor)
BuildRequires: perl(Path::Class)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Loop::Tk)
BuildRequires: perl(Readonly)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tk)
BuildRequires: perl(Tk::Balloon)
BuildRequires: perl(Tk::Font)
BuildRequires: perl(Tk::JPEG)
BuildRequires: perl(Tk::PNG)
BuildRequires: perl(Tk::Pane)
BuildRequires: perl(Tk::Pod::Text)
BuildRequires: perl(Tk::Role::Dialog)
BuildRequires: perl(Tk::Sugar)
BuildRequires: perl(Tk::TableMatrix)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(aliased)
BuildRequires: perl(Module::Build)

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
# xvfb-run is broken currently, even if all the tests pass :-(
#xvfb-run ./Build test

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


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 3.103.40-2mdv2011.0
+ Revision: 657325
- add br
- rebuild for updated spec-helper

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.103.40-1mdv2011.0
+ Revision: 596609
- update to 3.103040

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - rebuild to fix perl path in binary

* Sat Jul 17 2010 Jérôme Quelin <jquelin@mandriva.org> 3.101.590-1mdv2011.0
+ Revision: 554687
- skip tests, since xvfb-run is broken
- adding missing buildrequires:
- update to 3.101590

* Thu Apr 22 2010 Jérôme Quelin <jquelin@mandriva.org> 3.101.110-1mdv2010.1
+ Revision: 537897
- run tests in a xvfb (require a display)
- adding missing buildrequires:
- import prisk


* Wed Apr 21 2010 cpan2dist 3.101110-1mdv
- initial mdv release, generated with cpan2dist
