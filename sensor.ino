#include "dht.h"
int sensor = A2;
dht DHT;

void setup() {
 Serial.begin(9600);
 delay(1000);
}

void loop() {
  DHT.read11(sensor);

Serial.println(DHT.temperature,0);
Serial.println(DHT.humidity);

delay(500);


}
