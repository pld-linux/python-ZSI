Summary:	The Zolera SOAP Infrastructure
Summary(pl.UTF-8):	Infrastruktura Zolera SOAP
Name:		python-ZSI
Version:	2.0
Release:	4
License:	MIT/X + LBNL BSD-style + Zope Public License
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pywebsvcs/ZSI-%{version}.tar.gz
# Source0-md5:	bb706337cafe9e2201b06b1bce71ca0f
URL:		http://pywebsvcs.sourceforge.net/
%pyrequires_eq	python
Requires:	python-PyXML >= 0.8.4-6
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

%description -l pl.UTF-8
ZSI, czyli Zolera SOAP Infrastructure, to pakiet Pythona zawierający
implementację komunikacji SOAP zgodną ze specyfikacją SOAP 1.1. W
szczególności ZSI przetwarza i generuje komunikaty SOAP oraz dokonuje
konwersji między natywnymi typami danych Pythona a składnią SOAP. Może
być także używane do tworzenia aplikacji przy użyciu komunikatów SOAP
z załącznikami. ZSI jest niezależne od transportu i udostępnia jedynie
prostego szkieletu we/wy i wysyłania; za pełniejsze rozwiązanie
odpowiada aplikacja korzystająca z ZSI.

%prep
%setup -q -n ZSI-%{version}

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
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/ZSI*
