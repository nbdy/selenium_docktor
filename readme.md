## selenium-docktor
infinite proxy ips with the selenium webdriver

### how to use it?
check 'sdt.py' in this repo
<br>condensed code:
```python
from selenium_docktor import make_selenium_instances, get_ip
from docktor import Manager

def check_ips(drvs):
    for driver in drvs:
        print(get_ip(driver))

manager = Manager(2)  # 2 instances for testing
drivers = make_selenium_instances(manager)  # create firefox instances with a proxy profile
check_ips(drivers)  # or do other stuff
manager.change_all_identities()  # change identities of all containers
drivers = make_selenium_instances(manager)  # needs to be done after every ip renew
check_ips(drivers)  # outputs new ips
```