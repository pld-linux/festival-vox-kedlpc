Summary:	American English male voice 'ked'
Summary(pl.UTF-8):	Amerykańska odmiana języka angielskiego - głos męski 'ked'
Name:		festival-vox-kedlpc
Version:	0.1
Release:	3
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_kedlpc16k.tar.gz
# Source0-md5:	35d4a2f377d05913ddae61db542afca1
Requires:	festival-lex-CMU
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This voice provides an American English male voice using a residual
excited LPC diphone synthesis method. It uses the CMU Lexicon
pronunciations. Prosodic phrasing is provided by a statistically
trained model using part of speech and local distribution of breaks.
Intonation is provided by a CART tree predicting ToBI accents and an
F0 contour generated from a model trained from natural speech. The
duration model is also trained from data using a CART tree.

%description -l pl.UTF-8
Ten pakiet udostępnia głos męski dla amerykańskiej odmiany języka
angielskiego. Używa wzbudzanej szczątkowo dwugłoskowej metody syntezy
LPC. Używa leksykonu wymowy CMU. Frazy prozodyczne są zapewnione
przez statystycznie nauczony model przy użyciu części mowy i lokalnego
rozłożenia przerw. Intonację zapewnia drzewo CART przewidujące akcenty
ToBI i obrys F0 generowany z modelu nauczonego na podstawie naturalnej
mowy. Model czasów trwania jest nauczony na podstawie danych z drzewa
CART.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english

cd festival/lib/voices/english
cp -r ked_diphone $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english
rm $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/ked_diphone/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/voices/english/ked_diphone/COPYING
%{_datadir}/festival/lib/voices/english/ked_diphone
