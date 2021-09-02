%global date 20210902
%global commit0 dffedb9ef1b7d2320908d61836c034c8484f34d9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:12})
%global the_owner dwrobel

Name:           mqtt-mysensors
Version:        2.3.1
Release:        1.%{date}git%{shortcommit0}%{?dist}
Summary:        MQTT service for mysensors serial gateway
License:        GPLv3+
Url:            https://github.com/%{the_owner}/%{name}
Source0:        https://github.com/%{the_owner}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{date}git%{shortcommit0}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

Requires:       systemd
Requires:       %{py3_dist paho-mqtt}
Requires:       %{py3_dist pyserial}

%description
Provides MySensors MQTT service using a mysensors serial gateway version >=2.3


%package udev
Summary:        mysensor udev rules

BuildRequires:  systemd-udev

Requires:       systemd-udev
Requires:       mqtt-mysensors = %{version}-%{release}


%description udev
Provides udev rules for attaching Arduino Nano


%prep
%autosetup -n %{name}-%{commit0}


%build
%py3_build


%install
%py3_install
install -D -p -m 0644 50-usb-arduino.rules %{buildroot}%{_udevrulesdir}/50-usb-arduino.rules


%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_unitdir}/%{name}.service


%files udev
%{_udevrulesdir}/50-usb-arduino.rules


%post
%systemd_post %{name}.service


%preun
%systemd_preun %{name}.service


%postun
%systemd_postun_with_restart %{name}.service


%changelog
* Thu Sep 02 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.1-0.20210902gitdffedb9ef1b7
- Update to the latest version.

* Tue Mar 02 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.0-2.20190927gitbd35d0716f7a
- Update to the latest version.

* Fri Sep 27 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.0-1.20190501git337403300df1
- Initial RPM release.
