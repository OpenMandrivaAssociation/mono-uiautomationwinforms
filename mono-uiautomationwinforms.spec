%define oname uiautomationwinforms

Name:     	mono-%{oname}
Version:	2.1
Release:	%mkrel 1
License:	MIT or X11
URL:		https://www.mono-a11y.org/
Source0:	http://mono-a11y.org/releases/%{version}/sources/%{oname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	mono-devel >= 2.4
BuildRequires:	mono-uia >= 2.0
BuildRequires:	glib-sharp2
BuildRequires:	gtk-sharp2
BuildRequires:	intltool >= 0.35.0
Summary:	Implementation of Microsoft's UI Automation specification
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
UIAutomationWinforms is a project of the Mono Accessibility team. Its purpose
is to implement provider pattern interfaces defined in Microsoft's UI Automation
(UIA) specification for the standard controls provided by System.Windows.Forms.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x --libdir=%_prefix/lib
make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang UIAutomationWinforms

%clean
rm -rf %buildroot

%files -f UIAutomationWinforms.lang
%defattr(-, root, root)
%_prefix/lib/mono/gac/UIAutomationWinforms
%_prefix/lib/uiautomationwinforms
