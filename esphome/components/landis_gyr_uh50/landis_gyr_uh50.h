#ifndef LANDIS_GYR_UH50_H
#define LANDIS_GYR_UH50_H

#include "esphome.h"
#include "sensor.h"                         // Works in your environment for esphome::sensor::Sensor
#include "esphome/components/uart/uart.h"   // For uart::UARTComponent and uart::UARTDevice
// #include "/esphome/esphome/components/sensor/sensor.h"

namespace esphome {
namespace landis_gyr_uh50 {

class LandisGyrUH50 : public Component, public uart::UARTDevice {
 public:
  LandisGyrUH50() = default;
  void set_uart_parent(uart::UARTComponent *parent) { this->parent_ = parent; }

  void setup() override;
  void loop() override;

  void set_energy_sensor(esphome::sensor::Sensor *sensor) { energy_sensor_ = sensor; }
  void set_volume_sensor(esphome::sensor::Sensor *sensor) { volume_sensor_ = sensor; }
  void set_temp_in_sensor(esphome::sensor::Sensor *sensor) { temp_in_sensor_ = sensor; }
  void set_temp_out_sensor(esphome::sensor::Sensor *sensor) { temp_out_sensor_ = sensor; }

 protected:
  esphome::sensor::Sensor *energy_sensor_{nullptr};
  esphome::sensor::Sensor *volume_sensor_{nullptr};
  esphome::sensor::Sensor *temp_in_sensor_{nullptr};
  esphome::sensor::Sensor *temp_out_sensor_{nullptr};

  std::vector<uint8_t> buffer_;
  void parse_data_();

  uart::UARTComponent *parent_;
};

}  // namespace landis_gyr_uh50
}  // namespace esphome

#endif