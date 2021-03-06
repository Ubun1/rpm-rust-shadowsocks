# Generated by rust2rpm 13
%bcond_without check

%global crate shadowsocks-rust

Name:           rust-%{crate}
Version:        1.7.0
Release:        1%{?dist}
Summary:        Shadowsocks is a fast tunnel proxy that helps you bypass firewalls

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/shadowsocks-rust
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(base64/default) >= 0.10.0 with crate(base64/default) < 0.11.0)
BuildRequires:  (crate(byte_string/default) >= 1.0.0 with crate(byte_string/default) < 2.0.0)
BuildRequires:  (crate(byteorder/default) >= 1.2.0 with crate(byteorder/default) < 2.0.0)
BuildRequires:  (crate(bytes/default) >= 0.4.0 with crate(bytes/default) < 0.5.0)
BuildRequires:  (crate(clap/default) >= 2.0.0 with crate(clap/default) < 3.0.0)
BuildRequires:  (crate(digest/default) >= 0.8.0 with crate(digest/default) < 0.9.0)
BuildRequires:  (crate(dns-parser/default) >= 0.8.0 with crate(dns-parser/default) < 0.9.0)
BuildRequires:  (crate(env_logger/default) >= 0.5.0 with crate(env_logger/default) < 0.6.0)
BuildRequires:  (crate(futures/default) >= 0.1.0 with crate(futures/default) < 0.2.0)
BuildRequires:  (crate(json5/default) >= 0.2.0 with crate(json5/default) < 0.3.0)
BuildRequires:  (crate(libc/default) >= 0.2.0 with crate(libc/default) < 0.3.0)
BuildRequires:  (crate(log/default) >= 0.4.0 with crate(log/default) < 0.5.0)
BuildRequires:  (crate(lru-cache/default) >= 0.1.0 with crate(lru-cache/default) < 0.2.0)
BuildRequires:  (crate(md-5/default) >= 0.8.0 with crate(md-5/default) < 0.9.0)
BuildRequires:  (crate(openssl/default) >= 0.10.0 with crate(openssl/default) < 0.11.0)
BuildRequires:  (crate(qrcode) >= 0.10.0 with crate(qrcode) < 0.11.0)
BuildRequires:  (crate(rand/default) >= 0.5.0 with crate(rand/default) < 0.6.0)
BuildRequires:  (crate(ring/default) >= 0.13.0 with crate(ring/default) < 0.14.0)
BuildRequires:  (crate(spin) >= 0.5.0 with crate(spin) < 0.6.0)
BuildRequires:  (crate(time/default) >= 0.1.0 with crate(time/default) < 0.2.0)
BuildRequires:  (crate(tokio-io/default) >= 0.1.0 with crate(tokio-io/default) < 0.2.0)
BuildRequires:  (crate(tokio-process/default) >= 0.2.3 with crate(tokio-process/default) < 0.3.0)
BuildRequires:  (crate(tokio-signal/default) >= 0.2.0 with crate(tokio-signal/default) < 0.3.0)
BuildRequires:  (crate(tokio/default) >= 0.1.0 with crate(tokio/default) < 0.2.0)
BuildRequires:  (crate(typenum/default) >= 1.10.0 with crate(typenum/default) < 2.0.0)
BuildRequires:  (crate(url/default) >= 1.0.0 with crate(url/default) < 2.0.0)
%endif

%global _description %{expand:
Shadowsocks is a fast tunnel proxy that helps you bypass firewalls.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%{_bindir}/ssserver
%{_bindir}/ssurl
%{_bindir}/ssdns
%{_bindir}/sslocal
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+rc4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rc4-devel %{_description}

This package contains library source intended for building other packages
which use "rc4" feature of "%{crate}" crate.

%files       -n %{name}+rc4-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+sodium-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sodium-devel %{_description}

This package contains library source intended for building other packages
which use "sodium" feature of "%{crate}" crate.

%files       -n %{name}+sodium-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Sun Feb 16 09:55:33 MSK 2020 Nikita Kretov <nkretov@croc.ru> - 1.7.0-1
- Initial package
