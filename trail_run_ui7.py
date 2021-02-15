# import json
import os
import paramiko
import time
from subprocess import Popen

vtb = {
    62: ' -qbshost VTB62',  # 1. change the key and value
}
dummy_file = ' -b /logs/downloads/dummy.txt'
user = ' -user knarayanan'  # 2. change the user name to your name
product = ' -product TZ'
log_level = ' -var G_LOG_LEVEL=DEBUG2'
scmlabel = ' -scmlabel '
label_scm = {
    'no': 'TRIALRUN nodatabase',
    'yes': 'REGISTRATION'
}
rgname = ' -rgname '
nodb_trail = ' -nodatabase -trailrun'
trail_only = ' -trailrun'
prod_temp = '/SWIFT4.0/TESTS/SonicOSUI7/7.0.0/SonicOS7/scripts/test_suites/'
dev_temp = '/DEV_TESTS/SonicOS7/knarayanan/SonicOS7/scripts/test_suites/'
suite_name_individual = [
    # 3. give here the suite path
    'objects/content_filter_action_objects_valid_create.py',
    'objects/content_filter_action_objects_valid_edit.py',
    'policies/content_filter/content_filter_policy_create.py',
    'policies/content_filter/content_filter_policy_create2.py',
    'policies/content_filter/content_filter_policy_edit.py',
    'policies/gateway_antivirus/gateway_antivirus_base.py',
    'policies/gateway_antivirus/gateway_antivirus_config_view.py',
    'policies/gateway_antivirus/gateway_antivirus_protocol_view_boolean.py',
    'policies/gateway_antivirus/gateway_antivirus_protocol_view_exclusion_object.py',
    'policies/content_filter/content_filter_profile_create.py',
    'policies/content_filter/content_filter_profile_edit.py',
    'network/ip_helper_base.py',
    'device/app_flow/appflow_base.py'
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
    prod_suite_path = prod_temp + suite_path
    dev_suite_path = dev_temp + suite_path
    return file_name, prod_suite_path, dev_suite_path


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

def putty_command(host, command, times):
    if host == 62:  # 4 change vtb client - 10.5.80.232 - keerthanaa
        vtb = "10.5.80.182"
        # 10.5.2.146:3018
    for i in range(times):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(vtb, username="root", password="password")
        print("Running")
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read())
        print(stderr.read())
        print("Waiting")
        time.sleep(5)

def main():
    label_maker()
    count = int(input("Enter the number of suites you need to run : "))
    times = int(input("how many times you need to run each suite? : "))
    swift = str(input('swift or devtest? swift/devtest: '))
    host = int(input('which vtb? eg:62, 99 : '))
    db = str(input('need db? give yes for registration and no for trail run- yes/no : '))
    command = ''
    for i in range(count):
        num = int(input("Enter the suite number you need to run : "))
        file_name, prod_suite_path, dev_suite_path = take_a_suite(num)
        half_command = str(dummy_file) + str(user) + str(product)+ str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, ""))
        if swift == 'swift':
            command = 'rtqtest.pl -cts ' + str(prod_suite_path) + str(half_command)
        if swift == 'devtest':
            command = 'rtqtest.pl -cts ' + str(dev_suite_path) + str(half_command)
        print(command)
        putty_command(host, command, times)


main()
