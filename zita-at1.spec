Summary:	AT1 - autotuner for Jack Audio Connection Kit
Summary(pl.UTF-8):	AT1 - autostoiciel dla JACK-a
Name:		zita-at1
Version:	0.6.2
Release:	1
License:	GPL v3+
Group:		Applications/Sound
Source0:	https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	a27947a4c1bd48278aefc7f5b08a564f
URL:		https://kokkinizita.linuxaudio.org/linuxaudio/zita-at1-doc/quickguide.html
BuildRequires:	cairo-devel
BuildRequires:	clthreads-devel >= 2.4.0
BuildRequires:	clxclient-devel >= 3.9.0
BuildRequires:	fftw3-single-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXft-devel >= 2
BuildRequires:	zita-resampler-devel
Requires:	clthreads >= 2.4.0
Requires:	clxclient >= 3.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AT1 is an 'autotuner', normally used to correct the pitch of a voice
singing (slightly) out of tune. Compared to 'Autotalent' it provides
an improved pitch estimation algorithm, and much cleaner resampling.
AT1 does not include formant correction, so it should be used to
correct small errors only and not to really transpose a song. The
'expected' pitch can be controlled by Midi (via Jack only), or be a
fixed set of notes. AT1 can probably be used on some instruments as
well, but is primarily designed to cover the vocal range. It's also
usable as a quick and dirty guitar tuner.

The resampling algorithm in zita-at1 is designed to produce an
absolute minimum of artefacts and distortion.

%description -l pl.UTF-8
AT1 to "automatyczny stroiciel", zwykle używany do poprawiania stroju
głosu śpiewających (nieco) poza tonacją. W porównaniu z "autotalent"
zapewnia lepszy algorytm oceny stroju i dużo czystszy resampling. AT1
nie zawiera korekcji formantów, więc powinien być używany do poprawy
tylko małych błędów, a nie transpozycji utworu. "Oczekiwany" strój
może być sterowany przez MIDI (tylko przez Jack) albo być ustalonym
zbiorem nut. AT1 może być prawdopodobnie używany także dla niektórych
instrumentów, ale został zaprojektowany z myślą o pokryciu zakresu
wokalu. Jest przydatny także do szybkiego strojenia gitary.

%prep
%setup -q

%build
%{__make} -C source \
	CXXFLAGS="%{rpmcxxflags} -ffast-math -pthread $(pkg-config --cflags xft)" \
	LDFLAGS="%{rpmldflags}" \
	SHARED="%{_datadir}/zita-at1"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir} \
	SHARED="%{_datadir}/zita-at1"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS doc/*
%attr(755,root,root) %{_bindir}/zita-at1
%{_datadir}/zita-at1
