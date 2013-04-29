Summary:        Generator-based async result flow module for Twisted
Name:           python-twisted-flow
Version:  	8.2.0
Release:	    3
Source0:        http://tmrc.mit.edu/mirror/twisted/Flow/0.1/TwistedFlow-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/flow/
BuildRequires:	python-devel python-twisted-core
Requires:       python-twisted-core
# for twisted.flow.web
Requires:       python-twisted-web

%define debug_package %{nil}

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
%py_platsitedir/Twisted_Flow-*-py*.egg-info


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 8.2.0-2mdv2010.0
+ Revision: 442515
- rebuild

* Sat Jan 03 2009 Jérôme Soyer <saispo@mandriva.org> 8.2.0-1mdv2009.1
+ Revision: 323852
- New upstream release

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 8.0.0-2mdv2009.1
+ Revision: 323412
- rebuild

* Sun Jul 27 2008 Oden Eriksson <oeriksson@mandriva.com> 8.0.0-1mdv2009.0
+ Revision: 250535
- 8.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Fri Jan 27 2006 Michael Scherer <misc@mandriva.org> 0.1.0-3mdk
- make it noarch, in order to make it work on x86_64, use macro

* Sun May 15 2005 Michael Scherer <misc@mandriva.org> 0.1.0-2mdk
- fix requires

* Sat May 14 2005 Michael Scherer <misc@mandriva.org> 0.1.0-1mdk
- Initial package

