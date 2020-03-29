from seleniumwrapper import WebDriver, Configuration, IProxy


def get_ip(driver, ip_site="https://api.ipify.org"):
    """
    gets ip from specified page
    :param driver: selenium webdriver object
    :param ip_site: ip site, which only returns ip as string
    :return: str of current ip address
    """
    driver.get(ip_site)
    return driver.find_element_by_tag_name("body").text


def make_selenium_instances(manager, headless=True, profile=None):
    """
    creates web driver instances
    :param manager: docktor Manager object
    :param headless: bool value
    :param profile: profile name
    :return: list with driver instances
    """
    drivers = []
    for info in manager.get_containers():
        drivers.append(WebDriver.build(Configuration(proxy=IProxy(
            "127.0.0.1",
            manager.get_port(info, "8123/tcp"),
            manager.get_port(info, "8118/tcp"),
            manager.get_port(info, "9050/tcp")
        ), headless=headless, profile=profile)))
        print(drivers[-1].capabilities)
    return drivers
