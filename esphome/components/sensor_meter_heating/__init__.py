import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import CONF_ID, UNIT_KILOWATT_HOURS, UNIT_CUBIC_METERS, ICON_FLASH, ICON_WATER

DEPENDENCIES = ["uart"]

sensor_meter_heating_ns = cg.esphome_ns.namespace("sensor_meter_heating")
SensorMeterHeating = sensor_meter_heating_ns.class_("SensorMeterHeating", cg.PollingComponent, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SensorMeterHeating),
}).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    # Create and register the sensors
    kwh_sensor = cg.new_Pvariable(config[CONF_ID], SensorMeterHeating)
    await sensor.register_sensor(kwh_sensor, {
        "name": "Energy Consumption",
        "unit_of_measurement": UNIT_KILOWATT_HOURS,
        "icon": ICON_FLASH,
        "accuracy_decimals": 2,
    })

    m3_sensor = cg.new_Pvariable(config[CONF_ID], SensorMeterHeating)
    await sensor.register_sensor(m3_sensor, {
        "name": "Water Volume",
        "unit_of_measurement": UNIT_CUBIC_METERS,
        "icon": ICON_WATER,
        "accuracy_decimals": 2,
    })
