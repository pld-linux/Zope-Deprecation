Summary:	Deprecation library for Python code
Summary(pl.UTF-8):	Biblioteka odradzająca dla kodu w Pythonie
Name:		Zope-Deprecation
Version:	3.4.0
Release:	1
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://download.zope.org/distribution/zope.deprecation-%{version}.tar.gz
# Source0-md5:	cc5814063505f217c6df3fc93ec8b2df
URL:		http://www.zope.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
Requires:	Zope-Testing
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Deprecation library for Python code.

%description -l pl.UTF-8
Biblioteka odradzająca dla kodu w Pythonie.

%prep
%setup -q -n zope.deprecation-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/zope/deprecation
%{py_sitescriptdir}/zope.deprecation-*.egg-info
%{py_sitescriptdir}/zope.deprecation-*-nspkg.pth
