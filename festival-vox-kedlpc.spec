Summary:	American English male voice 'ked'
Summary(pl):	Ameryka�ska odmiana j�zyka angielskiego - g�os m�ski 'ked'
Name:		festival-vox-kedlpc
Version:	0.1
Release:	2
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_kedlpc16k.tar.gz
Requires:	festival-lex-CMU
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This voice provides an American English male voice using a residual
excited LPC diphone synthesis method. It uses the CMU Lexicon
pronunciations. Prosodic phrasing is provided by a statistically
trained model using part of speech and local distribution of breaks.
Intonation is provided by a CART tree predicting ToBI accents and an
F0 contour generated from a model trained from natural speech. The
duration model is also trained from data using a CART tree.

%description -l pl
Ten pakiet udost�pnia g�os m�ski dla ameryka�skiej odmiany j�zyka
angielskiego. U�ywa wzbudzanej szcz�tkowo dwyg�oskowej metody syntezy
LPC. U�ywa leksykonu wymowy CMU. Frazy prozodyczne s� zapewnione
przez statystycznie nauczony model przy u�yciu cz�ci mowy i lokalnego
roz�o�enia przerw. Intonacj� zapewnia drzewo CART przewiduj�ce akcenty
ToBI i obrys F0 generowany z modelu nauczonego na podstawie naturalnej
mowy. Model czas�w trwania jest nauczony na podstawie danych z drzewa
CART.

%prep
%setup -q -c %{name}-%{version}

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
