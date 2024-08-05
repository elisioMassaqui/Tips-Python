#include <Servo.h>

Servo myservo;

void setup() {
    Serial.begin(9600);
    myservo.attach(9);
}

void loop() {
    if (Serial.available() > 0) {
        int angle = Serial.parseInt();
        myservo.write(angle);
        Serial.println(angle);
    }
}
