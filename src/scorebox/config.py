#!/usr/bin/python
from configparser import ConfigParser
from typing import Dict


def config(filename: str = './configs/database.ini', section: str = 'postgresql') -> Dict[str, str]:
    parser: ConfigParser = ConfigParser()
    parser.read(filename)

    db: Dict[str, str] = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db
