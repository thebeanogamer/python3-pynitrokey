Name:           python-nitrokey
Version:        0.4.2
Release:        %autorelease
Summary:        Nitrokey Python SDK

License:        Apache-2.0 OR MIT
URL:            https://github.com/Nitrokey/nitrokey-sdk-py
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
%{summary}.}

%description %_description

%package -n     python3-nitrokey
Summary:        %{summary}

%description -n python3-nitrokey %_description


%prep
%autosetup -p1 -n nitrokey-sdk-py-%{version}

%pyproject_patch_dependency hidapi:drop_upper


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l nitrokey


%check
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-nitrokey -f %{pyproject_files}


%changelog
%autochangelog
