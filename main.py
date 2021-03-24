import os
import sys
import xml.etree.ElementTree as ET
from shutil import copyfile


def copy_file(file):
    """Функция копирования файла из source в destination"""
    file_name = file.get('file_name')
    file_src = os.path.join(file.get('source_path'), file_name)
    file_dst = os.path.join(file.get('destination_path'), file_name)
    if not os.path.isfile(file_src):
        return print(f'Source {file_src} file not found')

    if not os.path.isdir(os.path.dirname(file_dst)):
        print(f'Destination {file_dst} file not found')
        os.makedirs(os.path.dirname(file_dst))
    try:
        if os.path.isfile(file_dst):
            print(f'File: {file_dst} replacement!')
        copyfile(file_src, file_dst)
        print(f'File: {file_name} copy success')

    except Exception as error:
        print(f'Error copy: {error}')


def parser(path_xml):
    """Функция парсинга xml файла"""
    if os.path.isfile(path_xml):
        data = []
        tree = ET.parse(path_xml)
        for element in tree.iter('file'):
            if element.attrib.get('source_path') and element.attrib.get('destination_path') and element.attrib.get('file_name'):
                print(f'Find: {element.attrib}')
                copy_file(element.attrib)
                data.append(element.attrib)
    else:
        print(f'File {path_xml} not found')


if __name__ == '__main__':
    path_script = os.path.dirname(os.path.abspath(__file__))
    if len(sys.argv) == 1:
        file_xml = r'in\test.xml'
    else:
        file_xml = sys.argv[1]
        if not os.path.isfile(file_xml):
            print('WARNING: File argument not found. Use the default path.')
    parser(os.path.join(path_script, file_xml))
