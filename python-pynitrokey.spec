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
# docs/packaging.md says to replace this file with distro-specific instructions
echo 'PCSC_ABSENT = "Please install %{name}+pcsc using dnf to enable PCSC support"' > pynitokey/cli/nk3/pcsc_absent.py

%pyproject_patch_dependency hidapi:drop_upper

%if 0%{fedora} < 44
%pyproject_patch_dependency click:drop_lower
%endif

%generate_buildrequires
%pyproject_buildrequires -x pcsc


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pynitrokey -L


%check
%pyproject_check_import
%pytest


%files -n python3-pynitrokey -f %{pyproject_files}
%{_bindir}/nitropy
%license LICENSES/*


%changelog
%autochangelog
