# cli_utils

A beginner-friendly Python package with CLI utility functions.

## Usage

```python
from cli_utils import print_separator

print_separator()
# Output: **********************************


from cli_utils import print_char_separator

print_char_separator(x)
# Output: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


from cli_utils import print_custom_separator

print_custom_separator("x", 60)
# Output: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

from cli_utils import print_labeled_separator

def print_labeled_separator("STAR", char="*", width=30):
#Output: ***************STAR***************

from cli_utils import print_box

print_box("Hello, World")
#Output: 
# **************
# * Hello, World *
# **************