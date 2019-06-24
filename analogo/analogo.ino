int i=0;
void setup(){
	Serial.begin(9600);
	
}
void loop(){
	
	Serial.println("Hola");
	Serial.println(i);
	i=i+1;
	if (i>253){
		i=0;
	}
	delay(500);

}
