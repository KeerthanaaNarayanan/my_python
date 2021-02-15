prod_temp = '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/'
dev_temp = '/DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/'
suite_name_individual = [
    # 3. give here the suite path
    'objects/service_objects/service_object_valid_create1.py',
    'objects/service_objects/service_object_valid_create2.py',
    'objects/service_objects/service_object_valid_edit1.py',
    'objects/service_objects/service_object_valid_edit2.py',
    'objects/service_objects/service_object_valid_edit3.py',
    'objects/service_objects/service_object_valid_edit4.py',
    'objects/service_objects/service_object_valid_edit5.py',
    'objects/service_objects/service_object_valid_edit6.py',
    'objects/service_objects/service_object_valid_edit7.py',
    'objects/service_objects/service_object_valid_edit8.py',
    'objects/service_group_valid_create.py',
    'objects/service_group_valid_edit.py',
    'objects/service_group_full_reg.py',
    'policies/content_filter/content_filter_cfs_main.py',
    'policies/content_filter/content_filter_cfs_nsa.py',
    'policies/content_filter/content_filter_cfs_nsv.py',
    'policies/content_filter/content_filter_websense_main.py',
    'policies/content_filter/content_filter_websense_nsa.py',
    'policies/content_filter/content_filter_websense_nsv.py',
    'network/ip_helper_base.py',
    'network/mac_ip_antispoof/mac_ip_antispoof_ipv4_interface.py',
    'network/mac_ip_antispoof/mac_ip_antispoof_ipv6_interface.py',
    'users/user_sso_base/user_sso_base_main.py',
    'users/user_sso_base/user_sso_base_nsa1.py',
    'users/user_sso_base/user_sso_base_nsa2.py',
    'users/user_sso_base/user_sso_base_nsv1.py',
    'users/user_sso_base/user_sso_base_nsv2.py',
    'policies/content_filter/content_filter_cfs_policy_main.py',
    'network/mac_ip_antispoof/mac_ip_antispoof_ipv4_entries.py',
    'objects/service_objects/service_object_invalid_create.py',
    'objects/service_objects/service_object_invalid_edit.py',
    'objects/service_objects/service_object_regression.py',
    'users/user_tacacs_base_api_2.py',
    'network/mac_ip_antispoof/invalid_mac_ip_antispoof_ipv4_interface.py',
    'network/mac_ip_antispoof/invalid_mac_ip_antispoof_ipv6_interface.py',
    'network/vpn_base/vpn_base_api.py',
    'network/vpn_base/vpn_base_invalid_modify_1.py',
    'network/vpn_base/vpn_base_invalid_modify_2.py',
    'network/vpn_base/vpn_base_invalid_modify_3.py',
    'network/vpn_base/vpn_base_full_regression_1.py',
    'network/vpn_base/vpn_base_full_regression_2.py',
    'network/sd_wan/sd_wan_path_selection_profile_full_reg.py',
    'network/sd_wan/sd_wan_groups_full_reg.py',
    'network/sd_wan/sd_wan_path_selection_profile_edit.py',
    'policies/intrusion_prevention_policy.py',
    'policies/intrusion_prevention_base_api.py',
    'policies/intrusion_prevention_categories_1.py',
    'policies/intrusion_prevention_categories_2.py',
    'policies/intrusion_prevention_categories_3.py',
    'policies/intrusion_prevention_categories_4.py',
    'policies/security_services_base.py',
    'policies/security_policies_max_count.py'
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
for n in json_data.items():
    print(n)


def take_a_suite(number):
    suite_path = suites.get(number, "")
    prod_suite_path = prod_temp + suite_path
    dev_suite_path = dev_temp + suite_path
    print('prod_path:')
    print(prod_suite_path)
    print('dev_path:')
    print(dev_suite_path)


num = int(input("Enter the suite number you need : "))
take_a_suite(num)

print('//depot/SQA/SWIFT4.0/COMMON/data/topo/NSM/nsm.json')
