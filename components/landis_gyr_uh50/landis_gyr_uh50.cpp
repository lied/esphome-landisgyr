#include "landis_gyr_uh50.h"

namespace esphome {
namespace landis_gyr_uh50 {

void LandisGyrUH50::setup() {
  ESP_LOGD("landis_gyr_uh50", "Setting up Landis+Gyr UH50 component...");
}

void LandisGyrUH50::loop() {
  while (this->available()) {
    buffer_.push_back(this->read());
  }
  if (!buffer_.empty() && buffer_.size() >= 100) {
    parse_data_();
    buffer_.clear();
  }
}

void LandisGyrUH50::parse_data_() {
  if (buffer_.size() < 10) return;

  float energy = buffer_[2] * 256 + buffer_[3];
  float volume = buffer_[4] * 256 + buffer_[5];
  float temp_in = buffer_[6];
  float temp_out = buffer_[7];

  if (energy_sensor_) energy_sensor_->publish_state(energy / 100.0);
  if (volume_sensor_) volume_sensor_->publish_state(volume / 1000.0);
  if (temp_in_sensor_) temp_in_sensor_->publish_state(temp_in);
  if (temp_out_sensor_) temp_out_sensor_->publish_state(temp_out);

  ESP_LOGD("landis_gyr_uh50", "Parsed data - Energy: %.2f kWh, Volume: %.3f m³", 
           energy / 100.0, volume / 1000.0);
}

}  // namespace landis_gyr_uh50
}  // namespace esphome