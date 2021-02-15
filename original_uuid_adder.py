from aptest_files.common import *

uuid = [
    "55cb29c6-f846-45a5-bdda-a59c1daa0390",
    "8f5be731-74ae-45fb-95b6-ba307570b1de",
    "052c75e0-20cc-4a08-bd4c-73347b0f11af",
    "0d1fc262-c393-40a9-85bd-bb32cc66f033",
    "92173216-a982-4a4e-99b1-4dbf6c247f02",
    "48d9d12c-f805-4e91-b885-59c032d21bea",
    "bc3f8ea9-e6d6-4f41-b5e8-8e7b5b5609c7",
    "4abc08c8-d93c-478c-857b-c8d641438dbf",
    "0fd0210e-311b-4dbc-a7f7-ca06eeefce39",
    "466d29df-1916-4a87-b9ca-689448f3c7cd",
    "d95c8da3-09b7-434e-9211-4e45b3d61ecc",
    "24d8f4d3-cc79-4a90-b843-7615345d24cf",
    "3128b82b-639e-433a-adbe-68f965a84180",
]

test_keys = get_list(dict123)

for i, j in zip(test_keys, uuid):
    print('\"' + i + '\": \"' + j + '\",')
