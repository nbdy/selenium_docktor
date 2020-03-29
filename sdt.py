from selenium_docktor import get_ip, make_selenium_instances, WebDriver
from docktor import Manager

from time import sleep


def main():
    clearnet_driver = WebDriver.get_default()
    print("browser w/o proxy: {0}".format(get_ip(clearnet_driver)))

    print("initializing docktor manager")
    manager = Manager(2)
    print("running docktor manager")
    manager.start()
    print("waiting for the containers to start")
    sleep(5)
    manager.wait_until_ready()

    print("tor proxy ips:")
    for tor_driver in make_selenium_instances(manager, False):
        print(get_ip(tor_driver))

    print("changing identities")
    manager.change_all_identities()

    print("new tor proxy ips:")
    for tor_driver in make_selenium_instances(manager):
        print(get_ip(tor_driver))

    manager.stop()
    manager.join()


if __name__ == '__main__':
    main()
