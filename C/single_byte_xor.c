/*
  Author: Abraham Adberstein
  Date: May 16, 2016
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "modules.h"

void single_byte_xor(char *hexString){
  int elements = 64;
  //char hex[16] = {'0','1','2', '3', '4','5','6','7','8','9', 'a', 'b', 'c', 'd', 'e', 'f'};
  char hex[64] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0','1','2', '3', '4','5','6','7','8','9' };

  int length = strlen(hexString);
  int i, j;

  for ( i = 0; i < elements; i++){
    char buffer[length];
    char letter = hex[i];

    if ( letter >= 64 || letter <= 90){
      for ( j = 0; j < length; j+=2){
          int num = (int)letter;
          buffer[j] = (num/10) + '0';
          buffer[j+1] = (num - (num/10)*10) + '0';
      }
    }
    else {
      for ( j = 0; j < length; j++)
          buffer[j] = letter;
    }

    buffer[length] = '\0';

    //xor string
    char *result = fixed_xor(hexString, buffer);
    printf("Character used: %c\n", letter);
    printf("buffer 1: %s\nbuffer 2: %s\n", buffer, hexString);
    printf("%s\n\n", result );
    //printf("Hex: %s\n\n", result );

  }
}
