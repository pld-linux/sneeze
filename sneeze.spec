Summary:	Sneeze is a Snort false-positive generator written in Perl
Summary(pl.UTF-8):	Sneeze - generator pakietów testowych dla reguł Snorta napisany w Perlu
Name:		sneeze
Version:	1.0
Release:	1
License:	GPL v2
Vendor:		Don Bailey <baileydl@mitre.org> Brian Caswell <bmc@mitre.org>
Group:		Networking
Source0:	http://snort.sourceforge.net/%{name}-%{version}.tar
# Source0-md5:	6e35ac12ae681daf593a45600b958a72
URL:		http://snort.sourceforge.net/
BuildRequires:	perl-Net-RawIP
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sneeze is a Snort false-positive generator written in Perl. It will
read normal Snort rules files, parse them, and generate packets that
will hopefully trigger those same rules. Sneeze can be configured to
use specific network devices, source ports, spoofed IPs, as well as
loop a specified amount of times or forever. Sneeze provides a way to
safely test an IDS in a controlled manner and provides useful output
to track what you are sending as triggers.

%description -l pl.UTF-8
Sneeze jest generatorem fałszywych alarmów Snorta, napisanym w Perlu.
Odczytuje zwykłe pliki reguł Snorta, przetwarza je i generuje pakiety,
które prawdopodobnie uruchomią te reguły. Sneeze może zostać
skonfigurowany do używania określonych urządzeń sieciowych, portów
źródłowych, spoofowanych IP, jak również może działać w pętli podaną
liczbę razy, lub permanentnie. Sneeze pozwala bezpiecznie przetestować
system wykrywania intruzów (IDS) w kontrolowany sposób, a efekt jego
działania pozwala sprawdzić, co dokładnie jest wysyłane w celu
uaktywnienia alarmu.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install sneeze.pl $RPM_BUILD_ROOT%{_bindir}/sneeze.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
