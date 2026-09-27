import logging


class NetworkDevice:
    """Simple model of a network device."""

    def __init__(self, hostname, ip, type):
        self.hostname = hostname
        self.ip = ip
        self.type = type

    def summarize(self):
        """Print and log a one-line summary; also return it as a string."""
        msg = f"{self.hostname} ({self.type}) - {self.ip}"
        print(msg)
        logging.info(f"[DEVICE_SUMMARY]: {msg}")
        return msg
