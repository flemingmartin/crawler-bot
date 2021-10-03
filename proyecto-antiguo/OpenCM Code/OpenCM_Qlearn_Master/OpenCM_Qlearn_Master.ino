/* 
  Title: OpenCM_ctrl
  Author: Jordan Miller
  Description: This is the main code for the OpenCM side of the control
   for the crawler bot. It initializes the serial connection, waits for a command and 
   then updates the servo positions and returns success code if servo positions are acheived. 
   If the servo position is not acheived, it returns the servos to neutral and sends the 
   failure code back to the Raspberry Pi.
   
  Actions:
   _______  
  |   1   |
  |4     3|
  |___2___|

  The command protocol between Pi and OpenCM is as follows:  
   Command(CMD) is sent from Pi to OpenCM. 
   Answer(ANS) sent from OpenCM to Raspberry Pi.
   |CMD|_________________________Description____________________________        |ANS|_________________________Description____________________________

   
  References:
   Dynamixel SDK API Reference: http://support.robotis.com/en/software/dynamixel_sdk/api_reference.htm
   XL_320 Documentation:        http://support.robotis.com/en/product/actuator/dynamixel_x/xl_series/xl-320.htm
*/

//include Libraries
#include <string.h>

//include Files
#include "XL_320.h"
#include "QuadEncoder.h"

//define IDs for servos 
#define SHOULDER    1
#define ELBOW       2
#define SHOULDER_OFFSET      400
#define ELBOW_OFFSET         300
#define ENC_A       12                 //Uncomment to make it go toward leg
#define ENC_B       10
//#define ENC_A       10               //Uncomment to make it move towards wheels
//#define ENC_B       12
#define POS_THRESHOLD 30
#define NEG_THRESHOLD -30
#define ROW_NUM        4
#define COL_NUM        4


//declare objects
Dynamixel Dxl(1); 
QuadEncoder Enc(ENC_A, ENC_B);

//declare GLOBAL variables
int S[2] = {0, 0};
int state; 
char cmdFound = 0;
char temp = 0;
char incoming[100];
int strIndex = 0;
int position = 0;
int SH_ROT_SCALE, ELB_ROT_SCALE;
int Reward = 0;

void setup(){
    //initialize servo bus
    Dxl.begin(2);
    
    //initialize all variables
    Serial3.begin(9600);//initialize serial to pi
    
    //initialize serial to USB
    SerialUSB.begin();
    SH_ROT_SCALE = SHOULDER_OFFSET/ROW_NUM;
    ELB_ROT_SCALE = ELBOW_OFFSET/COL_NUM;
    
    //initialize servos
    Dxl.jointMode(SHOULDER); //jointMode() is to use position mode
    Dxl.jointMode(ELBOW); //jointMode() is to use position mode
    ZeroServos();
}

void loop()
{
   if (Serial3.available()){
    temp = Serial3.read();
    SerialUSB.print(temp);
    if(temp == '\n'){
      cmdFound = 1;
      incoming[strIndex] = '\0';
      strIndex = 0;
    }
    else{
      incoming[strIndex] = temp;
      strIndex++;
    } 
   }
   if(cmdFound){
      if(strcmp(incoming,"up")==0){
//          Serial3.print("OpenCM got: ");
//          Serial3.println(incoming);
          if((S[0]-1) >= 0){
            S[0]=S[0]-1; 
            position = Enc.pos();
            Dxl.writeWord(SHOULDER, GOAL_POSITION, SHOULDER_OFFSET-SH_ROT_SCALE*(S[0]));
            while(Dxl.readByte(SHOULDER, MOVING));
            Reward = position - Enc.pos();
          }
          // Measure the Reward
          Serial3.print(Reward);
          
          SerialUSB.print(S[0]); SerialUSB.println(S[1]);
      }
      else if(strcmp(incoming,"down")==0){
//          Serial3.print("OpenCM got: ");
//          Serial3.println(incoming);
          if((S[0]+1) < ROW_NUM){
            S[0]=S[0]+1; 
            position = Enc.pos();
            Dxl.writeWord(SHOULDER, GOAL_POSITION, SHOULDER_OFFSET-SH_ROT_SCALE*(S[0]));
            while(Dxl.readByte(SHOULDER, MOVING));
            Reward = position - Enc.pos();
          }
          // Measure the Reward
          Serial3.print(Reward);
          SerialUSB.print(S[0]); SerialUSB.println(S[1]);
      }
      else if(strcmp(incoming,"left")==0){
//          Serial3.print("OpenCM got: ");
//          Serial3.println(incoming);
          if((S[1]-1) >= 0){
            S[1]=S[1]-1; 
            position = Enc.pos();
            Dxl.writeWord(ELBOW, GOAL_POSITION, ELBOW_OFFSET-ELB_ROT_SCALE*(S[1]));
            while(Dxl.readByte(ELBOW, MOVING));
            Reward = position - Enc.pos();
          }
          // Measure the Reward
          Serial3.print(Reward);
          SerialUSB.print(S[0]); SerialUSB.println(S[1]);
      }
      else if(strcmp(incoming,"right")==0){
//          Serial3.print("OpenCM got: ");
//          Serial3.println(incoming);
          if((S[1]+1) < COL_NUM){
            S[1]=S[1]+1; 
            position = Enc.pos();
            Dxl.writeWord(ELBOW, GOAL_POSITION, ELBOW_OFFSET-ELB_ROT_SCALE*(S[1]));
            while(Dxl.readByte(ELBOW, MOVING));
            Reward = position - Enc.pos();
          }
          // Measure the Reward
          Serial3.print(Reward);
          SerialUSB.print(S[0]); SerialUSB.println(S[1]);
      }
      else if(strcmp(incoming,"zero")==0){
          ZeroServos();
          S={0,0};
          SerialUSB.print(S[0]); SerialUSB.println(S[1]);
      }
       else{
          Serial3.print("OpenCM got: ");
          Serial3.println(incoming);
          Serial3.println("That command does nothing");
       } 
       

    cmdFound = 0;
    Serial3.flush();
   }
   
}

void ZeroServos(){
    Dxl.writeWord(SHOULDER, GOAL_POSITION, SHOULDER_OFFSET);           //set all servos to zero position
    Dxl.writeWord(ELBOW, GOAL_POSITION, ELBOW_OFFSET);           //set all servos to zero position
}


