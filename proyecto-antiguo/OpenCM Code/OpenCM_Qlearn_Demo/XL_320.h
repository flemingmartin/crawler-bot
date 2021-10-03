/*  
	Title: XL_320_Defines.h
	Author: Jordan Miller
	Description: Contains all the defines for the ROBOTIS XL 320 Servo EEPROM and RAM.
				 More information at: http://support.robotis.com/en/product/actuator/dynamixel_x/xl_series/xl-320.htm
*/

#ifndef XL_320_h
#define XL_320_h

// the #include statment and code go here...


//------------------------------EEPROM------------------------------------------------//

#define MODEL_NUMBER 				0   //  R-  2 bytes
#define FIRMWARE	 				2   //  R-  1 byte
#define SERVO_ID	 				3   //  RW  1 byte
#define BAUD						4   //  RW  1 byte
#define RETURN_DELAY				5   //  RW  1 byte
#define CW_ANGLE_LIMIT				6   //  RW  2 bytes
#define CCW_ANGLE_LIMIT				8   //  RW  2 bytes
#define CONTROL_MODE	    		11  //  RW  1 byte
#define LIMIT_TEMP  				12  //  RW  1 byte
#define LOWER_VOLTAGE				13  //  RW  1 byte
#define UPPER_VOLTAGE				14  //  RW  1 byte
#define MAX_TORQUE					15  //  RW  2 bytes
#define RETURN_LEVEL				17  //  RW  1 byte
#define ALARM_SHUTDOWN				18  //  RW  1 byte

//------------------------------RAM--------------------------------------------------//
#define TORQUE_ENABLE				24  //  RW  1 byte
#define LED			 				25  //  RW  1 byte
#define D_GAIN	 					27  //  RW  1 byte
#define I_GAIN						28  //  RW  1 byte
#define P_GAIN						29  //  RW  1 byte
#define GOAL_POSITION				30  //  RW  2 bytes
#define GOAL_VELOCITY				32  //  RW  2 bytes
#define GOAL_TORQUE	    			35  //  RW  2 bytes
#define CURRENT_POSITION  			37  //  R-  2 bytes
#define CURRENT_SPEED				39  //  R-  2 bytes
#define CURRENT_LOAD				41  //  R-  2 bytes
#define CURRENT_VOLTAGE				45  //  R-  1 byte
#define CURRENT_TEMP			 	46  //  R-  1 byte
#define REGISTERED_INSTRUCTION		47  //  R-  1 byte
#define MOVING						49  //  R-  1 byte
#define HARDWARE_ERROR				50  //  R-  1 byte
#define PUNCH						51  //  RW  2 bytes

//-----------------------------MISC--------------------------------------------------//

#endif
