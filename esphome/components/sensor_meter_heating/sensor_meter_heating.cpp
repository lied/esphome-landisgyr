#include "sensor_meter_heating.h"
#include "esphome/core/log.h"

namespace esphome {
namespace sensor_meter_heating {

static const char *TAG = "sensor_meter_heating";

void SensorMeterHeating::setup() {
  ESP_LOGD(TAG, "Initializing Landis+Gyr UH50/T555 Meter...");
}

void SensorMeterHeating::update() {
  ESP_LOGD(TAG, "Requesting data from meter...");

  // Example request: Send a meter read command
  this->write_str("\x2F\x3F\x21\x0D\x0A");

  // Wait for response
  std::string response;
  while (this->available()) {
    response += this->read();
  }

  if (!response.empty()) {
    this->parse_response(response);
  }
}

void SensorMeterHeating::parse_response(const std::string &response) {
  ESP_LOGD(TAG, "Received response: %s", response.c_str());

  // Simulated parsing logic (replace with actual parsing)
  float kWh_value = 123.45;  // Replace with parsed value
  float m3_value = 678.90;   // Replace with parsed value

  if (this->energy_sensor != nullptr) {
    this->energy_sensor->publish_state(kWh_value);
  }
  if (this->volume_sensor != nullptr) {
    this->volume_sensor->publish_state(m3_value);
  }

  ESP_LOGD(TAG, "Published kWh: %.2f, m³: %.2f", kWh_value, m3_value);
}

}  // namespace sensor_meter_heating
}  // namespace esphome
