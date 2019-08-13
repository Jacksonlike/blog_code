OBJ := write read
CFLAGS := -Wall

all:$(OBJ)
	
$(OBJ):%:%.c
	$(CC) $^ -o $@ $(CFLAGS)

clean:
	$(RM) $(OBJ)