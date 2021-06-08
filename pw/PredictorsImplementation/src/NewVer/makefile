#Makefile

# Definition des constantes
CC = gcc
CFLAGS = -ansi -Wall
LDFLAGS = -lm
OBJFILES = MinMax.o Graphs.o
TARGET = MinMax

# Definition des commandes a effectuer
$(TARGET) : $(OBJFILES)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJFILES) $(LDFLAGS)


# Définition des commandes à appeler
install : $(TARGET)
	make clean

# Définition des commandes de nettoyage
clean :
	rm -f *.o

mrproper : clean
	rm -f $(EXEC)
