

import re

zen_fragment = """Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

match = re.findall("^If", zen_fragment, re.MULTILINE)
print(match)
