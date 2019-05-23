#include <iostream>
#include <fstream>

using namespace std;

const float dt=0.1;
const float m=7294.29;
const float q=2;

float ax(float t);
float ay(float t);

int main(){
    float t=0;
    float x=1;
    float y=0;
    float vx=0;
    float vy=1;
    
    ofstream outfile;
    outfile.open("datos.txt");
    
    outfile<<t<<' '<<x<<' '<<y<<endl;
    for(t=0; t<10; t=t+dt){
        vx=vx+dt*ax(t);
        x=x+dt*vx;
        
        double f0,f1,f2,f3;
        
        f0=ay(t);
        f1=ay(t + dt/2);
        f2=ay(t + dt/2);
        f3=ay(t + dt);
        
        vy=vy+dt*(f0+2*f1+2*f2+2*f3)/6;
        y=y+vy*dt;
        
        outfile<<t<<' '<<x<<' '<<y<<endl;
    }
    
    outfile.close();
}

float ax(float t){
    return 0.0;
}
float ay(float t){
    float respuesta=0.0;
    if(t>3 && t<7){
        respuesta=3.0;
    }
    
    return q*respuesta/m;
}
