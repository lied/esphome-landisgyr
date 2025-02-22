import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import CONF_ID, CONF_UART_ID, CONF_NAME, CONF_UNIT_OF_MEASUREMENT, CONF_ACCURACY_DECIMALS

# Define the namespace and class for the C++ component
landis_gyr_uh50_ns = cg.esphome_ns.namespace("landis_gyr_uh50")
LandisGyrUH50 = landis_gyr_uh50_ns.class_(
    "LandisGyrUH50", cg.Component, uart.UARTDevice
)

# Sensor configuration schema
SENSOR_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(sensor.Sensor),
        cv.Optional(CONF_NAME): cv.string,
        cv.Optional(CONF_UNIT_OF_MEASUREMENT): cv.string,
        cv.Optional(CONF_ACCURACY_DECIMALS): cv.positive_int,
    }
)

# Define YAML configuration schema for the component
CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(LandisGyrUH50),
        cv.Required(CONF_UART_ID): cv.use_id(uart.UARTComponent),
        cv.Optional("energy_sensor"): SENSOR_SCHEMA.extend(
            {
                cv.Optional(CONF_NAME, default="Energy Usage"): cv.string,
                cv.Optional(CONF_UNIT_OF_MEASUREMENT, default="kWh"): cv.string,
                cv.Optional(CONF_ACCURACY_DECIMALS, default=2): cv.positive_int,
            }
        ),
        cv.Optional("volume_sensor"): SENSOR_SCHEMA.extend(
            {
                cv.Optional(CONF_NAME, default="Water Volume"): cv.string,
                cv.Optional(CONF_UNIT_OF_MEASUREMENT, default="m³"): cv.string,
                cv.Optional(CONF_ACCURACY_DECIMALS, default=3): cv.positive_int,
            }
        ),
        cv.Optional("temp_in_sensor"): SENSOR_SCHEMA.extend(
            {
                cv.Optional(CONF_NAME, default="Inlet Temperature"): cv.string,
                cv.Optional(CONF_UNIT_OF_MEASUREMENT, default="°C"): cv.string,
                cv.Optional(CONF_ACCURACY_DECIMALS, default=1): cv.positive_int,
            }
        ),
        cv.Optional("temp_out_sensor"): SENSOR_SCHEMA.extend(
            {
                cv.Optional(CONF_NAME, default="Outlet Temperature"): cv.string,
                cv.Optional(CONF_UNIT_OF_MEASUREMENT, default="°C"): cv.string,
                cv.Optional(CONF_ACCURACY_DECIMALS, default=1): cv.positive_int,
            }
        ),
    }
).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)

# Function to generate the C++ code during compilation
async def to_code(config):
    # Create the component instance
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    # Link UART
    uart_component = await cg.get_variable(config[CONF_UART_ID])
    cg.add(var.set_uart_parent(uart_component))

    # Register sensors if defined in YAML
    if "energy_sensor" in config:
        conf = config["energy_sensor"]
        sens = cg.new_Pvariable(conf[CONF_ID])
        cg.add(sens.set_name(conf[CONF_NAME]))
        cg.add(sens.set_unit_of_measurement(conf[CONF_UNIT_OF_MEASUREMENT]))
        cg.add(sens.set_accuracy_decimals(conf[CONF_ACCURACY_DECIMALS]))
        cg.add(var.set_energy_sensor(sens))

    if "volume_sensor" in config:
        conf = config["volume_sensor"]
        sens = cg.new_Pvariable(conf[CONF_ID])
        cg.add(sens.set_name(conf[CONF_NAME]))
        cg.add(sens.set_unit_of_measurement(conf[CONF_UNIT_OF_MEASUREMENT]))
        cg.add(sens.set_accuracy_decimals(conf[CONF_ACCURACY_DECIMALS]))
        cg.add(var.set_volume_sensor(sens))

    if "temp_in_sensor" in config:
        conf = config["temp_in_sensor"]
        sens = cg.new_Pvariable(conf[CONF_ID])
        cg.add(sens.set_name(conf[CONF_NAME]))
        cg.add(sens.set_unit_of_measurement(conf[CONF_UNIT_OF_MEASUREMENT]))
        cg.add(sens.set_accuracy_decimals(conf[CONF_ACCURACY_DECIMALS]))
        cg.add(var.set_temp_in_sensor(sens))

    if "temp_out_sensor" in config:
        conf = config["temp_out_sensor"]
        sens = cg.new_Pvariable(conf[CONF_ID])
        cg.add(sens.set_name(conf[CONF_NAME]))
        cg.add(sens.set_unit_of_measurement(conf[CONF_UNIT_OF_MEASUREMENT]))
        cg.add(sens.set_accuracy_decimals(conf[CONF_ACCURACY_DECIMALS]))
        cg.add(var.set_temp_out_sensor(sens))