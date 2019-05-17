import time
import voltage
import swirl
import motion
import led
import something

# motion.test()
led.on()

i = 0
while True:
  swirl.next(i)
  if something.is_infront():
    print('Turning...')
    motion.turn_right(90)
  else:
    print('Starting...')
    motion.forward()
  i = (i+1) % 256
