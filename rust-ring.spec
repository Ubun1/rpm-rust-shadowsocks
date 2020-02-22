# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate ring

Name:           rust-%{crate}
Version:        0.16.1
Release:        1%{?dist}
Summary:        Safe, fast, small crypto using Rust

# Upstream license specification: None
License:        # FIXME

URL:            https://crates.io/crates/ring
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(cc) >= 1.0.37 with crate(cc) < 2.0.0)
BuildRequires:  (crate(lazy_static) >= 1.3.0 with crate(lazy_static) < 2.0.0)
BuildRequires:  (crate(libc) >= 0.2.48 with crate(libc) < 0.3.0)
BuildRequires:  (crate(spin) >= 0.5.0 with crate(spin) < 0.6.0)
BuildRequires:  (crate(untrusted/default) >= 0.7.0 with crate(untrusted/default) < 0.8.0)
%endif

%global _description %{expand:
Safe, fast, small crypto using Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc doc/link-to-readme.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages
which use "alloc" feature of "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+dev_urandom_fallback-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dev_urandom_fallback-devel %{_description}

This package contains library source intended for building other packages
which use "dev_urandom_fallback" feature of "%{crate}" crate.

%files       -n %{name}+dev_urandom_fallback-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+internal_benches-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+internal_benches-devel %{_description}

This package contains library source intended for building other packages
which use "internal_benches" feature of "%{crate}" crate.

%files       -n %{name}+internal_benches-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages
which use "lazy_static" feature of "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+slow_tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+slow_tests-devel %{_description}

This package contains library source intended for building other packages
which use "slow_tests" feature of "%{crate}" crate.

%files       -n %{name}+slow_tests-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages
which use "std" feature of "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+test_logging-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+test_logging-devel %{_description}

This package contains library source intended for building other packages
which use "test_logging" feature of "%{crate}" crate.

%files       -n %{name}+test_logging-devel
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
* Sat Feb 22 19:56:52 MSK 2020 Nikita Kretov <nkretov@croc.ru> - 0.16.1-1
- Initial package
