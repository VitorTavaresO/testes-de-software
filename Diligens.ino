void setup() {
  pinMode(2, INPUT);
  Serial.begin(115200);
}

void loop() {
  int val = analogRead(2);
  Serial.println(val);
  delay(1000);
}
