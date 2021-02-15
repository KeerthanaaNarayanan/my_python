from aptest_files.common import *

bug_id = "MAR-17127"

test_keys = get_list(dict123)

for i in test_keys:
    print('\"' + i + '\": \"' + bug_id + '\",')