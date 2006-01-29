%define	_rc	rc1
Summary:	The Zolera Soap Infrastructure
Name:		python-ZSI
Version:	2.0
Release:	0.%{_rc}.1
License:	MIT/X + LBNL BSD-style + Zope Public License
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pywebsvcs/ZSI-%{version}-%{_rc}.tar.gz
# Source0-md5:	17cbcda2bc2c702c851fca4a80341b56
URL:		http://pywebsvcs.sourceforge.net/
%pyrequires_eq	python
BuildRequires:	python-PyXML
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZSI, the Zolera SOAP Infrastructure, is a Python package that provides
an implementation of SOAP messaging, as described in The SOAP 1.1
Specification. In particular, ZSI parses and generates SOAP messages,
and converts between native Python datatypes and SOAP syntax. It can
also be used to build applications using SOAP Messages with
Attachments. ZSI is ``transport neutral'', and provides only a simple
I/O and dispatch framework; a more complete solution is the
responsibility of the application using ZSI.

%prep
%setup -q -n ZSI-%{version}-%{_rc}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.{html,css} doc/examples samples
%doc CHANGES Copyright README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/ZSI*
