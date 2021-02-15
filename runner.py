from trail_run.common import *
from subprocess import Popen

for n in label.items():
    print(n)
num = int(input("Enter the suite number you need to run : "))
data = label.get(num, "")
suite = str(input('production or development prod/dev? '))
env = str(input('which env qa/dev? '))
host = int(input('which vtb? eg:152 : '))
db = str(input('need db? yes/no : '))
command = ''
if suite == 'prod':
    if db == 'yes':
        if env == 'dev':
            command = 'rtqtest.pl -cts ' + str(suites_prod.get(num, "")) + str(dummy_file) + str(user) + str(product) + str(
                env_dev) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, "")) + str(
                rgname) + str(name.get(num, "")) + str(trail_only)
        if env == 'qa':
            command = 'rtqtest.pl -cts ' + str(suites_prod.get(num, "")) + str(dummy_file) + str(user) + str(product) + str(
                env_qa) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, "")) + str(
                rgname) + str(name.get(num, "")) + str(trail_only)
    if db == 'no':
        if env == 'dev':
            command = 'rtqtest.pl -cts ' + str(suites_prod.get(num, "")) + str(dummy_file) + str(user) + str(product) + str(
                env_dev) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, "")) + str(
                rgname) + str(name.get(num, "")) + str(nodb_trail)
        if env == 'qa':
            command = 'rtqtest.pl -cts ' + str(suites_prod.get(num, "")) + str(dummy_file) + str(user) + str(product) + str(
                env_qa) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, "")) + str(
                rgname) + str(name.get(num, "")) + str(nodb_trail)
if suite == 'dev':
    if db == 'yes':
        if env == 'dev':
            command = 'rtqtest.pl -cts ' + str(suites_dev.get(num, "")) + str(dummy_file) + str(user) + str(product) + str(
                env_dev) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, "")) + str(
                rgname) + str(name.get(num, "")) + str(trail_only)
        if env == 'qa':
            command = 'rtqtest.pl -cts ' + str(suites_dev.get(num, "")) + str(dummy_file) + str(user) + str(product) + str(
                env_qa) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, "")) + str(
                rgname) + str(name.get(num, "")) + str(trail_only)
    if db == 'no':
        if env == 'dev':
            command = 'rtqtest.pl -cts ' + str(suites_dev.get(num, "")) + str(dummy_file) + str(user) + str(product) + str(
                env_dev) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, "")) + str(
                rgname) + str(name.get(num, "")) + str(nodb_trail)
        if env == 'qa':
            command = 'rtqtest.pl -cts ' + str(suites_dev.get(num, "")) + str(dummy_file) + str(user) + str(product) + str(
                env_qa) + str(log_level) + str(scmlabel) + str(label_scm.get(db, "")) + str(vtb.get(host, "")) + str(
                rgname) + str(name.get(num, "")) + str(nodb_trail)
add_to_clip_board(command)

if host == 152:
    Popen("powershell putty.exe root@10.5.80.159 -pw password")
if host == 172:
    Popen("powershell putty.exe root@10.5.80.163 -pw password")
