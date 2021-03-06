# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate hyper

Name:           rust-%{crate}
Version:        0.12.35
Release:        1%{?dist}
Summary:        Fast and correct HTTP library

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/hyper
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast and correct HTTP library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+__internal_flaky_tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__internal_flaky_tests-devel %{_description}

This package contains library source intended for building other packages
which use "__internal_flaky_tests" feature of "%{crate}" crate.

%files       -n %{name}+__internal_flaky_tests-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+__internal_happy_eyeballs_tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+__internal_happy_eyeballs_tests-devel %{_description}

This package contains library source intended for building other packages
which use "__internal_happy_eyeballs_tests" feature of "%{crate}" crate.

%files       -n %{name}+__internal_happy_eyeballs_tests-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+futures-cpupool-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-cpupool-devel %{_description}

This package contains library source intended for building other packages
which use "futures-cpupool" feature of "%{crate}" crate.

%files       -n %{name}+futures-cpupool-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+net2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+net2-devel %{_description}

This package contains library source intended for building other packages
which use "net2" feature of "%{crate}" crate.

%files       -n %{name}+net2-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+nightly-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+nightly-devel %{_description}

This package contains library source intended for building other packages
which use "nightly" feature of "%{crate}" crate.

%files       -n %{name}+nightly-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+runtime-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+runtime-devel %{_description}

This package contains library source intended for building other packages
which use "runtime" feature of "%{crate}" crate.

%files       -n %{name}+runtime-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages
which use "tokio" feature of "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-executor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-executor-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-executor" feature of "%{crate}" crate.

%files       -n %{name}+tokio-executor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-reactor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-reactor-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-reactor" feature of "%{crate}" crate.

%files       -n %{name}+tokio-reactor-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-tcp-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-tcp-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-tcp" feature of "%{crate}" crate.

%files       -n %{name}+tokio-tcp-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-threadpool-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-threadpool-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-threadpool" feature of "%{crate}" crate.

%files       -n %{name}+tokio-threadpool-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+tokio-timer-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-timer-devel %{_description}

This package contains library source intended for building other packages
which use "tokio-timer" feature of "%{crate}" crate.

%files       -n %{name}+tokio-timer-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Feb 13 12:16:33 MSK 2020 Nikita Kretov <nkretov@croc.ru> - 0.12.35-1
- Initial package
