#include "esphome.h"

class SensorMeterHeating : public PollingComponent {
 public:
  Sensor *sensor_kWh = new Sensor();
  Sensor *sensor_m3 = new Sensor();

  SensorMeterHeating() : PollingComponent(60000) {}  // Poll every 60 seconds

  float get_setup_priority() const override { return esphome::setup_priority::HARDWARE; }

  void setup() override {
    // Initialization code here
  }

  void update() override {
    // Communication and data parsing code here
  }
};
