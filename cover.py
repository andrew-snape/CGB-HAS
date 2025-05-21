import logging
import requests
from homeassistant.components.cover import CoverEntity
from homeassistant.const import STATE_CLOSED, STATE_OPEN

_LOGGER = logging.getLogger(__name__)

URL = "http://192.168.1.100/api?key=a304d45d1d9d1316ae77bc2ae1de812b"

def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([CenturionGarageDoor()])

class CenturionGarageDoor(CoverEntity):

    def __init__(self):
        self._state = STATE_CLOSED

    def update(self):
        try:
            response = requests.get(f"{URL}&status=json", timeout=5)
            data = response.json()
            self._state = STATE_OPEN if data["door"] == "open" else STATE_CLOSED
        except Exception as e:
            _LOGGER.error(f"Error updating Centurion door status: {e}")

    @property
    def name(self):
        return "Centurion Garage Door"

    @property
    def is_closed(self):
        return self._state == STATE_CLOSED

    def open_cover(self, **kwargs):
        requests.get(f"{URL}&door=open")

    def close_cover(self, **kwargs):
        requests.get(f"{URL}&door=close")

    def stop_cover(self, **kwargs):
        requests.get(f"{URL}&door=stop")
