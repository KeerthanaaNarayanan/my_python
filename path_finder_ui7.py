import os

prod_temp = '/SWIFT4.0/TESTS/SonicOSUI7/7.0.0/SonicOS7/scripts/test_suites/ui/'
dev_temp = '/DEV_TESTS/SonicOS7/knarayanan/SonicOS7/scripts/test_suites/ui/'
suite_name_individual = [
    # 3. give here the suite path
    'objects/content_filter/content_filter_action_objects_valid_create.py',
    'objects/content_filter/content_filter_action_objects_valid_edit.py',
    'policies/content_filter/content_filter_policy_create.py',
    'policies/content_filter/content_filter_policy_create2.py',
    'policies/content_filter/content_filter_policy_edit.py',
    'policies/gateway_antivirus/gateway_antivirus_base.py',
    'policies/gateway_antivirus/gateway_antivirus_base_config_view.py',
    'policies/gateway_antivirus/gateway_antivirus_base_protocol_view_boolean.py',
    'policies/gateway_antivirus/gateway_antivirus_base_protocol_view_exclusion_object.py',
    'objects/content_filter/content_filter_profile_object_valid_create.py',
    'objects/content_filter/content_filter_profile_object_valid_create_2.py',
    'objects/content_filter/content_filter_profile_object_valid_create_category1.py',
    'objects/content_filter/content_filter_profile_object_valid_create_category2.py',
    'objects/content_filter/content_filter_profile_object_valid_create_category3.py',
    'objects/content_filter/content_filter_profile_object_valid_edit_1.py',
    'objects/content_filter/content_filter_profile_object_valid_edit_2.py',
    'objects/content_filter/content_filter_profile_object_valid_edit_category_1.py',
    'objects/content_filter/content_filter_profile_object_valid_edit_category_2.py',
    'objects/content_filter/content_filter_profile_object_valid_edit_category_3.py',
    'policies/content_filter/content_filter_policy_edit_schedule_and_users.py',
    'policies/content_filter/content_filter_policy_edit_source.py',
    'network/ip_helper_base.py',
    'device/app_flow/appflow_base.py',
    'device/app_flow/appflow_external_collector.py',
    'policies/gateway_antivirus/gateway_antivirus_exclusion_list_base.py',
    'network/ip_helper_policies.py',
    'policies/dpi_ssl_client/dpi_ssl_client_base.py',
    'policies/dpi_ssl_client/dpi_ssl_client_cfs_category.py',
    'policies/dpi_ssl_client/dpi_ssl_client_cfs_category2.py',
    'policies/dpi_ssl_client/dpi_ssl_server_base.py',
]
suites = {}
i = 1
for n in suite_name_individual:
    suites[i] = n
    i += 1
json_data = {}
for suite in suites:
    suite_path = suites.get(suite, "")
    suite_name = suite_path.split("/")[-1]
    file_name = suite_name.split(".")[0]
    json_data[suite] = file_name

# print(json_data)
for n in json_data.items():
    print(n)


def take_a_suite(number):
    suite_path = suites.get(number, "")
    prod_suite_path = prod_temp + suite_path
    dev_suite_path = dev_temp + suite_path
    print('prod_path:')
    print(prod_suite_path)
    print()
    print()
    print('dev_path:')
    print(dev_suite_path)
    add = 'echo | set /p nul=' + dev_suite_path.strip() + '| clip'
    os.system(add)


num = int(input("Enter the suite number you need : "))
take_a_suite(num)

print()
print()
print('//depot/SQA/SWIFT4.0/COMMON/data/topo/SonicOS/UI7/ui7_windows.json')