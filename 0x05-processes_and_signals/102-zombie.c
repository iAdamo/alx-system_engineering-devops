#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * infinite_while - creates 5 zombie processes
 *
 * Return: PID
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main entry
 *
 * Return: 0 on success
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
			continue;
		else if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: ZOMBIE_PID: %d\n", pid);
	}
	infinite_while();

	return (0);
}
