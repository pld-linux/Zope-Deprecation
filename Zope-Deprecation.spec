Summary:	zope.deprecation package used in Zope 3
Name:		Zope-Deprecation
Version:	3.4.0
Release:	0.1
License:	ZPL 2.0
Group:		Development/Tools
Source0:	http://download.zope.org/distribution/zope.deprecation-%{version}.tar.gz
# Source0-md5:	cc5814063505f217c6df3fc93ec8b2df
URL:		http://pypi.python.org/pypi/zope.deprecation/3.5.1
BuildRequires:	python
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zope.deprecation package used in Zope 3.

%prep
%setup -q -n zope.deprecation-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%{py_postclean}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/zope/deprecation
%{py_sitescriptdir}/zope*egg*
%{py_sitescriptdir}/zope*pth
