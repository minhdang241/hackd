from dis import dis
def produce(i):
  yield i * i
def main():
  v = produce(0)
  print(v)
print("produce: ")
dis(produce)
#test()
print("main: ")
dis(main)
