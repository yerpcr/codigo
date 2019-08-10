const int sensor = A0;
const int n = 500;
int i=0;
double x=0;
float m=0;
void setup(){
	Serial.begin(9600);
		
}
void loop(){
	m=0;
	for (i=0;i<n; i++){
		x = analogRead(sensor);
		m = x+m;
	}
	
	Serial.println(m/n);

}
