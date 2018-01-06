/*
  Author: Abraham Adberstein
  Date: May 16, 2016
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include "modules.h"

int binary_to_decimal(char *bin);

char *hex_to_base64(char *string){
  //Get length of string, and the number of groups of 6 bits.
  int STRING_LEN = strlen(string);
  int binLen = STRING_LEN * 4;
  char binaryString[binLen+1];
  //extra digits if they do not make a group of 6, get the length of base64 string
  int extraDigits = binLen % 6;
  int enWordLen = (binLen/6) + extraDigits + 1;
  char encodedWord[enWordLen];

  int i, count = 0;

  char base63[64] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1','2', '3', '4','5','6','7','8','9','+', '\\' };

  //convert each hex to binary
  for (i = 0; i < STRING_LEN; i++){
    char z[STRING_LEN];
    switch(string[i]){
               case '0': strcpy(z,"0000"); break;
               case '1': strcpy(z,"0001"); break;
               case '2': strcpy(z,"0010"); break;
               case '3': strcpy(z,"0011"); break;
               case '4': strcpy(z,"0100"); break;
               case '5': strcpy(z,"0101"); break;
               case '6': strcpy(z,"0110"); break;
               case '7': strcpy(z,"0111"); break;
               case '8': strcpy(z,"1000"); break;
               case '9': strcpy(z,"1001"); break;
               case 'a': strcpy(z,"1010"); break;
               case 'b': strcpy(z,"1011"); break;
               case 'c': strcpy(z,"1100"); break;
               case 'd': strcpy(z,"1101"); break;
               case 'e': strcpy(z,"1110"); break;
               case 'f': strcpy(z,"1111"); break;
               default: printf("nothing here\n"); break;
    }
    if ( i == 0 ){
      strcpy(binaryString, z);
    }
    else{
      strcat(binaryString, z);
    }
  }
  //group every 6 bits
  for(i = 0; i < enWordLen; i++){
    char substr[7];
    int digits = 6;

    if (i == (binLen/6) )
      digits = extraDigits;

    if (digits == 0)
      break;

    strncpy(substr, binaryString+i*6, digits);
    //every 6 bits convert to decimal
    int num = binary_to_decimal(substr);
    //from decimal to base64
    encodedWord[count] = base63[num];
    count++;
  }

  //make string
  encodedWord[enWordLen] = '\0';

  //return result
  char *result = malloc(enWordLen);
  strcpy(result, encodedWord);

  return result;

}

int binary_to_decimal(char *bin){
  int num = 0, i;
  int len = strlen(bin);
  for (i = 0; i < len; i++){
    if ( bin[i] == '1')
      num += pow(2, len-1-i);
  }
  return num;
}
