import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import CONF_ID, UNIT_KILOWATT_HOURS, ICON_FLASH, ICON_WATER

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor"]

sensor_meter_heating_ns = cg.esphome_ns.namespace("sensor_meter_heating")
SensorMeterHeating = sensor_meter_heating_ns.class_("SensorMeterHeating", cg.PollingComponent, uart.UARTDevice)

CONF_KWH_SENSOR = "energy_sensor"
CONF_M3_SENSOR = "volume_sensor"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SensorMeterHeating),
    cv.Optional(CONF_KWH_SENSOR): sensor.sensor_schema(
        unit_of_measurement=UNIT_KILOWATT_HOURS,
        icon=ICON_FLASH,
        accuracy_decimals=2,
    ),
    cv.Optional(CONF_M3_SENSOR): sensor.sensor_schema(
        unit_of_measurement="m³",
        icon=ICON_WATER,
        accuracy_decimals=2,
    ),
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if CONF_KWH_SENSOR in config:
        sens = await sensor.new_sensor(config[CONF_KWH_SENSOR])
        cg.add(var.sensor_kWh, sens)

    if CONF_M3_SENSOR in config:
        sens = await sensor.new_sensor(config[CONF_M3_SENSOR])
        cg.add(var.sensor_m3, sens)
