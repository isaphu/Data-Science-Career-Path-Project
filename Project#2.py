train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#temperature
def f_to_c(f_temp):
  celcius = ((f_temp - 32) * 5/9) 
  return celcius

f100_in_celsius = f_to_c(100) 
print(f100_in_celsius)

def c_to_f(c_temp):
  fahrenheit = (c_temp * (9/5) + 32)
  return fahrenheit

c0_in_fahrenheit = c_to_f(35)
print(c0_in_fahrenheit)

#force
def get_force(mass, acceleration):
  force = mass * acceleration
  return force

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force")

#energy
def get_energy(mass, c=3*10**8):
  return mass * (c**2)

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")


#work done
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
