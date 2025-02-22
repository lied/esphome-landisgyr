#ifndef LANDIS_GYR_UH50_H
#define LANDIS_GYR_UH50_H

#include "esphome.h"

namespace esphome {
namespace landis_gyr_uh50 {

class LandisGyrUH50 : public Component, public UARTDevice {
 public:
  // Constructor, taking UART as argument
  LandisGyrUH50(UARTComponent *parent);

  // Setup and loop functions required by Component
  void setup() override;
  void loop() override;

  // Method to set sensors from YAML config
  void set_energy_sensor(sensor::Sensor *sensor) { energy_sensor_ = sensor; }
  void set_volume_sensor(sensor::Sensor *sensor) { volume_sensor_ = sensor; }
  void set_temp_in_sensor(sensor::Sensor *sensor) { temp_in_sensor_ = sensor; }
  void set_temp_out_sensor(sensor::Sensor *sensor) { temp_out_sensor_ = sensor; }

 protected:
  sensor::Sensor *energy_sensor_{nullptr};  // Energy consumption (kWh)
  sensor::Sensor *volume_sensor_{nullptr};  // Volume (m³)
  sensor::Sensor *temp_in_sensor_{nullptr}; // Inlet temperature (°C)
  sensor::Sensor *temp_out_sensor_{nullptr}; // Outlet temperature (°C)

  // Variables for parsing UART data (adjust as needed)
  std::vector<uint8_t> buffer_;
  void parse_data_();  // Helper to process received data
};

}  // namespace landis_gyr_uh50
}  // namespace esphome

#endif