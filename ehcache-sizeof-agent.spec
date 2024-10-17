%{?_javapackages_macros:%_javapackages_macros}
Name:          ehcache-sizeof-agent
Version:       1.0.1
Release:       6.0%{?dist}
Summary:       Ehcache Size Of Agent
License:       ASL 2.0
URL:           https://www.terracotta.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/sizeof-agent-1.0.1
# tar czf ehcache-sizeof-agent-1.0.1.tar.gz sizeof-agent-1.0.1
Source0:       %{name}-%{version}.tar.gz
# ehcache-sizeof-agent package don't include the license file
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: java-devel

BuildRequires: maven-local
BuildRequires: maven-shared
BuildRequires: maven-gpg-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-pmd-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-release-plugin
BuildRequires: ehcache-parent
Requires:      ehcache-parent
BuildArch:     noarch

%description
Ehcache is a widely used, pure Java, in-process, distributed cache.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep

%setup -q -n sizeof-agent-%{version}

cp %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%build

%mvn_file :sizeof-agent %{name}
%mvn_build 

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Aug 08 2013 gil cattaneo <puntogil@libero.it> 1.0.1-6
- fix rhbz#992185
- install license file
- switch to XMvn
- minor changes to adapt to current guideline

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Andy Grimm <agrimm@gmail.com> - 1.0.1-4
- Add maven-local and maven-shared to BuildRequires (RHBZ#913968)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 17 2012 David Nalley <david@gnsa.us> - 1.0.1-1
- Initial rpm build
