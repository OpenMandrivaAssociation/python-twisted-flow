Summary:        Generator-based async result flow module for Twisted
Name:           python-twisted-flow
Version: 0.1.0
Release: %mkrel 3
Source0:        http://tmrc.mit.edu/mirror/twisted/Flow/0.1/TwistedFlow-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/flow/
BuildRoot:      %{_tmppath}/%{name}-buildroot
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
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir


%clean
%__rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc LICENSE README doc/*
%py_platsitedir/twisted/flow/

