import logging
import requests
from homeassistant.components.cover import CoverEntity
from homeassistant.const import STATE_CLOSED, STATE_OPEN
from .const import DOMAIN, CONF_IP_ADDRESS, CONF_API_KEY

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    ip = config_entry.data[CONF_IP_ADDRESS]
    api_key = config_entry.data[CONF_API_KEY]
    async_add_entities([CenturionGarageDoor(ip, api_key)], update_before_add=True)

class CenturionGarageDoor(CoverEntity):
    def __init__(self, ip, api_key):
        self._ip = ip
        self._api_key = api_key
        self._state = STATE_CLOSED
        self._attr_unique_id = f"centurion_garage_{ip.replace('.', '_')}"

    def _base_url(self):
        return f"http://{self._ip}/api?key={self._api_key}"

    def update(self):
        try:
            url = f"{self._base_url()}&status=json"
            _LOGGER.debug(f"Fetching door status from: {url}")
            response = requests.get(url, timeout=5)
            data = response.json()
            door_state = data.get("door", "").lower()
            self._state = STATE_OPEN if door_state == "open" else STATE_CLOSED
            _LOGGER.debug(f"Door status updated: {self._state}")
        except Exception as e:
            _LOGGER.error(f"Error updating Centurion door status: {e}")

    @property
    def name(self):
        return "Centurion Garage Door"

    @property
    def is_closed(self):
        return self._state == STATE_CLOSED

    def open_cover(self, **kwargs):
        try:
            url = f"{self._base_url()}&door=open"
            _LOGGER.debug(f"Sending open command to: {url}")
            requests.get(url, timeout=5)
            self._state = STATE_OPEN
            self.schedule_update_ha_state()
        except Exception as e:
            _LOGGER.error(f"Error sending open command: {e}")

    def close_cover(self, **kwargs):
        try:
            url = f"{self._base_url()}&door=close"
            _LOGGER.debug(f"Sending close command to: {url}")
            requests.get(url, timeout=5)
            self._state = STATE_CLOSED
            self.schedule_update_ha_state()
        except Exception as e:
            _LOGGER.error(f"Error sending close command: {e}")

    def stop_cover(self, **kwargs):
        try:
            url = f"{self._base_url()}&door=stop"
            _LOGGER.debug(f"Sending stop command to: {url}")
            requests.get(url, timeout=5)
        except Exception as e:
            _LOGGER.error(f"Error sending stop command: {e}")
