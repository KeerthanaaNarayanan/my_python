testCaseName = "modify_intrusion_prevention_category_valid_prevention"
file_name = "intrusion_prevention_categories_api"
categories = [
    # 'BACKDOOR', 'SUSPICIOUS-TRAFFIC', 'DNS', 'FTP', 'ICMP',
    # 'IMAP','INFO','MISC','NETBIOS','POP','RPC','SMTP','VIRUS','VoIP-ATTACKS','WEB-ATTACKS','WEB-CLIENT','WEB-PHP',
    # 'SQL-INJECTION', 'ACTIVEX','BAD-FILES','LDAP','XSS','DB-ATTACKS','SCADA-ATTACKS','JAVA','OS-ATTACKS',
    # 'WEB-TLS',
    'IoT-ATTACKS'
]
prevention = [
    'global',
    # 'enable',
    # 'disable'
]
# id = {'BACKDOOR': 2, 'SUSPICIOUS-TRAFFIC': 3, 'DNS': 5, 'FTP': 9, 'ICMP': 10, 'IoT-ATTACKS': 94}
subTestName = []
for category in categories:
    for prevent in prevention:
        subTestName.append(testCaseName + '_' + str(category.lower()) + '_' + str(prevent))

print(subTestName)
