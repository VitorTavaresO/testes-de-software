#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);
#define HUMIDITY 2

void setup() {
  pinMode(HUMIDITY, INPUT);
  Serial.begin(115200);
  lcd.init();
  lcd.clear();         
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Humidity: ");
  lcd.setCursor(0,1);
  lcd.print("Temperature: ");
  lcd.setCursor(0,2);
  lcd.print("Last Sunbath: ");
  lcd.setCursor(0,3);
  lcd.print("Last Attention: ");

}

void loop() {
  int val = map(analogRead(HUMIDITY), 0, 4095, 0, 100);
  Serial.println(val);
  delay(1000);
}
