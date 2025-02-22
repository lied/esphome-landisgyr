#include "landis_gyr_uh50.h"

namespace esphome {
namespace landis_gyr_uh50 {

LandisGyrUH50::LandisGyrUH50(UARTComponent *parent) : UARTDevice(parent) {}

void LandisGyrUH50::setup() {
  // Initialize UART settings (baud rate, parity, etc.)
  // Example: 2400 baud, 7E1 (common for Landis+Gyr meters)
  // Adjust based on your meter's specs
  ESP_LOGD("landis_gyr_uh50", "Setting up Landis+Gyr UH50 component...");
}

void LandisGyrUH50::loop() {
  // Read available bytes from UART
  while (available()) {
    buffer_.push_back(read());
  }

  // Process data when a full message is received
  if (!buffer_.empty() && buffer_.size() >= 100) {  // Adjust size based on protocol
    parse_data_();
    buffer_.clear();
  }
}

void LandisGyrUH50::parse_data_() {
  // Example parsing logic (replace with actual protocol from sensorMeterHeating.h)
  // Assuming a simple protocol for demonstration
  if (buffer_.size() < 10) return;  // Minimum length check

  // Dummy parsing (replace with real logic)
  float energy = buffer_[2] * 256 + buffer_[3];  // Example: kWh
  float volume = buffer_[4] * 256 + buffer_[5];  // Example: m³
  float temp_in = buffer_[6];                    // Example: °C
  float temp_out = buffer_[7];                   // Example: °C

  // Publish sensor values if sensors are defined in YAML
  if (energy_sensor_) energy_sensor_->publish_state(energy / 100.0);
  if (volume_sensor_) volume_sensor_->publish_state(volume / 1000.0);
  if (temp_in_sensor_) temp_in_sensor_->publish_state(temp_in);
  if (temp_out_sensor_) temp_out_sensor_->publish_state(temp_out);

  ESP_LOGD("landis_gyr_uh50", "Parsed data - Energy: %.2f kWh, Volume: %.3f m³", 
           energy / 100.0, volume / 1000.0);
}

}  // namespace landis_gyr_uh50
}  // namespace esphome