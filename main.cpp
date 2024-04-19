#include <iostream>
using namespace std;


class A1
{
protected:
    int a1;
public:
    A1(int V1 = 0) {a1 = V1;cout<<"\nClass A1 constructor";}
    virtual void print() const {cout <<"\nVariable of A1 class";}
    virtual void show() const {cout <<"\na1 = " <<a1;}
};

class  A2
{
protected:
    int a2;
public:
    A2(int V1 = 0) {a2 = V1;cout<<"\nClass A2 constructor";}
    virtual void print() const {cout <<"\nVariable of A2 class";}
    virtual void show() const {cout <<"\na1 = " <<a2;}
};

class A3
{
protected:
    int a3;
public:
    A3(int V1 = 0) {a3 = V1;cout<<"\nClass A3 constructor";}
    virtual void print() const {cout <<"\nVariable of A3 class";}
    virtual void show() const {cout <<"\na1 = " <<a3;}
};

class B1: virtual public A1, virtual public A2, virtual public A3
{
protected:
    int b1;
public:
    B1(int V1 = 0, int V2 = 0, int V3 = 0, int V4 = 0) : A1(V2), A2(V3), A3(V4) {b1 = V1; cout <<"\nClass B1 constructor";}
    virtual void print() const {cout <<"\nVariable of B1 class";}
    virtual void show() const {cout <<"\nb1 = " <<b1  <<"\na1 = " <<a1 <<"\na2 = " <<a2 <<"\na3 = " <<a3;}

};

class B2: virtual public A1, virtual public A2, virtual public A3
{
protected:
    int b2;
public:
    B2(int V1 = 0, int V2 = 0, int V3 = 0, int V4 = 0) : A1(V2), A2(V3), A3(V4) {b2 = V1; cout <<"\nClass B2 constructor";}
    virtual void print() const {cout <<"\nVariable of B1 class";}
    virtual void show() const {cout <<"\nb2 = " <<b2  <<"\na1 = " <<a1 <<"\na2 = " <<a2 <<"\na3 = " <<a3;}

};

class B3: virtual public A1, virtual public A2, virtual public A3
{
protected:
    int b3;
public:
    B3(int V1 = 0, int V2 = 0, int V3 = 0, int V4 = 0) : A1(V2), A2(V3), A3(V4) {b3 = V1; cout <<"\nClass B3 constructor";}
    virtual void print() const {cout <<"\nVariable of B1 class";}
    virtual void show() const {cout <<"\nb3 = " <<b3  <<"\na1 = " <<a1 <<"\na2 = " <<a2 <<"\na3 = " <<a3;}

};

class C1: virtual public B1, virtual public B2, virtual public B3
{
protected:
    int c1;
public:
    C1(int V1 = 0, int V2 = 0, int V3 = 0, int V4 = 0, int V5 = 0, int V6 = 0, int V7 = 0) : A1(V2), A2(V3), A3(V4), B1(V5), B2(V6),B3(V7) {c1 = V1; cout <<"\nClass C1 constructor";}
    virtual void print() const {cout <<"\nVariable of C1 class";}
    virtual void show() const {cout <<"\nc1 = " <<c1 << "\nb1 = " << b1 << "\nb2 = " << b2 <<"\nb3 = " << b3 <<"\na1 = " <<a1 <<"\na2 = " <<a2 <<"\na3 = " <<a3;}

};


int main()
{


        C1 test(1,2,3,4,5,6,7);
        test.show();
        test.print();
        A1* ptr = &test; ptr -> show(); ptr ->print();

}
