#include <LiquidCrystal_I2C.h>
#include <Wire.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);
#define HUMIDITY 2

void setup() {
  pinMode(HUMIDITY, INPUT);
  Serial.begin(115200);
  lcd.begin (20,4);
}

void loop() {
  int val = map(analogRead(HUMIDITY), 0, 4095, 0, 100);
  Serial.println(val);
  delay(1000);
}
