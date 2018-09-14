import socket
import os


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


def _create_bash_profile_bashrc(username):
    try:
        profile = open('/Users/{}/.bash_profile'.format(username), 'w')
        profile.write("if [ -f ~/.bashrc ]; then\n\t\tsource ~/.bashrc\nfi\n")
        rc = open('/Users/{}/.bashrc'.format(username), 'w')
        rc.close()
        return True
    except FileNotFoundError as e:
        print(e)
        return False


def _install_python3_add_alias(username):
    os.system('brew reinstall python@3')
    rc = open('/Users/{}/.bashrc'.format(username), 'a')
    rc.write("alias python=python3\nalias pip=pip3\n")
    rc.close()
    return True


def _install_java8_add_path(username):
    os.system('brew tap caskroom/versions')
    os.system('brew cask reinstall java8')
    rc = open('/Users/{}/.bashrc'.format(username), 'a')
    rc.write("export JAVA_HOME=$(/usr/libexec/java_home)")
    rc.close()


if __name__ == '__main__':
    r = _install_java8_add_path('soumasishgoswami')
    print(r)
