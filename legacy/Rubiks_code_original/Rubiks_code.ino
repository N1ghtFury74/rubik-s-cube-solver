/*
 *Author : Momentum SoftWare team. 
 *Project : Rubk's cube solver robot.
 *Idea : using python libraries to solve cube ( cubesolver & pyserial)
 ########################################################################
   structure of code :
   1/ get string from rubiks solver arduino library.
   2/ deal with string as every charcter represent specific move. 
   3/calling functions to be implemented.
   note : passing string to function as some mover doen't contaion one charcter
 */
///// pins of stepper ///
#define stepUp 3 // up rotation motor pin 
#define dirUp  2
#define stepDown 5  // down rotation motor pin 
#define dirDown 4
#define stepForward 7 // forward rotation motor pin 
#define dirForward 6
#define stepBack 9 // back rotation motor pin  
#define dirBack  8
#define stepLeft 11 // left rotation motor pin 
#define dirLeft 10
#define stepRight 13 // right rotation motor pin 
#define dirRight  12

#define MOVE_DELAY 200

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

const float stepPerAngle = 1.8 ;// 1 step = 1.8 degree
String moves;
//////  stepper library ////// 
#include <Stepper.h> 
void setup() 
{
  ////// stepper pins ///////////
   pinMode(stepUp,OUTPUT);
      pinMode(stepDown,OUTPUT);
         pinMode(stepForward,OUTPUT);
         pinMode(stepBack,OUTPUT);
     pinMode(stepLeft,OUTPUT);
   pinMode(stepRight,OUTPUT);
   ///////// direction pins /////////
   pinMode(dirUp,OUTPUT);
      pinMode(dirDown,OUTPUT);
         pinMode(dirForward,OUTPUT);
         pinMode(dirBack,OUTPUT);
     pinMode(dirLeft,OUTPUT);
   pinMode(dirRight,OUTPUT);
   /////////***************////////////////
 Serial.begin(9600);
}
void rotateUp(String M)
{
  if(M=="U")
  {
    digitalWrite(dirUp,U_CW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepUp,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepUp,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="U'")
  {
    digitalWrite(dirUp,U_CCW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepUp,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepUp,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="U2")
  {
    digitalWrite(dirUp,U_CW);
    for(int i=0;i<100;i++)
    {
           digitalWrite(stepUp,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepUp,LOW);

           delayMicroseconds(1000);
      
    }
  }
}
void rotateDown(String M)
{
  if(M=="D")
  {
    digitalWrite(dirDown,D_CW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepDown,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepDown,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="D'")
  {
    digitalWrite(dirDown,D_CCW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepDown,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepDown,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="D2")
  {
    digitalWrite(dirDown,D_CW);
    for(int i=0;i<100;i++)
    {
           digitalWrite(stepDown,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepDown,LOW);

           delayMicroseconds(1000);
      
    }
  }
}
void rotateForward(String M)
{
  if(M=="F")
  {
    digitalWrite(dirForward,F_CW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepForward,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepForward,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="F'")
  {
    digitalWrite(dirForward,F_CCW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepForward,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepForward,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="F2")
  {
    digitalWrite(dirForward,F_CW);
    for(int i=0;i<100;i++)
    {
           digitalWrite(stepForward,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepForward,LOW);

           delayMicroseconds(1000);
      
    }
  }
}
void rotateBack(String M)
{
   if(M=="B")
  {
    digitalWrite(dirBack,B_CW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepBack,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepBack,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="B'")
  {
    digitalWrite(dirBack,B_CCW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepBack,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepBack,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="B2")
  {
    digitalWrite(dirBack,B_CW);
    for(int i=0;i<100;i++)
    {
           digitalWrite(stepBack,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepBack,LOW);

           delayMicroseconds(1000);
      
    }
  }
}
void rotateLeft(String M)
{
  if(M=="L")
  {
    digitalWrite(dirLeft,L_CW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepLeft,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepLeft,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="L'")
  {
    digitalWrite(dirLeft,L_CCW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepLeft,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepLeft,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="L2")
  {
    digitalWrite(dirLeft,L_CW);
    for(int i=0;i<100;i++)
    {
           digitalWrite(stepLeft,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepLeft,LOW);

           delayMicroseconds(1000);
      
    }
  }
}
void rotateRight(String M)
{
   if(M=="R")
  {
    digitalWrite(dirRight,R_CW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepRight,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepRight,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="R'")
  {
    digitalWrite(dirRight,R_CCW);
    for(int i=0;i<50;i++)
    {
           digitalWrite(stepRight,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepRight,LOW);

           delayMicroseconds(1000);
      
    }
  }
  else if(M=="R2")
  {
    digitalWrite(dirRight,R_CW);
    for(int i=0;i<100;i++)
    {
           digitalWrite(stepRight,HIGH);

           delayMicroseconds(1000);

           digitalWrite(stepRight,LOW);

           delayMicroseconds(1000);
      
    }
  }
}
void loop() {
   // prepare string 
    while (!Serial.available());
    if (Serial.available()){
      delay(100);
      moves = Serial.readString();
      delay(500);
    }
      Serial.println(moves);
      delay(5000);
  /* moves.replace(" ",""); // deleting spaces
   moves.replace(",",""); // deleting commas 
   moves.replace("[",""); // deleting openning bracket
   moves.replace("]",""); // deleting closing bracket 
   */
   for(int i =0; i < moves.length(); ) 
   {
     String mov ="";
     if(moves[i+1]=='2'||moves[i+1]==39) // if the move consists of more than a charachter ,, like R2 or L' ,, 39 is ASCII of ' 
          {
            mov=moves.substring(i,i+2);
            i+=2;
          } 
      else
          {
            mov=moves[i];
            i++;
           }
     ///////////  functions calling //////////// 
     if(mov[0]=='U')
         rotateUp(mov),delay(MOVE_DELAY);
     else if(mov[0]=='D')
         rotateDown(mov),delay(MOVE_DELAY);
    else if(mov[0]=='R')
         rotateRight(mov),delay(MOVE_DELAY);
    else if(mov[0]=='L')
         rotateLeft(mov),delay(MOVE_DELAY);
    else if(mov[0]=='F')
         rotateForward(mov),delay(MOVE_DELAY);
    else if(mov[0]=='B')
         rotateBack(mov),delay(MOVE_DELAY);
   }  
   //while(1);
   ///////// finally the cube is Solved ////////////
}
