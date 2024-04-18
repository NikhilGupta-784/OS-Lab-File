#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void child_function() {
    // Child process code
    pid_t child_pid = getpid();
    printf("Child process %d is running.\n", child_pid);
    sleep(3);
    printf("Child process %d is terminating.\n", child_pid);
}

int main() {
    // Main process code
    printf("Main process is running.\n");

    // Create a child process
    pid_t child_pid = fork();

    if (child_pid == -1) {
        // Fork failed
        perror("Fork failed");
        exit(EXIT_FAILURE);
    }

    if (child_pid == 0) {
        // This code runs in the child process
        child_function();
        exit(EXIT_SUCCESS);
    } else {
        // This code runs in the parent process

        // Do some work in the main process
        sleep(1);
        printf("Main process is doing some work.\n");

        // Wait for the child process to finish
        int status;
        waitpid(child_pid, &status, 0);

        if (WIFEXITED(status)) {
            // Child process terminated normally
            printf("Child process exited with status %d.\n", WEXITSTATUS(status));
        } else {
            // Child process terminated abnormally
            printf("Child process terminated abnormally.\n");
        }

        printf("Main process is done.\n");
    }

    return 0;
}