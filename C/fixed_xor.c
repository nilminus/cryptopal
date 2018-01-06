/*
  Author: Abraham Adberstein
  Date: May 16, 2016
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "modules.h"

char *fixed_xor(char *buffer1, char *buffer2){

  //get length of buffers
  int length = strlen(buffer1);
  char result[length];
  int i, b1, b2;

  for (i = 0; i < length; i++){

    //substract '0' which is 48
    b1 = buffer1[i] - '0';
    b2 = buffer2[i] - '0';

    //if bigger than 49 it means it is not within [0-9] 49 - x = 10
    if ( b1 >= 10 )
      b1 -= 39;

    if ( b2 >= 10 )
      b2 -= 39;

    // xor the bytes and encode to hex again
    int hexNumber = (b1 ^ b2);
    char encodeCharater = hexNumber + '0';

    //if bigger tahn 57 add padding to reach corresponding ascii characters
    if (encodeCharater > 57)
      encodeCharater += 39;

    result[i] =  encodeCharater;
  }

  //add null bit to string
  result[length] = '\0';

  //return result, weird warning at the end for some reason
  char *res = malloc(length);
  strcpy(res, result);

  return res;
}
