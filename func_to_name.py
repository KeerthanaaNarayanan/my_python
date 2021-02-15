subTest_Edit_Type = [
    'create_serviceobject_valid_type_custom',
    'create_serviceobject_valid_type_icmp',
    'create_serviceobject_valid_type_igmp',
    'create_serviceobject_valid_type_with_ports',
    'create_serviceobject_valid_type_with_enable',
    'create_serviceobject_valid_type_icmpv6',
    'create_serviceobject_valid_type_ospf',
    'create_serviceobject_valid_type_pim',
    'edit_serviceobject_valid_to_other_types',
    'edit_serviceobject_valid_port_custom',
    'edit_serviceobject_valid_subtype_icmp',
    'edit_serviceobject_valid_subtype_igmp',
    'edit_serviceobject_valid_subtype_with_ports',
    'edit_serviceobject_valid_subtype_icmpv6',
    'edit_serviceobject_valid_subtype_ospf',
    'edit_serviceobject_valid_subtype_pim'
]

for j in subTest_Edit_Type:
    print('\"' + j + '\": \"uuid\",')
