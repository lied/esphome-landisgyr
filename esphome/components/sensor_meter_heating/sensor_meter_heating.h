#pragma once

#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"
#include "esphome/core/component.h"

namespace esphome {
namespace sensor_meter_heating {

class SensorMeterHeating : public PollingComponent, public uart::UARTDevice {
 public:
  sensor::Sensor *sensor_kWh{nullptr};
  sensor::Sensor *sensor_m3{nullptr};

  SensorMeterHeating() : PollingComponent(60000) {}

  void setup() override;
  void update() override;
  void parse_response(const std::string &response);
};

}  // namespace sensor_meter_heating
}  // namespace esphome
