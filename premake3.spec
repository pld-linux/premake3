Summary:	Cross-platform build configuration tool
Summary(pl.UTF-8):	Międzyplatformowe narzędzie do budowy projektów
Name:		premake3
Version:	3.7
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://http.debian.net/debian/pool/main/p/premake/premake_%{version}.orig.tar.gz
# Source0-md5:	a328ea385f2bbf65007df36c74cb4f8c
Patch0:		%{name}-system-lua.patch
Patch1:		%{name}-flags.patch
URL:		http://industriousone.com/premake/
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Premake is a build configuration tool that can generate project files
for:
 - GNU make
 - Code::Blocks
 - CodeLite
 - MonoDevelop
 - SharpDevelop
 - Apple XCode
 - Microsoft Visual Studio

%description -l pl.UTF-8
Premake jest narzędziem do budowy projektów, które potrafi wygenerować
pliki projektów dla:
 - GNU make
 - Code::Blocks
 - CodeLite
 - MonoDevelop
 - SharpDevelop
 - Apple XCode
 - Microsoft Visual Studio

%prep
%setup -q -n premake-%{version}.orig
%patch0 -p1
%patch1 -p1

sed -i -e's/@\$(CC/$(CC/g;s/@\$(BLD/$(BLD/' Src/Makefile

%build
CC="%{__cc}" \
OPTFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CONFIG="Release" \
	verbose=true

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -a bin/premake $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{_bindir}/premake
