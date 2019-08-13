#include "common.h"

int main(int argc, char const *argv[])
{
	if (access(FIFO, F_OK)) {
		mkfifo(FIFO, 0644);
	}

	int fifo = open(FIFO, O_WRONLY); // 只写的方式打开FIFO
	
	char msg[20];
	memset(msg, 0, 20);

	fgets(msg, 20, stdin);
	int n = write(fifo, msg, strlen(msg));
	printf("sebded %d bytes to FIFO\n", n);
	
	return 0;
}