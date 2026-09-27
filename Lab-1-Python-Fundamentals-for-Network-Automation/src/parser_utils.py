import csv
import json
import logging
import xml.etree.ElementTree as ET

import yaml


def _unwrap(data):
    """If a file wraps its list in a single top-level key, return the list."""
    if isinstance(data, dict) and len(data) == 1:
        only = next(iter(data.values()))
        if isinstance(only, list):
            return only
    return data


def parse_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = _unwrap(json.load(f))
        logging.info("PARSE_JSON_SUCCESS")
        return data
    except FileNotFoundError:
        logging.error(f"PARSE_JSON_ERROR: file not found: {path}")
    except json.JSONDecodeError as e:
        logging.error(f"PARSE_JSON_ERROR: {e}")
    return []


def parse_yaml(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = _unwrap(yaml.safe_load(f))
        logging.info("PARSE_YAML_SUCCESS")
        return data
    except FileNotFoundError:
        logging.error(f"PARSE_YAML_ERROR: file not found: {path}")
    except yaml.YAMLError as e:
        logging.error(f"PARSE_YAML_ERROR: {e}")
    return []


def parse_xml(path):
    """Return a list of dicts, one per child element of the root."""
    try:
        root = ET.parse(path).getroot()
        items = []
        for elem in root:
            item = dict(elem.attrib)
            for child in elem:
                item[child.tag] = (child.text or "").strip()
            items.append(item)
        logging.info("PARSE_XML_SUCCESS")
        return items
    except FileNotFoundError:
        logging.error(f"PARSE_XML_ERROR: file not found: {path}")
    except ET.ParseError as e:
        logging.error(f"PARSE_XML_ERROR: {e}")
    return []


def parse_csv(path):
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        logging.info("PARSE_CSV_SUCCESS")
        return rows
    except FileNotFoundError:
        logging.error(f"PARSE_CSV_ERROR: file not found: {path}")
    except csv.Error as e:
        logging.error(f"PARSE_CSV_ERROR: {e}")
    return []
