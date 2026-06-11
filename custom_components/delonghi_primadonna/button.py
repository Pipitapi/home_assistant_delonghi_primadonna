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
    async_add_entities([DelongiPrimadonnaPowerToggleButton(device, hass)])


class DelongiPrimadonnaPowerToggleButton(DelonghiDeviceEntity, ButtonEntity):
    """Button to toggle the coffee machine on/off."""

    _attr_translation_key = "power_toggle"

    @property
    def icon(self) -> str:
        return "mdi:power" if self.device.switches.is_on else "mdi:power-off"

    async def async_press(self, **kwargs: Any) -> None:
        """Toggle power based on current state."""
        if self.device.switches.is_on:
            await self.device.power_off()
        else:
            await self.device.power_on()
