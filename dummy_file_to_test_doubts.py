# import os
# import subprocess
# # create a pipe to a child process
# data, temp = os.pipe()
#
# # write to STDIN as a byte object(convert string
# # to bytes with encoding utf8)
# os.write(temp, bytes("5 10\n", "utf-8"));
# os.close(temp)
#
# # store output of the program as a byte string in s
# s = subprocess.check_output("g++ HelloWorld.cpp -o out2;./out2", stdin=data, shell=True)
#
# # decode s to a normal string
# print(s.decode("utf-8"))

import paramiko
import time
command = 'rtqtest.pl -cts /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_objects/service_object_invalid_create.py -b /logs/downloads/dummy.txt -user knarayanan -product NSM -var G_ENV=QA-AWS -var G_LOG_LEVEL=DEBUG2 -scmlabel TRIALRUN nodatabase -qbshost VTB152 -rgname [SonicOS]service_object_invalid_create -nodatabase -trailrun'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.5.80.159", username="root", password="password")

while True:
    print("Running")
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read())
    print(stderr.read())
    print("Waiting")
    time.sleep(5)