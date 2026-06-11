"""Button entities for Delonghi Primadonna."""

from typing import Any

from homeassistant.components.button import ButtonEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .base_entity import DelonghiDeviceEntity
from .const import DOMAIN
from .device import DelongiPrimadonna


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Register button entities for a config entry."""
    device: DelongiPrimadonna = hass.data[DOMAIN][entry.unique_id]
    async_add_entities([
        DelongiPrimadonnaPowerOnButton(device, hass),
        DelongiPrimadonnaPowerOffButton(device, hass),
    ])


class DelongiPrimadonnaPowerOnButton(DelonghiDeviceEntity, ButtonEntity):
    """Button to turn on the coffee machine."""

    _attr_icon = "mdi:power"
    _attr_translation_key = "power_on"

    async def async_press(self, **kwargs: Any) -> None:
        """Handle the button press."""
        await self.device.power_on()


class DelongiPrimadonnaPowerOffButton(DelonghiDeviceEntity, ButtonEntity):
    """Button to turn off the coffee machine."""

    _attr_icon = "mdi:power-off"
    _attr_translation_key = "power_off"

    async def async_press(self, **kwargs: Any) -> None:
        """Handle the button press."""
        await self.device.power_off()
