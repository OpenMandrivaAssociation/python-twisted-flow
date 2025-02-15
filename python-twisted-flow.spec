%define debug_package %{nil}

Summary:    Generator-based async result flow module for Twisted
Name:       python-twisted-flow
Version:	8.2.0
Release:	6
Source0:    http://tmrc.mit.edu/mirror/twisted/Flow/0.1/TwistedFlow-%{version}.tar.bz2
License:    MIT
Group:      Development/Python
URL:        https://twistedmatrix.com/projects/flow/
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core
# for twisted.flow.web
Requires:       python-twisted-web

%description
Flow is a generator-based async result flow module for Twisted.

%prep
%setup -q -n TwistedFlow-%version

%build
%__python setup.py build

%install
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir

%files
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%{py_platsitedir}/twisted/flow/
%{py_platsitedir}/Twisted_Flow-*-py*.egg-info
