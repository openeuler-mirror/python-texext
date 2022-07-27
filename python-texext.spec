Name:           python-texext
Version:        0.6.7
Release:        1
Summary:        Sphinx extensions for working with LaTeX math

License:        MIT
URL:            http://github.com/matthew-brett/texext
Source0:        texext-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel python3dist(docutils)  python3dist(matplotlib) python3dist(pytest) python3dist(setuptools)
BuildRequires:  python3dist(six) python3dist(sphinx) python3dist(sphinxtesters) python3dist(sympy) 

%description
This package contains Sphinx extensions for working with LaTeX math.

%package -n     python3-texext
Summary:        %{summary}
%{?python_provide:%python_provide python3-texext}

Requires:       python3dist(docutils) python3dist(matplotlib) python3dist(pytest) python3dist(six) python3dist(sphinx) 
Requires:       python3dist(sphinxtesters) python3dist(sympy) 
%description -n python3-texext
This package contains Sphinx extensions for working with LaTeX math.

%prep
%autosetup -n texext-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-texext
%license LICENSE
%doc  README.rst
%{python3_sitelib}/texext
%{python3_sitelib}/texext-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Jul 24 2022 hkgy <kaguyahatu@outlook.com> - 0.6.7
- Update to 0.6.7

* Tue May 10 2022 houyingchao <houyingchao@h-partners.com> - 0.6.6-2
- License compliance rectification

* Mon Sep 27 2021 weidong <weidong@uniontech.com> - 0.6.6-1
- Initial package.
