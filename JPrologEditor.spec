Summary:	J Prolog Editor is an editor (written in Java) for SWI-Prolog 
Summary(pl):	J Prolog Editor to edytor (napisany w Javie) dla jêzyka SWI-Prolog
Name:		JPrologEditor
Version:	1.1
Release:	1
License:	Public Domain	
Group:		Development/Tools
Source0:	http://520094857424.bei.t-online.de/JPrologEditor/%{name}.jar
# Source0-md5:	b69363f07ffc3ea6f2ad702a709dc6b8
URL:		http://520094857424.bei.t-online.de/JPrologEditor
Requires:       jre >= 1.3.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
J Prolog Editor is an editor (written in Java) for SWI-Prolog (www.swi-prolog.org) providing syntax highlighting, an embedded Prolog interpreter and other features.

%description -l pl
J Prolog Editor to edytor (napisany w Javie) dla jêzyka SWI-Prolog. Obs³ugujê pod¶wietlanie sk³adni, wbudowany interpreter Prologu oraz wiele innych mo¿liwo¶ci.

%prep
%setup -q -c -T

%build
cat > %{name} <<EOF
#!/bin/sh
java -jar %{_javadir}/%{name}.jar
EOF

cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=J Prolog Editor
Comment=J Prolog Editor is an SWI-Prolog editor
Exec=%{name}
Categories=Java;Development;IDE;
Terminal=false
# vi: encoding=utf-8
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir},%{_desktopdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE0}  $RPM_BUILD_ROOT%{_javadir}
install %{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_javadir}/*.jar
%{_desktopdir}/%{name}.desktop
