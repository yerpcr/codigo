
int t =1000;

void setup(){
	pinMode(13,OUTPUT);

}

void loop(){
	digitalWrite(13,1);
	delay(t);
	digitalWrite(13,0);
	delay(t);
}
