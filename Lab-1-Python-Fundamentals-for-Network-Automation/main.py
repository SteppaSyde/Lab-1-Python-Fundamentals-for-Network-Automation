import logging
import os

from src.network_device import NetworkDevice
from src.parser_utils import parse_csv, parse_json, parse_xml, parse_yaml


os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename="logs/lab.log", level=logging.INFO)


def main():
    devices = parse_json("data/devices.json")
    interfaces = parse_yaml("data/interfaces.yaml")
    vlans = parse_xml("data/vlans.xml")
    inventory = parse_csv("data/inventory.csv")

    for d in devices:
        NetworkDevice(d["hostname"], d["ip"], d["type"]).summarize()

    for i in interfaces:
        msg = f"Interface {i['name']} is {i['status']}"
        print(msg)
        logging.info(f"INTERFACE_MSG: {msg}")

    for d in inventory:
        msg = f"Device {d['hostname']} is a {d['location']} {d['role']}"
        print(msg)
        logging.info(f"DEVICE_MSG: {msg}")

    for v in vlans:
        msg = f"VLAN {v['id']} is the {v['name']}"
        print(msg)
        logging.info(f"VLAN_MSG: {msg}")


if __name__ == "__main__":
    logging.info("[LAB1-START] LAB1_START")
    main()
    logging.info("[LAB1-END] LAB1_END")
