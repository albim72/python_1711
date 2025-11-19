import pandas as pd
import pkg_resources

packages = pkg_resources.working_set
for package in packages:
    print(package)
