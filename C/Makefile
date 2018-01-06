C = gcc
TARGET = main
DEP = hex_to_base64.o fixed_xor.o single_byte_xor.o

run: $(TARGET).o $(DEP)
	$(CC) $(TARGET).o $(DEP) -o main

main.o: $(TARGET).c modules.h
	$(CC) -c $(TARGET).c

hex_to_base64.o: hex_to_base64.c modules.h
	$(CC) -c hex_to_base64.c

fixed_xor.o: fixed_xor.c modules.h
	$(CC) -c fixed_xor.c

single_byte_xor.o: single_byte_xor.c modules.h
	$(CC) -c single_byte_xor.c

clean:
	$(RM) $(TARGET) *.o
