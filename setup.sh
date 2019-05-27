#!/usr/bin/env bash
main(){
  python=false
  java=false
  node=false
  go=false
  while getopts :pjng option; do
      case $option in
          p)python=true;;
          j)java=true;;
          n)node=true;;
          g)go=true;;
          ?)echo "Unrecognized Flag."
      esac
  done
  create_bashrc
  install_essentials
  make_bash_nicer
  create_common_aliases
  if [ $python = true ]; then
    install_python
  fi
  if [ $java = true ]; then
    install_java
  fi
  if [ $node = true ]; then
    install_node
  fi
  if [ $go = true ]; then
    install_go
  fi
}

create_bashrc(){
  echo "if [ -f ~/.bashrc ]; then
      source ~/.bashrc
  fi" >> ~/.bashrc
}
install_essentials(){
  echo "Installing Brew"
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  brew install git
}

make_bash_nicer(){
  echo export HISTCONTROL="ignorespace:ignoredups" >> ~/.bashrc
}

create_common_aliases(){
  echo "alias ll=ls -lAH"
}

install_python(){
  echo "Installing Python 3"
  brew install python
  echo "alias python=python3" >> ~/.bashrc
  echo "alias pip=pip3" >> ~/.bashrc
}
install_java(){
  echo "Installing Java 8 & 11 and setting JAVA_HOME to 8"
  brew tap adoptopenjdk/openjdk
  brew cask install adoptopenjdk8
  brew cask install adoptopenjdk11
  echo "export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_131.jdk/Contents/Home"
}
install_node(){

}
install_go(){

}
main; exit
