# TODO
# - why it was needed to move code to py_sitedir in 99929afd5fede7d191f944c30d2cfa692454ba84 ?
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Deprecation library for Python code
Summary(pl.UTF-8):	Biblioteka odradzająca dla kodu w Pythonie
Name:		Zope-Deprecation
Version:	4.0.2
Release:	2
License:	ZPL 2.1
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/z/zope.deprecation/zope.deprecation-%{version}.tar.gz
# Source0-md5:	5f8cecce85f2783f9e020f1288e908fd
URL:		http://docs.zope.org/zope.deprecation/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	Zope-Testing
Requires:	python-modules
# not noarch because of py_sitedir in 99929afd5fede7d191f944c30d2cfa692454ba84
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a simple function called deprecated(names, reason) to
mark deprecated modules, classes, functions, methods and properties.

%description -l pl.UTF-8
Biblioteka odradzająca dla kodu w Pythonie.

%prep
%setup -q -n zope.deprecation-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--install-purelib=%{py_sitedir} \
	--skip-build \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/zope/deprecation/tests.py[co]

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt
%dir %{py_sitedir}/zope/deprecation
%{py_sitedir}/zope/deprecation/*.py[co]
%{py_sitedir}/zope.deprecation-*.egg-info
%{py_sitedir}/zope.deprecation-*-nspkg.pth
