String indata="",read_String="";
const int n = 200;
int i=0,j=0,k=0;
int x[]={0,0,0,0,0};
float m=0;
int n_analogos=0,q,espera=500,listo=1;
int led = 13;
char c;
int habilitar = 2;
void setup(){
  pinMode(led,OUTPUT);
  pinMode(habilitar,OUTPUT);
  digitalWrite(led,0);
  digitalWrite(habilitar,0);
	Serial.begin(2400); 
  while(listo){
    read_String="";
    digitalWrite(habilitar,0);
    while (!Serial.available()) {}
	  digitalWrite(led,1);
	  while (Serial.available()) // this will be skipped if no data present, leading to
                             // the code sitting in the delay function below
    {
      delay(30);  //delay to allow buffer to fill 
      if (Serial.available() >0)
      {
        c = Serial.read();  //gets one byte from serial buffer
        read_String+= c;
         c=0;
      }
    }
    digitalWrite(led,0);
    digitalWrite(habilitar,1);
    Serial.println(read_String);
    if (read_String=="1")n_analogos=1;
    if (read_String=="2")n_analogos=2;
    if (read_String=="3")n_analogos=3;
    if (read_String=="4")n_analogos=4;
    if (read_String=="5")n_analogos=5;
    if (read_String=="6")n_analogos=6;
    if(n_analogos>0&&n_analogos<7){
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
		Serial.println(x[i]);
	}
	Serial.println("*");
	delay(espera);
}
