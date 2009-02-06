%define oname uiautomationwinforms

Name:     	mono-%{oname}
Version:	0.9.1
Release:	%mkrel 1
License:	MIT or X11
URL:		http://www.mono-project.com/Accessibility
Source0:	ftp://ftp.novell.com/pub/mono/uia/%{oname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	mono-devel >= 2.2
BuildRequires:	mono-uia >= 0.9
BuildRequires:	glib-sharp2
BuildRequires:	gtk-sharp2
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

%clean
rm -rf %buildroot

%files
%defattr(-, root, root)
%_prefix/lib/mono/gac/UIAutomationWinforms
%_prefix/lib/uiautomationwinforms
