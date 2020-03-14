from seleniumwrapper import WebDriver, Configuration, IProxy


def get_ip(driver, ip_site="https://api.ipify.org"):
    driver.get(ip_site)
    return driver.find_element_by_tag_name("body").text


def make_selenium_instances(manager, headless=False):
    configs = []
    for info in manager.get_containers():
        config = Configuration(proxy=IProxy(
            "127.0.0.1",
            manager.get_port(info, "8123/tcp"),
            manager.get_port(info, "8118/tcp"),
            manager.get_port(info, "9050/tcp")
        ), headless=headless)
        configs.append(config)
    drivers = []
    for config in configs:
        drivers.append(WebDriver.build(config, False))
    return drivers
