# static solution
sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
slce = sentence[0:33]
print(slce)

#dynamic solution
sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
slce = test_str[:test_str.index(",")] 
print(slce)
