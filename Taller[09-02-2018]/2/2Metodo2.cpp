#include <math.h>
#include<iostream>

using namespace std;

int main()
{
    int largo=32;
    
    int ancho=24;
    
    int numCort=2;
    
    int v[10];
    
    v[0]=largo*ancho;
    v[1]=largo*numCort;
    v[1]=v[1]+(ancho*numCort);
    v[2]=numCort*numCort;
    
    cout<<"V=";
    for(int i=0;i<3;i++){
        
        cout<<v[i]<<"x^"<<i+1;
        if(i<2){
            cout<<"+";
        }

    }
    cout<<endl;
    
    v[2]=v[2]*3;
    v[1]=v[1]*2;
    v[0]=v[0]*1;


    cout<<"Deriva V"<<endl;
    cout<<"V=";
    for(int i=0;i<3;i++){
        
        cout<<v[i];
        if(i>0){
            cout<<"x^"<<i;
        }
        
        if(i<2){
            cout<<"+";
        }

    }
    cout<<endl;
    cout<<"Ecuacion cuadratica para 2 respuestas"<<endl;
    
    cout<<"x=("<<v[1]<<"+-sqrt("<<v[1]<<"^2+"<<4<<"("<<v[2]<<")"<<"("<<v[0]<<")"<<")"<<")/"<<2<<"*"<<v[2];
    cout<<endl;
    cout<<"(28+-sqrt(208))/(3) x simplificado";
    cout<<endl;
    cout<<(28+sqrt(208))/(3);
    cout<<endl;
    cout<<(28-sqrt(208))/(3);
    return 0;
}
