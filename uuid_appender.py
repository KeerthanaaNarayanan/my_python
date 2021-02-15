from aptest_files.common import *

test_keys = get_list(dict123)

for i in test_keys:
    print('\"' + i + '\": \"uuid\",')