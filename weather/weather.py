import xmltodict
import json
import sys

input_file_name = ''


def load_xml_file():
    global input_file_name
    input_file_name = sys.argv[1]
    file_location = './'+input_file_name
    f = open(file_location)
    return f


def xml_to_dict(file):
    xml_dict = xmltodict.parse(file.read())
    xml_dict = xml_dict['current']
    return xml_dict


def xml_to_json_with_beautifier(xml_dict, indent):
    string_of_json = json.dumps(xml_dict, indent=indent)
    list_of_json = string_of_json.split('"')
    for i in range(len(list_of_json)):
        if list_of_json[i][0] == '@':
            list_of_json[i] = list_of_json[i][1:]
    return list_of_json


def json_list_to_string(json_list):
    ans_string = ''

    for i in json_list:
        ans_string = ans_string+i+'"'
    ans_string = ans_string[:len(ans_string)-1]
    return ans_string


def write_string_to_file(json_string):
    if  len(sys.argv) <3 :
        file_name = input_file_name[:-3]+'json'
    else:
        file_name = sys.argv[2]
    file_location = './'+file_name
    f = open(file_location, mode="w")
    print(json_string, file=f)


if __name__ == "__main__":
    xml_file = load_xml_file()
    xml_dict = xml_to_dict(xml_file)
    json_list = xml_to_json_with_beautifier(xml_dict, 4)
    json_string = json_list_to_string(json_list)
    write_string_to_file(json_string)
