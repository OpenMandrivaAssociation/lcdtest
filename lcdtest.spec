Summary:	Utility to display LCD monitor test patterns
Name:		lcdtest
Version:	1.18
Release:	2
License:	GPLv3+
Group:		System/Configuration/Hardware
Url:		http://www.brouhaha.com/~eric/software/lcdtest/
Source0:	http://www.brouhaha.com/~eric/software/%{name}/download/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		lcdtest-1.18-font-path.patch
BuildRequires:	scons >= 1.2.0
BuildRequires:	imagemagick
BuildRequires:	netpbm
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_ttf)
Requires:	fonts-ttf-liberation

%description
lcdtest is a utility to display LCD monitor test patterns. It may be
useful for adjusting the pixel clock frequency and phase on LCD
monitors when using analog inputs, and for finding pixels that are
stuck on or off.

%prep
%setup -q
%patch0 -p1

%build
scons CFLAGS="%{optflags}"

%install
scons CFLAGS="%{optflags}" \
	--buildroot %{buildroot} \
	--bindir %{_bindir} \
	--mandir %{_mandir} \
	--datadir %{_datadir} \
	install

# install menu icons
for N in 16 22 24 32 48 64 128 256;
do
convert %{SOURCE1} -resize ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*
