def append_attrib_key(attrib_path, attrib_key):
    # print('Into append attrib key')
    if attrib_path is not "":
        attrib_path = attrib_path + "." + attrib_key
    else:
        attrib_path = attrib_key
    return attrib_path


def append_data_to_json(current_json, complete_json, attrib_path, attrib_key):
    # print('Into append data to json')
    attrib_path = append_attrib_key(attrib_path, attrib_key)
    # To be executed when it is a list to which data needs to be appended
    if type(current_json) is list:
        # To be executed when it is an empty list and multiple elements to be appended
        if type(complete_json[attrib_path]) is list and len(current_json) == 0:
            for newElement in complete_json[attrib_path]:
                temp_dict = ''
                temp_dict[attrib_key] = newElement
                current_json.append(temp_dict)
        # To be executed when it is an existing list and multiple elements to be appended
        elif type(complete_json[attrib_path]) is list:
            for (newElement, currentElement) in zip(complete_json[attrib_path], current_json):
                currentElement[attrib_key] = newElement
        # To be executed when it is a list and an element to be appended
        else:
            temp_dict = {}
            temp_dict[attrib_key] = complete_json[attrib_path]
            current_json.append(temp_dict)
    # Fallback to a dictionary!
    else:
        current_json[attrib_key] = complete_json[attrib_path]
    return current_json

complete_json = {
    'service_objects': [],
    'service_objects.tcp': {},
    'service_objects.udp': {},
    'service_objects.name': 'CreateServiceObjectPim',
    'service_objects.service_object_type': 'service_object_pim',
    'service_objects.pim': 'None'
}
print("Creating json")
created_json = {}
for attribute in complete_json:
    # Split the attributes to fetch the path
    attributes = attribute.split(".")
    print('printing attributes')
    print(attributes)
    current_json = created_json
    print("printing current_json")
    print(current_json)
    attrib_path = ""
    for attrib_key in attributes:
        # Check if the key is the present in the next level of json
        if attrib_key not in current_json:
            # Append data to the JSON
            current_json = append_data_to_json(current_json, complete_json, attrib_path, attrib_key)
            break
        else:
            attrib_path = append_attrib_key(attrib_path, attrib_key)
            # To be executed when it is a list and the last traversal level in the path
            if type(current_json[attrib_key]) is list and attrib_key == attributes[-2]:
                current_json = current_json[attrib_key]
            # To be executed when it is a list for next traversal
            elif type(current_json[attrib_key]) is list and len(current_json[attrib_key]) > 0:
                current_json = current_json[attrib_key][0]
            # Fallback to a dictionary!
            else:
                current_json = current_json[attrib_key]

# logger.debug2("Created JSON :" + str(current_json))
