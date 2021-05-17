#Makefile

# Definition des constantes
CC = gcc
CFLAGS = -ansi -Wall

# Definition des commandes a effectuer
MinMax : MinMax.c
	$(CC) -o $@ $^ $(CFLAGS)
	$(CC) -S -o $@.s $^ $(CFLAGS)

Exponentiation : Exponentiation.c
	$(CC) -o $@ $^ $(CFLAGS)
	$(CC) -S -o $@.s $^ $(CFLAGS)

Dichotomie : Dichotomie.c
	$(CC) -o $@ $^ $(CFLAGS)
	$(CC) -S -o $@.s $^ $(CFLAGS)

# Définition des commandes de nettoyage
clean :
	rm -f *.o

mrproper : clean
	rm -f $(EXEC)


# Définition des commandes à appeler
install : MinMax Exponentiation Dichotomie

uninstall : mrproper
	rm -f ../bin/$(EXEC)
	rm -rf ../bin
