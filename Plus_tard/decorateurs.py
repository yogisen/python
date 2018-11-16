import time

def time_it(function_to_wrap):
  def _wrapper():
    debut = time.time()
    function_to_wrap()
    print("Exec time : {} ms".format(time.time() - debut))
  return _wrapper

@time_it
def show_numbers():
  for i in range(1000):
    print(i)

show_numbers()



------------------------------------------------------------------------

import time

def time_it(function_to_wrap):
  def _wrapper():
    debut = time.time()
    function_to_wrap()
    print("Exec time : {} ms".format(time.time() - debut))
  return _wrapper

def show_numbers():
  for i in range(1000):
    print(i)

show_numbers = time_it(show_numbers)
show_numbers()