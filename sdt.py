from selenium_docktor import get_ip, make_selenium_instances, WebDriver, Configuration
from docktor import Manager

from loguru import logger
from time import sleep


def main():
    clearnet_driver = WebDriver.build(Configuration())
    logger.info("browser w/o proxy: {0}".format(get_ip(clearnet_driver)))

    logger.info("initializing docktor manager")
    manager = Manager(2)
    logger.info("running docktor manager")
    manager.start()
    logger.info("waiting for the containers to start")
    sleep(5)
    manager.wait_until_ready()

    logger.info("tor proxy ips:")
    for tor_driver in make_selenium_instances(manager):
        logger.info(get_ip(tor_driver))

    logger.info("changing identities")
    manager.change_all_identities()

    logger.info("new tor proxy ips:")
    for tor_driver in make_selenium_instances(manager):
        logger.info(get_ip(tor_driver))

    manager.stop()
    manager.join()


if __name__ == '__main__':
    main()
