int i=0;
void setup(){
	Serial.begin(9600);
}
void loop(){
	
  i=analogRead(A0);
  delay(10);
  Serial.println(i);

}
