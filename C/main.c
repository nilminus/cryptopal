/*
  Author: Abraham Adberstein
  Date: May 16, 2016
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
// #include "modules.h"


int main(int argc, char** argv){
  char *cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";

	printf("The solution is\t\n%s\n", single_byte_xor(cipher));
}
