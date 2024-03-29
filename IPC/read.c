#include "common.h"

int main(int argc, char const *argv[])
{
	if (access(FIFO, F_OK)) {
		mkfifo(FIFO, 0644);
	}

	int fifo = open(FIFO, O_RDONLY); // 只读的方式打开FIFO
	
	char msg[20];
	memset(msg, 0, 20);

	read(fifo, msg, 20);
	printf("read from FIFO: %s\n", msg);
	
	return 0;
}