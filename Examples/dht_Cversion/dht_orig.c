
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <dirent.h>
#include <fcntl.h>
#include <assert.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <unistd.h>
#include <gpiod.h>

#define MAXTIMINGS 100

#ifndef	CONSUMER
#define	CONSUMER	"Consumer"
#endif


//#define DEBUG
#define HIGH 1
#define LOW 0
#define DHT11 11
#define DHT22 22
#define AM2302 22

int readDHT(int type, struct gpiod_line *pin);

int main(int argc, char **argv)
{
	char *chipname = "gpiochip1";
	unsigned int line_num = 9;	// GPIO Pin #32
	int val;
	struct gpiod_chip *chip;
	struct gpiod_line *line;
	int i, ret;


/*	ret = gpiod_line_request_input(line, CONSUMER);
	if (ret < 0) {
		perror("Request line as input failed\n");
		goto release_line;
	}
*/

  if (argc != 3) {
	printf("usage: %s [11|22|2302] GPIOpin#\n", argv[0]);
	printf("example: %s 2302 4 - Read from an AM2302 connected to GPIO #4\n", argv[0]);
	return 2;
  }
  int type = 0;
  if (strcmp(argv[1], "11") == 0) type = DHT11;
  if (strcmp(argv[1], "22") == 0) type = DHT22;
  if (strcmp(argv[1], "2302") == 0) type = AM2302;
  if (type == 0) {
	printf("Select 11, 22, 2302 as type!\n");
	return 3;
  }

  line_num = atoi(argv[2]);

  if (line_num <= 0) {
	printf("Please select a valid GPIO pin #\n");
	return 3;
  }

  chip = gpiod_chip_open_by_name(chipname);
  if (!chip) {
 	perror("Open chip failed\n");
 	exit(1);
  }

  line = gpiod_chip_get_line(chip, line_num);
  if (!line) {
 	perror("Get line failed\n");
	exit(1);
   }



  printf("Using pin #%d\n", line_num);

  while (1) {
     readDHT(type, line);
     sleep(4);
  }
  return 0;

} // main


int bits[250], data[100];
int bitidx = 0;


void setPinModeOutput(struct gpiod_line *line){
	int ret = gpiod_line_request_output(line, CONSUMER, 1);
	if (ret < 0) {
		perror("Request line as output failed\n");
		exit(1);
	}
}

void setPinModeInput(struct gpiod_line *line){
	int ret = gpiod_line_request_input(line, CONSUMER);
	if (ret < 0) {
		perror("Request line as input failed\n");
		exit(1);
	}
}

void gpio_write(struct gpiod_line *line,  int val){
     int ret = gpiod_line_set_value(line, val);
     if (ret < 0) {
	perror("Set line output failed\n");
	exit(1);
     }
}




int gpio_read(struct gpiod_line *line){
     int val = gpiod_line_get_value(line);
     if (val < 0) {
	perror("Read line input failed\n");
        exit(1);
     }
     return val;
}

#define COUNT 1000  //before 1000
#define BIT1 50


int readDHT(int type, struct gpiod_line *pin) {
  int counter = 0;
  int laststate = HIGH;
  int j=0;

  // Set GPIO pin to output
  setPinModeOutput(pin);


  gpio_write(pin, HIGH);
  usleep(500000);  // 500 ms
  gpio_write(pin, LOW);
  usleep(20000);

  gpiod_line_release(pin);


  setPinModeInput(pin);

  data[0] = data[1] = data[2] = data[3] = data[4] = 0;

  // wait for pin to drop?
/*  counter= 0;
  while (gpio_read(pin) == 1) {
//    usleep(1);
      counter++;
      if (counter > 1000000) {
        printf("Ops, blocked ");
	break;

      }
  }
 */
  usleep(30); 

  // read data!
  for (int i=0; i< MAXTIMINGS; i++) {
    counter = 0;
    while ( gpio_read(pin) == laststate) {
	counter++;
	//nanosleep(1);		// overclocking might change this?
        if (counter == COUNT)
	  break;
    }
    laststate = gpio_read(pin);
    if (counter == COUNT) break;
    bits[bitidx++] = counter;

    if ((i>3) && (i%2 == 0)) {
      // shove each bit into the storage bytes
      data[j/8] <<= 1;
      if (counter > BIT1)
        data[j/8] |= 1;
      j++;
    }
  }


#ifdef DEBUG
  for (int i=3; i<bitidx; i+=2) {
    printf("bit %d: %d\n", i-3, bits[i]);
    printf("bit %d: %d (%d)\n", i-2, bits[i+1], bits[i+1] > 200);
  }
#endif

  printf("Data (%d): 0x%x 0x%x 0x%x 0x%x 0x%x\n", j, data[0], data[1], data[2], data[3], data[4]);

  if ((j >= 38) ) {
     // yay!
     if (type == DHT11)
	printf("Temp = %d *C, Hum = %d \%\n", data[2], data[0]);
     if (type == DHT22) {
	float f, h;
	h = data[0] * 256 + data[1];
	h /= 10;

	f = (data[2] & 0x7F)* 256 + data[3];
        f /= 10.0;
        if (data[2] & 0x80)  f *= -1;
	printf("Temp =  %.1f *C, Hum = %.1f \%\n", f, h);
    }
  }
  if (data[4] == ((data[0] + data[1] + data[2] + data[3]) & 0xFF))  {
     printf("Checksum ok \n");
  }else {
     printf("Checksum failed \n");

  }

  gpiod_line_release(pin);

 // return 0;
}
