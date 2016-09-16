Summary:	Free content package for LGeneral based on k.u.k General
Summary(pl.UTF-8):	Wolnodostępny pakiet danych dla gry LGeneral oparty na k.u.k General
Name:		lgeneral-data-kukgen
Version:	1.1
Release:	1
License:	CC-BY-SA v3.0
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/lgeneral/kukgen-data-%{version}.tar.gz
# Source0-md5:	5a9755bdb2ae0a94910c093c5feafd61
URL:		http://lgames.sourceforge.net/LGeneral
Requires:	lgeneral >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LGeneral is a turn-based strategy engine heavily inspired by Panzer
General. This package contains free content data for LGeneral based on
Steve McGuba's k.u.k General.

%description -l pl.UTF-8
LGeneral jest turową grą strategiczną zainspirowaną o Panzer General.
Ten pakiet zawiera wolnodostępne pliki z danymi dla gry LGeneral
oparte na k.u.k General autorstwa Steve'a McGuby.

%prep
%setup -q -n lgeneral-data-1.1-d4d831b06c39a4d20dd0a96d0a89e3d50f22e69a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/lgeneral

cp -pr campaigns gfx maps nations scenarios sounds units $RPM_BUILD_ROOT%{_datadir}/lgeneral

%{__rm} $RPM_BUILD_ROOT%{_datadir}/lgeneral/sounds/LICENSE.sounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS COPYING ChangeLog LICENSE README THANKS TODO docs/* sounds/LICENSE.sounds
%{_datadir}/lgeneral/campaigns/kukgen
%{_datadir}/lgeneral/gfx/flags/kukgen.bmp
%{_datadir}/lgeneral/gfx/terrain/kukgen
%{_datadir}/lgeneral/gfx/units/kukgen*.bmp
%{_datadir}/lgeneral/maps/kukgen
%{_datadir}/lgeneral/maps/kukgen.tdb
%{_datadir}/lgeneral/nations/kukgen.ndb
%{_datadir}/lgeneral/scenarios/kukgen
%{_datadir}/lgeneral/sounds/kukgen
%{_datadir}/lgeneral/units/kukgen.udb
