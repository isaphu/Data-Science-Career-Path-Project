
def ground_shipping(weight):
  if (weight < 2):
    return (weight * 1.5) + 20
  elif (weight > 2 and weight <= 6):
    return (weight * 3) + 20
  elif (weight > 6 and weight <= 10):
    return (weight * 4) + 20
  else: 
    return (weight * 4.75) + 20


print(ground_shipping(8.4))

premium_shipping = 125.00

def drone_shipping(weight):
  if (weight < 2):
    return (weight * 4.5)
  elif (weight > 2 and weight <= 6):
    return (weight * 9) 
  elif (weight > 6 and weight <= 10):
    return (weight * 12) 
  else: 
    return (weight * 14.25) 

print(drone_shipping(1.5))

def shipping_method(weight):

  ground = ground_shipping(weight)
  premium = premium_shipping
  drone = drone_shipping(weight)

  if ground < premium and ground < drone:
    method = "ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium"
    cost = premium 
  else:
    method = "drone"
    cost = drone
    
    print(
      "You should ship using %s shipping, it will cost $%.2f"
       % (method, cost)
      )

shipping_method(4.8)
shipping_method(41.5)


