#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 20, 4);
#define HUMIDITY 2
#define TEMPERATURE 13
#define BUZZER 18

void setup() {
  pinMode(HUMIDITY, INPUT);
  pinMode(TEMPERATURE, INPUT);
  pinMode(BUZZER, OUTPUT);
  Serial.begin(115200);

  lcd.init();
  lcd.clear();         
  lcd.backlight();

  lcd.setCursor(0,0);
  lcd.print("Humidity: ");
  lcd.setCursor(0,1);
  lcd.print("Temperature: ");
  lcd.setCursor(0,2);
  lcd.print("Sunbath: ");

}

void loop() {
  int humidity_output = map(analogRead(HUMIDITY), 0, 4095, 0, 99);
  int temperature_output = map(analogRead(TEMPERATURE), 0, 4095, 0, 100);
  if(humidity_output < 20){
    analogWrite(BUZZER, 255);
    lcd.setCursor(0,3);
    lcd.print("!!!!Low Humidity!!!!");
  }
  else if(humidity_output > 60){
    analogWrite(BUZZER, 255);
    lcd.setCursor(0,3);
    lcd.print("!!!!High Humidity!!!");
  }
  else if(temperature_output < 20){
    analogWrite(BUZZER, 255);
    lcd.setCursor(0,3);
    lcd.print("!!!Low Temperature!!");
  }
    else if(temperature_output > 30){
    analogWrite(BUZZER, 255);
    lcd.setCursor(0,3);
    lcd.print("!!High Temperature!!");
  }
  else{
    lcd.setCursor(0,3);
    lcd.print("                    ");
  }

  lcd.setCursor(10,0);
  lcd.print(humidity_output);
  lcd.setCursor(12,0);
  lcd.print("%");

  lcd.setCursor(13,1);
  lcd.print(temperature_output);
  lcd.setCursor(15,1);
  lcd.print("C");

  lcd.setCursor(9,2);
  lcd.print("12:52-10/08");

  delay(1000);
}
