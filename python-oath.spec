Name:           python-oath
Version:        1.4.4
Release:        %autorelease
Summary:        Python implementation of HOTP, TOTP and OCRA

License:        MIT
URL:            https://github.com/bdauvergne/python-oath
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
%{summary}.}

%description %_description

%package -n     python3-oath
Summary:        %{summary}

%description -n python3-oath %_description


%prep
%autosetup -p1 -n python-oath-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files oath


%check
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-oath -f %{pyproject_files}


%changelog
%autochangelog
