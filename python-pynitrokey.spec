Name:           python-pynitrokey
Version:        0.12.3
Release:        %autorelease
Summary:        Python client for Nitrokey devices

License:        Apache-2.0 OR MIT
URL:            https://github.com/Nitrokey/pynitrokey
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies (as the generator can't parse Poetry dev deps)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(oath)

%global _description %{expand:
A command line interface for the Nitrokey FIDO2, Nitrokey Start, Nitrokey 3 and NetHSM.}

%description %_description

%package -n     python3-pynitrokey
Summary:        %{summary}

Requires:       libnitrokey
Recommends:     %{name}+pcsc = %{version}

%description -n python3-pynitrokey %_description

%pyproject_extras_subpkg -n python3-pynitrokey pcsc


%prep
%autosetup -p1 -n pynitrokey-%{version}

%pyproject_patch_dependency hidapi:drop_upper

%generate_buildrequires
%pyproject_buildrequires -x pcsc


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pynitrokey


%check
%pyproject_check_import
%pytest


%files -n python3-pynitrokey -f %{pyproject_files}
%{_bindir}/nitropy


%changelog
%autochangelog
