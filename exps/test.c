#include <stdio.h>
#include <string.h>
#include <assert.h>
#define NCPU 1
int syscall1(void);
int syscall2(void);
int main(void) {

  // aligned => the address should be divided by 32
  __attribute__((aligned (32))) char stack[4096 * NCPU];
  //char stack[4096 * NCPU];
  printf("address of the array should be divided by 16: %ld\n", (long) stack);
  
  // array of funciton pointer
  int (*syscalls[])(void) =  {
    [1] = syscall1,
    [2] = syscall2,
  };
  printf("address of the function pointer array: %ld\n", (long) syscalls);
  return 0;

  // memset function
  memset(stack, 1, 4096 * NCPU);
  assert(*stack == 1);

}

int syscall1(void) {
  return 1;
}
int syscall2(void) {
  return 2;
}
