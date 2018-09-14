import socket
import os


class Macaroni:
    def __init__(self, username):
        self.username = username

    def _check_connectivity(host="8.8.8.8", port=53, timeout=3):
        """
        Host: 8.8.8.8 (google-public-dns-a.google.com)
        OpenPort: 53/tcp
        Service: domain (DNS/TCP)
        """
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except OSError as e:
            print(e)
            return False

    def create_bash_profile_bashrc(self):
        try:
            profile = open('/Users/{}/.bash_profile'.format(self.username), 'w')
            profile.write("if [ -f ~/.bashrc ]; then\n\t\tsource ~/.bashrc\nfi\n")
            rc = open('/Users/{}/.bashrc'.format(self.username), 'w')
            rc.close()
            return True
        except FileNotFoundError as e:
            print(e)
            return False

    def install_python3_add_alias(self):
        try:
            os.system('brew reinstall python@3')
            rc = open('/Users/{}/.bashrc'.format(self.username), 'a')
            rc.write("alias python=python3\nalias pip=pip3\n")
            rc.close()
            return True
        except Exception as e:
            print(e)
            return False

    def install_java8_add_path(self):
        os.system('brew tap caskroom/versions')
        os.system('brew cask reinstall java8')
        rc = open('/Users/{}/.bashrc'.format(self.username), 'a')
        rc.write("export JAVA_HOME=$(/usr/libexec/java_home)")
        rc.close()
