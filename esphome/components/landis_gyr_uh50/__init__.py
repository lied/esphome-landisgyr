import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID, CONF_UART_ID

# Define the namespace and class for the C++ component
landis_gyr_uh50_ns = cg.esphome_ns.namespace("landis_gyr_uh50")
LandisGyrUH50 = landis_gyr_uh50_ns.class_(
    "LandisGyrUH50", cg.Component, uart.UARTDevice
)

# Define YAML configuration schema
CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(LandisGyrUH50),
        cv.Required(CONF_UART_ID): cv.use_id(uart.UARTComponent),
        cv.Optional("energy_sensor"): cv.Schema(
            {
                cv.GenerateID(): cv.declare_id(cg.Sensor),
                cv.Optional("name", default="Energy Usage"): cv.string,
                cv.Optional("unit_of_measurement", default="kWh"): cv.string,
                cv.Optional("accuracy_decimals", default=2): cv.positive_int,
            }
        ),
        cv.Optional("volume_sensor"): cv.Schema(
            {
                cv.GenerateID(): cv.declare_id(cg.Sensor),
                cv.Optional("name", default="Water Volume"): cv.string,
                cv.Optional("unit_of_measurement", default="m³"): cv.string,
                cv.Optional("accuracy_decimals", default=3): cv.positive_int,
            }
        ),
        cv.Optional("temp_in_sensor"): cv.Schema(
            {
                cv.GenerateID(): cv.declare_id(cg.Sensor),
                cv.Optional("name", default="Inlet Temperature"): cv.string,
                cv.Optional("unit_of_measurement", default="°C"): cv.string,
                cv.Optional("accuracy_decimals", default=1): cv.positive_int,
            }
        ),
        cv.Optional("temp_out_sensor"): cv.Schema(
            {
                cv.GenerateID(): cv.declare_id(cg.Sensor),
                cv.Optional("name", default="Outlet Temperature"): cv.string,
                cv.Optional("unit_of_measurement", default="°C"): cv.string,
                cv.Optional("accuracy_decimals", default=1): cv.positive_int,
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

    # Link