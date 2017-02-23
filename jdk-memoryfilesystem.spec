Name     : jdk-memoryfilesystem
Version  : 0.6.7
Release  : 1
URL      : http://repo1.maven.org/maven2/com/github/marschall/memoryfilesystem/0.6.7/memoryfilesystem-0.6.7.jar
Source0  : http://repo1.maven.org/maven2/com/github/marschall/memoryfilesystem/0.6.7/memoryfilesystem-0.6.7.jar
Source1  : http://repo1.maven.org/maven2/com/github/marschall/memoryfilesystem/0.6.7/memoryfilesystem-0.6.7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
Memory File System [![Build Status](https://travis-ci.org/marschall/memoryfilesystem.png?branch=master)](https://travis-ci.org/marschall/memoryfilesystem) [![Maven Central](https://maven-badges.herokuapp.com/maven-central/cz.jirutka.rsql/rsql-parser/badge.svg)](https://maven-badges.herokuapp.com/maven-central/com.github.marschall/memoryfilesystem)
==================
An in memory implementation of a [JSR-203](http://jcp.org/en/jsr/detail?id=203) (Java 7) file system for testing purposes.

%prep
mv %{SOURCE1} pom.xml

python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :maven-source-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :maven-release-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :maven-javadoc-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  com.github.marschall:jdeps-maven-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  org.jboss.jandex:jandex-maven-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep com.github.marschall:zipfilesystem-standalone
python3 /usr/share/java-utils/pom_editor.py pom_remove_dep org.openjdk.jol:jol-core
sed -i '/jandex.idx/d' pom.xml
rm -rf ./src/test/java/com/github/marschall/memoryfilesystem/MemoryFileTest.java
rm -rf ./src/test/java/com/github/marschall/memoryfilesystem/ZipFileSystemInteropabilityTest.java

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms/memoryfilesystem
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java/memoryfilesystem

mv %{SOURCE0} %{buildroot}/usr/share/java/memoryfilesystem/memoryfilesystem.jar
mv pom.xml %{buildroot}/usr/share/maven-poms/memoryfilesystem/memoryfilesystem.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/memoryfilesystem.xml \
%{buildroot}/usr/share/maven-poms/memoryfilesystem/memoryfilesystem.pom \
%{buildroot}/usr/share/java/memoryfilesystem/memoryfilesystem.jar

%files
%defattr(-,root,root,-)
/usr/share/java/memoryfilesystem/memoryfilesystem.jar
/usr/share/maven-metadata/memoryfilesystem.xml
/usr/share/maven-poms/memoryfilesystem/memoryfilesystem.pom
