# Disable the debuginfo build operation
%global debug_package %{nil}

%if 0%{?fedora}
%bcond_without python3
%else
%if 0%{?rhel} >= 8
%bcond_without python3
%else
%bcond_with python3
%endif
%endif

Name:       {{{ git_dir_name }}}
Version:    {{{ git_dir_version }}}
Release:    1%{?dist}
Summary:    Provides a simple interface for the Red Hat Security Data API

License:    GPL
URL:        https://github.com/RedHatOfficial/rhsecapi
Source:     {{{ git_dir_pack }}}

%if %{with python3}
BuildRequires:  python3-devel python3-setuptools
Requires:	python3-requests python3-%{name}
%else
BuildRequires:  python-devel python-setuptools
Requires:	python-argparse python-requests python-%{name}
%endif

%description
Leverage Red Hat's Security Data API to find CVEs by various attributes
(date, severity, scores, package, IAVA, etc). Retrieve customizable details
about found CVEs or about specific CVE ids input on cmdline. Parse
arbitrary stdin for CVE ids and generate a customized report, optionally
sending it straight to pastebin. Searches are done via a single
instantaneous http request and CVE retrieval is parallelized, utilizing
multiple threads at once. Python requests is used for all remote
communication, so proxy support is baked right in. BASH intelligent
tab-completion is supported via optional Python argcomplete module. Python2
tested on RHEL6, RHEL7, & Fedora and Python3 on Fedora but since it doesnt
integrate with RHN/RHSM/yum/Satellite, it can be used on any
internet-connected machine. Feedback, feature requests, and code
contributions welcome.

%if %{with python3}
%package     -n python3-%{name}
Summary:    Provides a simple interface for the Red Hat Security Data API

%description -n python3-%{name}
Leverage Red Hat's Security Data API to find CVEs by various attributes
(date, severity, scores, package, IAVA, etc). Retrieve customizable details
about found CVEs or about specific CVE ids input on cmdline. Parse
arbitrary stdin for CVE ids and generate a customized report, optionally
sending it straight to pastebin. Searches are done via a single
instantaneous http request and CVE retrieval is parallelized, utilizing
multiple threads at once. Python requests is used for all remote
communication, so proxy support is baked right in. BASH intelligent
tab-completion is supported via optional Python argcomplete module. Python2
tested on RHEL6, RHEL7, & Fedora and Python3 on Fedora but since it doesnt
integrate with RHN/RHSM/yum/Satellite, it can be used on any
internet-connected machine. Feedback, feature requests, and code
contributions welcome.
%else
%package     -n python2-%{name}
Summary:    Provides a simple interface for the Red Hat Security Data API

%description -n python2-%{name}
Leverage Red Hat's Security Data API to find CVEs by various attributes
(date, severity, scores, package, IAVA, etc). Retrieve customizable details
about found CVEs or about specific CVE ids input on cmdline. Parse
arbitrary stdin for CVE ids and generate a customized report, optionally
sending it straight to pastebin. Searches are done via a single
instantaneous http request and CVE retrieval is parallelized, utilizing
multiple threads at once. Python requests is used for all remote
communication, so proxy support is baked right in. BASH intelligent
tab-completion is supported via optional Python argcomplete module. Python2
tested on RHEL6, RHEL7, & Fedora and Python3 on Fedora but since it doesnt
integrate with RHN/RHSM/yum/Satellite, it can be used on any
internet-connected machine. Feedback, feature requests, and code
contributions welcome.
%endif

%prep
{{{ git_dir_setup_macro }}}

%build
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

%if %{with python3}
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
%else
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%{__python3} setup.py install -O1 --root $RPM_BUILD_ROOT/
%else
%{__python} setup.py install -O1 --root $RPM_BUILD_ROOT/
%endif

%files
%{_bindir}/*
# For noarch packages: sitelib
%if %{with python3}
%files -n python3-%{name}
%{_bindir}/*
# For noarch packages: sitelib
%{python3_sitelib}/*
%else
%files -n python2-%{name}
%{python_sitelib}/*
%endif

%changelog
{{{ git_dir_changelog }}}

