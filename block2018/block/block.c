#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int f1(int v1, int v2, float f1) {
  int s = v1 + (int)f1;
  if (s < 2) {
    s = 2;
  } 
  else {    
    s =  1 - v2;
    return v1;
  }
  s = 12 - v1;

  return s;
}

int main()
{
  // double a = 0.0, b = 0.0, c = 1.0, d = 0.0;

  // d = 1.2;
  // // a = a - b / (c-d) * c;
  // a = d + b / c * 2 - 2;
  // int q = 0, s = 0, r = 0;
  // q = s + r;
  // printf("%f", a);
  // char * w = malloc(sizeof w * 255);
  // w = "asdassss";
  // w = "qwe";
  // strcpy(w,"qwe2");
  // printf("%s", w);
  // scanf("%s", w);
  int w = 1;
  //   if (w < 2) {
  //   w = 2;
  // } 
  // else {    
  //   w =  1 - w ;
  // }
  int i= 0;
  for (i = 0; i < w; ++i) {
    float s = 123;
    printf("%d %f", w, s);
  }
  int s = f1(1,w, 3);
  printf("%d", s);
}
