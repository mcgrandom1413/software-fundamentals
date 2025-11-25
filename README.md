const int BATHROOM_LIGHT = 11;
const int BEDROOM_LIGHT = 12;
const int KITCHEN_LIGHT = 13;

// Light states
bool bathroom_state = LOW;
bool bedroom_state  = LOW;
bool kitchen_state  = LOW;

bool blinking_mode = false;

void menu() {
  Serial.println("- MENU -");
  Serial.println("[1] Turn ON bathroom light");
  Serial.println("[2] Turn OFF bathroom light");
  Serial.println("[3] Turn ON bedroom light");
  Serial.println("[4] Turn OFF bedroom light");
  Serial.println("[5] Turn ON kitchen light");
  Serial.println("[6] Turn OFF kitchen light");
  Serial.println("[7] Turn ON all lights");
  Serial.println("[8] Turn OFF all lights");
  Serial.println("[9] Activate infinite blinking mode");
}

void setup() {
  pinMode(BATHROOM_LIGHT, OUTPUT);
  pinMode(BEDROOM_LIGHT, OUTPUT);
  pinMode(KITCHEN_LIGHT, OUTPUT);

  Serial.begin(9600);
  menu();
}

void loop() {

  // ------------ READ INPUT ------------
  if (Serial.available() > 0) {
    char opt = Serial.read();

    switch (opt) {

      case '1': bathroom_state = HIGH; break;
      case '2': bathroom_state = LOW; break;

      case '3': bedroom_state = HIGH; break;
      case '4': bedroom_state = LOW; break;

      case '5': kitchen_state = HIGH; break;
      case '6': kitchen_state = LOW; break;

      case '7':
        bathroom_state = HIGH;
        bedroom_state  = HIGH;
        kitchen_state  = HIGH;
        break;

      case '8':
        bathroom_state = LOW;
        bedroom_state  = LOW;
        kitchen_state  = LOW;
        blinking_mode = false;  // stop blinking if all are turned off manually
        break;

      case '9':
        Serial.println("MODE 9: Infinite blinking activated.");
        blinking_mode = true;

        // force all ON so blinking can start
        bathroom_state = HIGH;
        bedroom_state  = HIGH;
        kitchen_state  = HIGH;
        break;
    }

    menu();
  }

  // ------------ BLINKING MODE ------------
  if (blinking_mode) {

    // IF all lights are OFF → STOP blinking
    if (bathroom_state == LOW && bedroom_state == LOW && kitchen_state == LOW) {
      blinking_mode = false;
      Serial.println("All lights OFF → blinking mode deactivated.");
      return;
    }

    // ON phase
    if (bathroom_state == HIGH) digitalWrite(BATHROOM_LIGHT, HIGH);
    if (bedroom_state  == HIGH) digitalWrite(BEDROOM_LIGHT, HIGH);
    if (kitchen_state  == HIGH) digitalWrite(KITCHEN_LIGHT, HIGH);
    delay(300);

    // OFF phase
    if (bathroom_state == HIGH) digitalWrite(BATHROOM_LIGHT, LOW);
    if (bedroom_state  == HIGH) digitalWrite(BEDROOM_LIGHT, LOW);
    if (kitchen_state  == HIGH) digitalWrite(KITCHEN_LIGHT, LOW);
    delay(300);

  } else {
    // NORMAL mode (lights do not blink)
    digitalWrite(BATHROOM_LIGHT, bathroom_state);
    digitalWrite(BEDROOM_LIGHT, bedroom_state);
    digitalWrite(KITCHEN_LIGHT, kitchen_state);
  }