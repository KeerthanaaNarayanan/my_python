import os

def add_to_clip_board(text):
    add = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(add)


suites_prod = {
    1: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_create1.py',
    2: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_create2.py',
    3: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit1.py',
    4: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit2.py',
    5: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit3.py',
    6: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit4.py',
    7: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit5.py',
    8: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/objects/service_group.py',
    9: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/policies/content_filter/content_filter_cfs1.py',
    10: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/policies/content_filter/content_filter_cfs2.py',
    11: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/policies/content_filter/content_filter_cfs3.py',
    12: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/policies/content_filter/content_filter_cfs4.py',
    13: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/policies/content_filter/content_filter_websense_main.py',
    14: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/policies/content_filter/content_filter_websense2.py',
    15: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/policies/content_filter/content_filter_websense3.py',
    16: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/policies/content_filter/content_filter_websense4.py',
    17: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/network/ip_helper_base.py',
    18: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/network/mac_ip_antispoof/ipv4_interface.py',
    19: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base_main.py',
    20: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base2.py',
    21: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base3.py',
    22: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base4.py',
    23: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base5.py',
    24: '/SWIFT4.0/TESTS/NSM/2.0/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base6.py',
}
suites_dev = {
    1: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_create1.py',
    2: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_create2.py',
    3: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit1.py',
    4: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit2.py',
    5: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit3.py',
    6: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit4.py',
    7: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_objects/service_object_valid_edit5.py',
    8: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/objects/service_group.py',
    9: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/policies/content_filter/content_filter_cfs1.py',
    10: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/policies/content_filter/content_filter_cfs2.py',
    11: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/policies/content_filter/content_filter_cfs3.py',
    12: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/policies/content_filter/content_filter_cfs4.py',
    13: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/policies/content_filter/content_filter_websense_main.py',
    14: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/policies/content_filter/content_filter_websense2.py',
    15: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/policies/content_filter/content_filter_websense3.py',
    16: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/policies/content_filter/content_filter_websense4.py',
    17: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/network/ip_helper_base.py',
    18: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/network/mac_ip_antispoof/ipv4_interface.py',
    19: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base_main.py',
    20: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base2.py',
    21: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base3.py',
    22: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base4.py',
    23: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base5.py',
    24: ' /DEV_TESTS/NSM/knarayanan/GMS/scripts/test_suites/api/users/user_sso_base/user_sso_base6.py',
}
vtb = {
    152: ' -qbshost VTB152',
    172: ' -qbshost VTB172',
}
dummy_file = ' -b /logs/downloads/dummy.txt'
user = ' -user knarayanan'
product = ' -product NSM'
env_qa = ' -var G_ENV=QA-AWS'
env_dev = ' -var G_ENV=DEV-AWS'
log_level = ' -var G_LOG_LEVEL=DEBUG2'
scmlabel = ' -scmlabel '
label_scm = {
    'no' : 'TRIALRUN nodatabase',
    'yes': 'REGISTRATION'
}
label = {
    1: 'service_object_valid_create1',
    2: 'service_object_valid_create2',
    3: 'service_object_valid_edit1',
    4: 'service_object_valid_edit2',
    5: 'service_object_valid_edit3',
    6: 'service_object_valid_edit4',
    7: 'service_object_valid_edit5',
    8: 'service_group',
    9: 'content_filer_cfs_base1',
    10: 'content_filer_cfs_base2',
    11: 'content_filer_cfs_base3',
    12: 'content_filer_cfs_base4',
    13: 'content_filter_websense_main',
    14: 'content_filter_websense2',
    15: 'content_filter_websense3',
    16: 'content_filter_websense4',
    17: 'ip_helper_base',
    18: 'ipv4_interface',
    19: 'user_sso_base_main',
    20: 'user_sso_base2',
    21: 'user_sso_base3',
    22: 'user_sso_base4',
    23: 'user_sso_base5',
    24: 'user_sso_base6',

}
rgname = ' -rgname '
name = {
    1: '[SonicOS]service_object_valid_create1',
    2: '[SonicOS]service_object_valid_create2',
    3: '[SonicOS]service_object_valid_edit1',
    4: '[SonicOS]service_object_valid_edit2',
    5: '[SonicOS]service_object_valid_edit3',
    6: '[SonicOS]service_object_valid_edit4',
    7: '[SonicOS]service_object_valid_edit5',
    8: '[SonicOS]service_group',
    9: '[SonicOS]content_filter_cfs1',
    10: '[SonicOS]content_filter_cfs2',
    11: '[SonicOS]content_filter_cfs3',
    12: '[SonicOS]content_filter_cfs4',
    13: '[SonicOS]content_filter_websense_main',
    14: '[SonicOS]content_filter_websense2',
    15: '[SonicOS]content_filter_websense3',
    16: '[SonicOS]content_filter_websense4',
    17: '[SonicOS]ip_helper_base',
    18: '[SonicOS]ipv4_interface',
    19: '[SonicOS]user_sso_base_main',
    20: '[SonicOS]user_sso_base2',
    21: '[SonicOS]user_sso_base3',
    22: '[SonicOS]user_sso_base4',
    23: '[SonicOS]user_sso_base5',
    24: '[SonicOS]user_sso_base6',
}
nodb_trail = ' -nodatabase -trailrun'
trail_only = ' -trailrun'
