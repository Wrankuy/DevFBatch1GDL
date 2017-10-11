int a=0;
int b=1;
int c=2;
int d=3;
int e=4;
int f=5;
int g=6;
/*
int azul=8,
int verde=9;
int rojo=10;
*/
int q=13;
int r=12;
int s=11;
void setup() {
  // put your setup code here, to run once:
/*
  pinMode(azul,OUTPUT);
  pinMode(verde,OUTPUT);
  pinMode(rojo,OUTPUT);
 */
  pinMode(a,OUTPUT);
  pinMode(b,OUTPUT);
  pinMode(c,OUTPUT);
  pinMode(d,OUTPUT);
  pinMode(e,OUTPUT);
  pinMode(f,OUTPUT);
  pinMode(g,OUTPUT);
 
  pinMode(q,INPUT);
  pinMode(r,INPUT);
  pinMode(s,INPUT);

 
}
void loop() {
   if(q==0 && r==0 && s==1){
    
    
  digitalWrite(g,HIGH);
  digitalWrite(b,HIGH);
  digitalWrite(c,HIGH);
  digitalWrite(e,HIGH);
  digitalWrite(f,HIGH);
  digitalWrite(a,LOW);
  digitalWrite(d,LOW);
  delay(2000);
    
  digitalWrite(g,LOW);
  digitalWrite(b,HIGH);
  digitalWrite(c,HIGH);
  digitalWrite(e,HIGH);
  digitalWrite(f,HIGH);
  digitalWrite(a,HIGH);
  digitalWrite(d,HIGH);
  delay(2000);
  
  digitalWrite(g,LOW);
  digitalWrite(b,LOW);
  digitalWrite(c,LOW);
  digitalWrite(e,HIGH);
  digitalWrite(f,HIGH);
  digitalWrite(a,LOW);
  digitalWrite(d,HIGH);
  delay(2000);
  
  digitalWrite(g,HIGH);
  digitalWrite(b,HIGH);
  digitalWrite(c,HIGH);
  digitalWrite(e,HIGH);
  digitalWrite(f,HIGH);
  digitalWrite(a,HIGH);
  digitalWrite(d,LOW);
  delay(2000);

     }
    
    

/*  if(){
    digitalWrite(rojo,HIGH); 
    digitalWrite(rojo,HIGH);
    digitalWrite(rojo,HIGH);
    
    }
*/
}

