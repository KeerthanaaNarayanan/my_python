# import json
import os
from subprocess import Popen

vtb = {
    152: ' -qbshost VTB152',  # 1. change the key and value
    172: ' -qbshost VTB172',
}
dummy_file = ' -b /logs/downloads/dummy.txt'
user = ' -user knarayanan'  # 2. change the user name to your name
product = ' -product NSM'
env_qa = ' -var G_ENV=QA-AWS'
env_dev = ' -var G_ENV=DEV-AWS'
log_level = ' -var G_LOG_LEVEL=DEBUG2'
scmlabel = ' -scmlabel '
label_scm = {
    'no': 'TRIALRUN nodatabase',
    'yes': 'REGISTRATION'
}
rgname = ' -rgname '
nodb_trail = ' -nodatabase -trailrun'
trail_only = ' -trailrun'
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
    'policies/content_filter/content_filter_cfs_main.py',
    'policies/content_filter/content_filter_cfs_nsa.py',
    'policies/content_filter/content_filter_cfs_nsv.py',
    'policies/content_filter/content_filter_websense_main.py',
    'policies/content_filter/content_filter_websense_nsa.py',
    'policies/content_filter/content_filter_websense_nsv.py',
    'network/ip_helper_base.py',
    'network/mac_ip_antispoof/ipv4_interface.py',
    'users/user_sso_base/user_sso_base_main.py',
    'users/user_sso_base/user_sso_base_nsa1.py',
    'users/user_sso_base/user_sso_base_nsa2.py',
    'users/user_sso_base/user_sso_base_nsv1.py',
    'users/user_sso_base/user_sso_base_nsv2.py',
    'policies/content_filter/content_filter_cfs_policy_main.py',
    'network/mac_ip_antispoof/mac_ip_antispoof_ipv4_entries.py',
    'objects/service_objects/service_object_invalid_create.py',
]

# def suite_list_maker():
suites = {}
i = 1
for n in suite_name_individual:
    suites[i] = n
    i += 1
    # return suites


def take_a_suite(number):
    suite_path = suites.get(number, "")
    suite_name = suite_path.split("/")[-1]
    file_name = suite_name.split(".")[0]
    name = '[SonicOS]' + str(file_name)
    prod_suite_path = prod_temp + suite_path
    dev_suite_path = dev_temp + suite_path
    return file_name, name, prod_suite_path, dev_suite_path


def add_to_clip_board(text):
    add = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(add)


def label_maker():
    # suites = suite_list_maker()
    json_data = {}
    for suite in suites:
        suite_path = suites.get(suite, "")
        suite_name = suite_path.split("/")[-1]
        file_name = suite_name.split(".")[0]
        json_data[suite] = file_name
    for n in json_data.items():
        print(n)


def vtb_putty(host):  # 4. change the vtb and controller ip
    if host == 152:  # change vtb client - 10.5.80.209 - keerthanaa
        Popen("powershell putty.exe root@10.5.80.159 -pw password")  # change the controller
    if host == 172:  # client - 10.5.80.213 shivank
        Popen("powershell putty.exe root@10.5.80.163 -pw password")
    if host == 158:  # client - 10.5.80.210 vishal
        Popen("powershell putty.exe root@10.5.80.160 -pw password")


def main():
    label_maker()
    num = int(input("Enter the suite number you need to run : "))
    file_name, name, prod_suite_path, dev_suite_path = take_a_suite(num)
    swift = str(input('swift or devtest? swift/devtest: '))
    env = str(input('which env? qa/dev: '))
    host = int(input('which vtb? eg:152,158,172 : '))
    db = str(input('need db? give yes for registration and no for trail run- yes/no : '))
    command = ''
    if swift == 'swift':
        if db == 'yes':
            if env == 'dev':
                command = 'rtqtest.pl -cts ' + str(prod_suite_path) + str(dummy_file) + str(user) + str(
                    product) + str(
                    env_dev) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(
                    vtb.get(host, "")) + str(
                    rgname) + str(name) + str(trail_only)
            if env == 'qa':
                command = 'rtqtest.pl -cts ' + str(prod_suite_path) + str(dummy_file) + str(user) + str(
                    product) + str(
                    env_qa) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(
                    vtb.get(host, "")) + str(
                    rgname) + str(name) + str(trail_only)
        if db == 'no':
            if env == 'dev':
                command = 'rtqtest.pl -cts ' + str(prod_suite_path) + str(dummy_file) + str(user) + str(
                    product) + str(
                    env_dev) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(
                    vtb.get(host, "")) + str(
                    rgname) + str(name) + str(nodb_trail)
            if env == 'qa':
                command = 'rtqtest.pl -cts ' + str(prod_suite_path) + str(dummy_file) + str(user) + str(
                    product) + str(
                    env_qa) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(
                    vtb.get(host, "")) + str(
                    rgname) + str(name) + str(nodb_trail)
    if swift == 'devtest':
        if db == 'yes':
            if env == 'dev':
                command = 'rtqtest.pl -cts ' + str(dev_suite_path) + str(dummy_file) + str(user) + str(
                    product) + str(
                    env_dev) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(
                    vtb.get(host, "")) + str(
                    rgname) + str(name) + str(trail_only)
            if env == 'qa':
                command = 'rtqtest.pl -cts ' + str(dev_suite_path) + str(dummy_file) + str(user) + str(product) + str(
                    env_qa) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(
                    vtb.get(host, "")) + str(rgname) + str(name) + str(trail_only)
        if db == 'no':
            if env == 'dev':
                command = 'rtqtest.pl -cts ' + str(dev_suite_path) + str(dummy_file) + str(user) + str(
                    product) + str(
                    env_dev) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(
                    vtb.get(host, "")) + str(
                    rgname) + str(name) + str(nodb_trail)
            if env == 'qa':
                command = 'rtqtest.pl -cts ' + str(dev_suite_path) + str(dummy_file) + str(user) + str(
                    product) + str(
                    env_qa) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(
                    vtb.get(host, "")) + str(
                    rgname) + str(name) + str(nodb_trail)
    add_to_clip_board(command)
    vtb_putty(host)


main()
