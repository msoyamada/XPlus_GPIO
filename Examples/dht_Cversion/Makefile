PROJ=dht
CC=gcc
SRC=dht.c
LIBS=-lgpiod
CFLAGS=-O3 -D CONSUMER=\"$(PROJ)\"  

all:
	$(CC) $(SRC) $(LIBS) $(CFLAGS) -o $(PROJ)

clean:
	rm $(PROJ)
