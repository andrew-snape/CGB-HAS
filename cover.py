import logging
import requests
from homeassistant.components.cover import CoverEntity
from homeassistant.const import STATE_CLOSED, STATE_OPEN
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONF_IP = "ip_address"
CONF_API_KEY = "api_key"

DEFAULT_TIMEOUT = 5

PLATFORM_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_IP): cv.string,
        vol.Required(CONF_API_KEY): cv.string,
    }
)

def setup_platform(hass, config, add_entities, discovery_info=None):
    ip = config[CONF_IP]
    api_key = config[CONF_API_KEY]
    add_entities([CenturionGarageDoor(ip, api_key)])

class CenturionGarageDoor(CoverEntity):

    def __init__(self, ip, api_key):
        self._ip = ip
        self._api_key = api_key
        self._state = STATE_CLOSED

    def _base_url(self):
        return f"http://{self._ip}/api?key={self._api_key}"

    def update(self):
        try:
            response = requests.get(f"{self._base_url()}&status=json", timeout=DEFAULT_TIMEOUT)
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
        requests.get(f"{self._base_url()}&door=open")

    def close_cover(self, **kwargs):
        requests.get(f"{self._base_url()}&door=close")

    def stop_cover(self, **kwargs):
        requests.get(f"{self._base_url()}&door=stop")
