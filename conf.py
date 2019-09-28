import os
from enum import Enum


class BrowserTypes(Enum):
    os_platform = os.name
    executable_suffix = '.exe' if 'nt' in os_platform else ''

    Firefox = 'geckodriver' + executable_suffix
    Chrome = 'chromedriver' + executable_suffix
    Ie = 'MicrosoftWebDriver' + executable_suffix
