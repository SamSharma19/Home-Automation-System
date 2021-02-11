#include<CayenneMQTTESP8266.h>
#include<DHT.h>
#define CAYENNE_DEBUG
#define CAYENNE_PRINT Serial
char ssid[] = "Redmi";
char password[] = "samyak19";

char username[] = "85b78f10-f118-11ea-93bf-d33a96695544";
char mqtt_password[] ="e0ba2ccb1dc6ecca7fe61958f3ac561f2a45d717";
char client_id[] = "a114b760-f118-11ea-b767-3f1a8f1211ba";

DHT dht(D2,DHT11); 

void setup() {
  // put your setup code here, to run once:
  dht.begin();
  pinMode(D1,OUTPUT);
  Cayenne.begin(username,mqtt_password,client_id,ssid,password);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Cayenne.loop();
  float temp = dht.readTemperature(true);
  float hum = dht.readHumidity();
  Cayenne.virtualWrite(1, temp, TYPE_TEMPERATURE, UNIT_FAHRENHEIT);
  Cayenne.virtualWrite(2, hum, TYPE_RELATIVE_HUMIDITY, UNIT_PERCENT);
  Serial.print("temp is :");
  Serial.println(temp);
  Serial.print("humidity is :");
  Serial.println(hum);
  delay(2000);
}
//to take command form cayenne website
CAYENNE_IN(0)
{
  digitalWrite(D1, !getValue.asInt());
}
