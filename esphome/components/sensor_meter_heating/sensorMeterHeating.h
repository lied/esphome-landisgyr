#pragma once

#include "esphome.h"

namespace esphome {
namespace sensor_meter_heating {

class SensorMeterHeating : public PollingComponent, public uart::UARTDevice {
 public:
  Sensor *sensor_kWh = nullptr;
  Sensor *sensor_m3 = nullptr;

  SensorMeterHeating() : PollingComponent(60000) {}  // Poll every 60s

  void setup() override;
  void update() override;
};

}  // namespace sensor_meter_heating
}  // namespace esphome
