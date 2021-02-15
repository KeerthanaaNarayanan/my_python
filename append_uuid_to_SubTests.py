testCaseName = "modify_intrusion_prevention_policy_valid_log_redundancy_filter_value"
file_name = 'intrusion_prevention_policy_api'
subTest_Type = [
    0, 1, 14, 100, 9999, 999999
]
subTestName = []
for value in subTest_Type:
    subTestName.append(testCaseName + '_' + str(value))



print(testCaseName)
for j in subTestName:
    print(j)
