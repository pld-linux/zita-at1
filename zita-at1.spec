Summary:	AT1 - autotuner for Jack Audio Connection Kit
Name:		zita-at1
Version:	0.6.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	a27947a4c1bd48278aefc7f5b08a564f
URL:		https://kokkinizita.linuxaudio.org/linuxaudio/zita-at1-doc/quickguide.html
BuildRequires:	cairo-devel
BuildRequires:	clthreads-devel
BuildRequires:	clxclient-devel
BuildRequires:	fftw3-single-devel
BuildRequires:	freetype-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig
BuildRequires:	zita-resampler-devel
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

%prep
%setup -q

%build
cd source
%{__make} \
	CXXFLAGS="%{rpmcxxflags} -ffast-math -pthread $(pkg-config --cflags freetype2)" \
	LDFLAGS="%{rpmldflags}" \
	SHARED="%{_datadir}/zita-at1"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

cd source
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir} \
	SHARED="%{_datadir}/zita-at1"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/zita-at1
%{_datadir}/zita-at1
