%global date 20250117
%global commit0 1336b21511b5c3441d35d9a16c097e20ac73e239
%global shortcommit0 %(c=%{commit0}; echo ${c:0:12})
%global the_owner dwrobel

Name:           mqtt-mysensors
Version:        2.3.4
Release:        1.%{date}git%{shortcommit0}%{?dist}
Summary:        MQTT service for mysensors serial gateway
License:        GPLv3+
Url:            https://github.com/%{the_owner}/%{name}
Source0:        https://github.com/%{the_owner}/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{date}git%{shortcommit0}.tar.gz
BuildArch:      noarch

BuildRequires:  %{py3_dist setuptools}
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros

Requires:       systemd

%description
Provides MySensors MQTT service using a mysensors serial gateway version >=2.3


%package udev
Summary:        mysensor udev rules

BuildRequires:  systemd-udev

Requires:       systemd-udev
Requires:       mqtt-mysensors = %{version}-%{release}


%generate_buildrequires
%pyproject_buildrequires

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
* Fri Jan 17 2025 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.4-2.20250117git6aad64d17cce
- Update to the latest version

* Fri Dec 22 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.2-3.20230717git0d56fac7ace2
- Rebuild for F39

* Fri Jul 21 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.2-2.20230717git2e55a0e0051f
- Add resseting mysensor device

* Wed Jul 12 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.2-2.20210902git2e55a0e0051f
- Rebuild for python-3.12

* Thu Sep 02 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.2-1.20210902git2e55a0e0051f
- Update to the latest version.

* Thu Sep 02 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.1-2.20210902gitdffedb9ef1b7
- Add BR python setuptools.

* Thu Sep 02 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.1-0.20210902gitdffedb9ef1b7
- Update to the latest version.

* Tue Mar 02 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.0-2.20190927gitbd35d0716f7a
- Update to the latest version.

* Fri Sep 27 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.3.0-1.20190501git337403300df1
- Initial RPM release.
