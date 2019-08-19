const int sensor = A0;
const int n = 500;
int i=0,j=0;
int x[]={0,0,0,0,0};
float m=0;
int n_analogos=0,espera=500,listo=1;
int led = 13;
void setup(){
  pinMode(led,OUTPUT);
  digitalWrite(led,0);
	Serial.begin(9600); 
  while(listo){
	if (Serial.available()>0){
	n_analogos = Serial.read();
	Serial.print(n_analogos);
	}
 if( n_analogos>48 && n_analogos<55){
    n_analogos=n_analogos-48;
    listo=0;
    digitalWrite(led,1);
  }
  }
}
void loop(){
	for (i=0;i<n_analogos; i++){
		switch (i){
			case (0):
				x[0]=analogRead(A0);
			break;
			case (1):
				x[1]=analogRead(A1);
			break;
			case (2):
				x[2]=analogRead(A2);
			break;
			case (3):
				x[3]=analogRead(A3);
			break;
			case (4):
				x[4]=analogRead(A4);
			break;
			case (5):
				x[5]=analogRead(A5);
			break;
		}
	}
	for (i=0; i<n_analogos; i++){
		Serial.print(x[i]);
	}
	Serial.print("*");
	delay(espera);
}
