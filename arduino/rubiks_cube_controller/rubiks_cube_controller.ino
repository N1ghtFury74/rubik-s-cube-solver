/*
 * Rubik's Cube Solver Robot - Arduino Controller
 * Author: Momentum Software Team
 * Project: Professional Rubik's Cube Solver Robot
 * Year: 2022
 * Budget: 900 EGP
 * Performance: 10-12 second solve time
 * 
 * Description: Controls 6 stepper motors to execute cube solving moves
 * received from Python brain via serial communication.
 * 
 * Hardware Setup:
 * - 6 Stepper Motors (one for each face: U, D, L, R, F, B)
 * - Arduino Uno/Nano
 * - Stepper Motor Drivers
 * - Power Supply
 */

// ===== PIN DEFINITIONS =====
// Stepper motor pins for each cube face
#define STEP_UP 3       // Up face rotation motor
#define DIR_UP  2
#define STEP_DOWN 5     // Down face rotation motor  
#define DIR_DOWN 4
#define STEP_FORWARD 7  // Forward face rotation motor
#define DIR_FORWARD 6
#define STEP_BACK 9     // Back face rotation motor
#define DIR_BACK  8
#define STEP_LEFT 11    // Left face rotation motor
#define DIR_LEFT 10
#define STEP_RIGHT 13   // Right face rotation motor
#define DIR_RIGHT  12

// ===== TIMING CONFIGURATION =====
#define MOVE_DELAY 200          // Delay between moves (ms)
#define STEP_DELAY 1000         // Delay between steps (microseconds)
#define STEPS_90_DEGREE 50      // Steps for 90° rotation
#define STEPS_180_DEGREE 100    // Steps for 180° rotation

// ===== DIRECTION DEFINITIONS =====
// Clockwise and counter-clockwise directions for each face
#define U_CW   LOW
#define U_CCW  HIGH
#define D_CW   HIGH
#define D_CCW  LOW
#define L_CW   LOW
#define L_CCW  HIGH
#define R_CW   LOW
#define R_CCW  HIGH
#define F_CW   LOW
#define F_CCW  HIGH
#define B_CW   LOW
#define B_CCW  HIGH

// ===== GLOBAL VARIABLES =====
String receivedMoves = "";
bool isExecuting = false;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Configure stepper motor pins as outputs
  pinMode(STEP_UP, OUTPUT);
  pinMode(DIR_UP, OUTPUT);
  pinMode(STEP_DOWN, OUTPUT);
  pinMode(DIR_DOWN, OUTPUT);
  pinMode(STEP_FORWARD, OUTPUT);
  pinMode(DIR_FORWARD, OUTPUT);
  pinMode(STEP_BACK, OUTPUT);
  pinMode(DIR_BACK, OUTPUT);
  pinMode(STEP_LEFT, OUTPUT);
  pinMode(DIR_LEFT, OUTPUT);
  pinMode(STEP_RIGHT, OUTPUT);
  pinMode(DIR_RIGHT, OUTPUT);
  
  // Send ready signal
  Serial.println("RUBIKS_ROBOT_READY");
  Serial.println("Momentum Team - 900 EGP Robot - 10-12s Solver");
}

void loop() {
  // Wait for moves from Python brain
  if (Serial.available()) {
    delay(100);  // Allow complete message to arrive
    receivedMoves = Serial.readString();
    receivedMoves.trim();  // Remove whitespace
    
    if (receivedMoves.length() > 0) {
      Serial.println("Received: " + receivedMoves);
      executeMoveSequence(receivedMoves);
      Serial.println("MOVES_COMPLETED");
    }
  }
}

void executeMoveSequence(String moves) {
  isExecuting = true;
  Serial.println("Starting cube solution...");
  
  int moveCount = 0;
  
  for (int i = 0; i < moves.length(); ) {
    String currentMove = "";
    
    // Parse move (handle single moves, prime moves, and double moves)
    if (i + 1 < moves.length() && (moves[i + 1] == '2' || moves[i + 1] == '\'')) {
      currentMove = moves.substring(i, i + 2);
      i += 2;
    } else {
      currentMove = moves[i];
      i++;
    }
    
    // Execute the move
    executeMove(currentMove);
    moveCount++;
    
    // Progress feedback
    if (moveCount % 5 == 0) {
      Serial.println("Progress: " + String(moveCount) + " moves completed");
    }
    
    delay(MOVE_DELAY);  // Delay between moves
  }
  
  Serial.println("Solution completed! Total moves: " + String(moveCount));
  isExecuting = false;
}

void executeMove(String move) {
  char face = move[0];
  
  switch (face) {
    case 'U':
      rotateUp(move);
      break;
    case 'D':
      rotateDown(move);
      break;
    case 'R':
      rotateRight(move);
      break;
    case 'L':
      rotateLeft(move);
      break;
    case 'F':
      rotateForward(move);
      break;
    case 'B':
      rotateBack(move);
      break;
    default:
      Serial.println("Unknown move: " + move);
  }
}

void rotateUp(String move) {
  if (move == "U") {
    digitalWrite(DIR_UP, U_CW);
    stepMotor(STEP_UP, STEPS_90_DEGREE);
  } else if (move == "U'") {
    digitalWrite(DIR_UP, U_CCW);
    stepMotor(STEP_UP, STEPS_90_DEGREE);
  } else if (move == "U2") {
    digitalWrite(DIR_UP, U_CW);
    stepMotor(STEP_UP, STEPS_180_DEGREE);
  }
}

void rotateDown(String move) {
  if (move == "D") {
    digitalWrite(DIR_DOWN, D_CW);
    stepMotor(STEP_DOWN, STEPS_90_DEGREE);
  } else if (move == "D'") {
    digitalWrite(DIR_DOWN, D_CCW);
    stepMotor(STEP_DOWN, STEPS_90_DEGREE);
  } else if (move == "D2") {
    digitalWrite(DIR_DOWN, D_CW);
    stepMotor(STEP_DOWN, STEPS_180_DEGREE);
  }
}

void rotateRight(String move) {
  if (move == "R") {
    digitalWrite(DIR_RIGHT, R_CW);
    stepMotor(STEP_RIGHT, STEPS_90_DEGREE);
  } else if (move == "R'") {
    digitalWrite(DIR_RIGHT, R_CCW);
    stepMotor(STEP_RIGHT, STEPS_90_DEGREE);
  } else if (move == "R2") {
    digitalWrite(DIR_RIGHT, R_CW);
    stepMotor(STEP_RIGHT, STEPS_180_DEGREE);
  }
}

void rotateLeft(String move) {
  if (move == "L") {
    digitalWrite(DIR_LEFT, L_CW);
    stepMotor(STEP_LEFT, STEPS_90_DEGREE);
  } else if (move == "L'") {
    digitalWrite(DIR_LEFT, L_CCW);
    stepMotor(STEP_LEFT, STEPS_90_DEGREE);
  } else if (move == "L2") {
    digitalWrite(DIR_LEFT, L_CW);
    stepMotor(STEP_LEFT, STEPS_180_DEGREE);
  }
}

void rotateForward(String move) {
  if (move == "F") {
    digitalWrite(DIR_FORWARD, F_CW);
    stepMotor(STEP_FORWARD, STEPS_90_DEGREE);
  } else if (move == "F'") {
    digitalWrite(DIR_FORWARD, F_CCW);
    stepMotor(STEP_FORWARD, STEPS_90_DEGREE);
  } else if (move == "F2") {
    digitalWrite(DIR_FORWARD, F_CW);
    stepMotor(STEP_FORWARD, STEPS_180_DEGREE);
  }
}

void rotateBack(String move) {
  if (move == "B") {
    digitalWrite(DIR_BACK, B_CW);
    stepMotor(STEP_BACK, STEPS_90_DEGREE);
  } else if (move == "B'") {
    digitalWrite(DIR_BACK, B_CCW);
    stepMotor(STEP_BACK, STEPS_90_DEGREE);
  } else if (move == "B2") {
    digitalWrite(DIR_BACK, B_CW);
    stepMotor(STEP_BACK, STEPS_180_DEGREE);
  }
}

void stepMotor(int stepPin, int steps) {
  for (int i = 0; i < steps; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(STEP_DELAY);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(STEP_DELAY);
  }
}
