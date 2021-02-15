# importing webbrowser python module
import webbrowser
#urls = ["summary_images", "summary_images_jsm", "summary_simple", "summary_simple_jsm", "whatisthis_acceptAutoAllowedLists", "whatisthis_batv", "whatisthis_cipherStrength", "whatisthis_deletealladdressbooks", "whatisthis_dkimKeys", "whatisthis_dmarc", "whatisthis_dmarc_rua", "whatisthis_downloadLogFiles", "whatisthis_easy_config", "whatisthis_easy_config_ldap_server_name", "whatisthis_realhost", "whatisthis_test_connectivity", "whatisthis_emailArchive", "whatisthis_emailArchiveAging", "whatisthis_greylisting", "whatisthis_host_config", "whatisthis_ipReputation", "whatisthis_likelyvirus", "whatisthis_per_domain_dha_protection", "whatisthis_reinitialize", "whatisthis_resetlicensemanager", "whatisthis_safemode", "whatisthis_skipSpamAnalysisInternal", "whatisthis_smtpAuth", "whatisthis_spf", "whatisthis_startTLs", "whatisthis_strictMailFromChecking", "whatisthis_submitMessageFeatures", "whatisthis_submitSpam", "whatisthis_submitUnjunkThumbprints", "whatisthis_submitURLs", "whatisthis_tarpitting", "whatisthis_TEMPLATE", "whatisthis_uploadBranding", "whatisthis_uploadPatch", "whatisthis_userViewURL", "whatisthis_zombie"]
#i = 1
#for i in range(44):
	#Assigning URL to be opened
#	for_this = urls[i]
	# strURL = "https://10.5.58.8/static_page?url=/static_htms/it/{}.htm".format(for_this)
	# Open url in default browser
	
#	webbrowser.open(strURL, new=2)

i = 1
for i in range(1, 45):
	strURL = "https://qatest.eng.sonicwall.com/browse/viewTestCase.mpl?suite=EmailSecurity&tc=ES_General.dir/RESTful-API.dir/Certificates.dir/{}.bts&dir=ES_General.dir/RESTful-API.dir/Certificates.dir".format(i)
	webbrowser.open(strURL, new=2)


#class TestCreatePEMTrustedCertificate(Test):
    # uuid = "e3312b04-f6fb-419f-9c08-ab4e3de1cb4c"
	#
    # def runTest(self):
    #     api_obj, authorization_code = login()
    #     cert_type = 'pem'
    #     cert_name = 'TestCreatePEMTrustedCertificate'
    #     cert_pass_phrase = 'password'
    #     cert_key_pass_phrase = 'password'
    #     is_cert_file = True
    #     is_pvt_key_file = True
    #     # Deleting the certificate which is already in the same certificate name...
    #     api_obj.delete_certificates(authorization_code, cert_name)
    #     # creating a self signed certificate...
    #     try:
    #         status_code, response_json = api_obj.post_certificates_upload(authorization_code, cert_type, cert_name,
    #                                                                       cert_pass_phrase, cert_key_pass_phrase,
    #                                                                       is_cert_file, is_pvt_key_file)
    #         Assertion.assert_equal(status_code, 200, "ERR: Unable to add pem certificate http error")
    #         Assertion.assert_equal(response_json['msgType'], "SUCCESS", "ERR: Could not add trusted certificate")
    #     # Fetching and Deleting the created certificate...
    #     finally:
    #         if response_json['msgType'] == 'SUCCESS':
    #             Assertion.assert_equal(
    #                 fetch_certificates(api_obj, authorization_code, cert_name), True,
    #                 "Err: Fetching the certificates is successful")
    #             delete_after_posting(api_obj, authorization_code, cert_name)

# def post_upload(authorization_code, cert_type, cert_name, cert_passPhrase, cert_keyPassPhrase,
#                              isCertFile=True, isPvtKeyFile=True, key_file_path=None):
#     logger("***************Invoking method to upload trusted certificate***************")
#     logger("URL to upload certificate is " + certificates_upload_url)
#     # In case of certificate validity expires, no need to change file name in code, instead change the .key, .pem,
#     # .p7b and .pfx files in the inputs/certificates folder
#     if cert_type == 'pem':
#         cert_file = glob.glob(os.path.join(root_dir, 'inputs', 'certificates', '*.pem'))
#         cert_file_path = cert_file[-1]
#         key_file = glob.glob(os.path.join(root_dir, 'inputs', 'certificates', '*.key'))
#         key_file_path = key_file[-1]
#     elif cert_type == 'p7b':
#         cert_file = glob.glob(os.path.join(root_dir, 'inputs', 'certificates', '*.p7b'))
#         cert_file_path = cert_file[-1]
#         key_file = glob.glob(os.path.join(root_dir, 'inputs', 'certificates', '*.key'))
#         key_file_path = key_file[-1]
#     else:
#         cert_file = glob.glob(os.path.join(root_dir, 'inputs', 'certificates', '*.pfx'))
#         cert_file_path = cert_file[-1]
#     cert_file_name = 'temp'
#     key_file_name = 'temp'
#     if cert_type == 'pem' or cert_type == 'p7b':
#         cert_file_name = cert_file_path.split("/")[-1]
#         key_file_name = key_file_path.split("/")[-1]
#     if cert_type == 'pfx':
#         cert_file_name = cert_file_path.split("/")[-1]
#     upload_request_file = {"certificatename": cert_name, "certificatepassphrase": cert_passPhrase,
#                            "keypassphrase": cert_keyPassPhrase}
#     if isCertFile and isPvtKeyFile:
#         trusted_files = {'certfile': (cert_file_name, open(str(cert_file_path), 'rb')),
#                          'pvtkeyfile': (key_file_name, open(str(key_file_path), 'rb')),
#                          'uploadRequest': (str(upload_request_file))
#                          }
#     elif isCertFile and (isPvtKeyFile is False):
#         trusted_files = {'certfile': (cert_file_name, open(cert_file_path, 'rb')),
#                          'uploadRequest': (str(upload_request_file))
#                          }
#     elif isPvtKeyFile and (isCertFile is False):
#         trusted_files = {'pvtkeyfile': (key_file_name, open(str(key_file_path), 'rb')),
#                          'uploadRequest': (str(upload_request_file))
#                          }
#
#     else:
#         trusted_files = {'uploadRequest': (str(upload_request_file))
#                          }
#
#     new_session = requests.Session()
#     r = requests.Request('POST', certificates_upload_url, files=trusted_files)
#     new_request = new_session.prepare_request(r)
#     new_request.headers['Authorization'] = authorization_code
#     response = new_session.send(new_request)
#     new_session.close()
#     status_code = response.status_code
#     response_json = response.json()
#     logger(response_json)
#     return status_code, response_json

# # login to Gateway
#     def login_to_gateway(self, user_cred=None):
#         response = ""
#         if user_cred:
#             response = self.post(login_to_gateway, user_cred)
#         else:
#             user_cred = {
#                 "username": "admin",
#                 "password": "password"
#             }
#             headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
#             response = self.post(login_to_gateway, user_cred, headers=headers)
#         authorization_code = response.json()["data"]["token"]
#         return authorization_code

# generic post method
#     def post(self, request_url, json_obj=None, params=None, files=None, headers=None):
#         if headers is None:
#             headers = default_headers
#
#         if files is None:
#             resp = requests.post(request_url, data=json.dumps(json_obj), params=params, files=files,
#                                  headers=headers, verify=False)
#         else:
#             resp = requests.post(request_url, params=params, files=files,
#                                  verify=False)
#         return resp