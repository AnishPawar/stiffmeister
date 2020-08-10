#include<Keypad.h>
const int ROW = 4;
const int COLUMN = 4;

char keys[ROW][COLUMN] = {{'1','2','3','A'},
                          {'4','5','6','B'},
                          {'7','8','9','C'},
                          {'*','0','#','D'}};

byte pin_row[ROW] = {9,8,7,6};
byte pin_column[COLUMN] = {5,4,3,2};

Keypad keypad = Keypad( makeKeymap(keys),pin_row,pin_column,ROW,COLUMN);

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  char key = keypad.getKey();
  if (key)
    Serial.println(key);
}
