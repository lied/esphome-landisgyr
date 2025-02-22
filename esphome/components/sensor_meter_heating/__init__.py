import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID

DEPENDENCIES = ['uart']

sensor_meter_heating_ns = cg.esphome_ns.namespace('sensor_meter_heating')
SensorMeterHeating = sensor_meter_heating_ns.class_('SensorMeterHeating', cg.PollingComponent)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SensorMeterHeating),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    # Register sensors
    await sensor.register_sensor(var.sensor_kWh, {'unit_of_measurement': 'kWh', 'accuracy_decimals': 3})
    await sensor.register_sensor(var.sensor_m3, {'unit_of_measurement': 'm³', 'accuracy_decimals': 3})
