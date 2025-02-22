#ifndef LANDIS_GYR_UH50_H
#define LANDIS_GYR_UH50_H

#include "esphome.h"
#include "sensor.h"                         // Works in your environment
#include "esphome/components/uart/uart.h"   // For uart::UARTComponent and uart::UARTDevice

namespace esphome {
namespace landis_gyr_uh50 {

class LandisGyrUH50 : public Component, public uart::UARTDevice {
 public:
  LandisGyrUH50() = default;
  void set_uart_parent(uart::UARTComponent *parent) { this->parent_ = parent; }

  void setup() override;
  void loop() override;

  // Use sensor::Sensor directly, assuming sensor.h provides it
  void set_energy_sensor(sensor::Sensor *sensor) { energy_sensor_ = sensor; }
  void set_volume_sensor(sensor::Sensor *sensor) { volume_sensor_ = sensor; }
  void set_temp_in_sensor(sensor::Sensor *sensor) { temp_in_sensor_ = sensor; }
  void set_temp_out_sensor(sensor::Sensor *sensor) { temp_out_sensor_ = sensor; }

 protected:
  sensor::Sensor *energy_sensor_{nullptr};
  sensor::Sensor *volume_sensor_{nullptr};
  sensor::Sensor *temp_in_sensor_{nullptr};
  sensor::Sensor *temp_out_sensor_{nullptr};

  std::vector<uint8_t> buffer_;
  void parse_data_();

  uart::UARTComponent *parent_;
};

}  // namespace landis_gyr_uh50
}  // namespace esphome

#endif