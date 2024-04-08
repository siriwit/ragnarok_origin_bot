
time_left = 290
ignore_spawn = False
threshold = 180
map_distant_offset = 120

print(f"time left: {time_left}")
print(f"ignore spawn: {ignore_spawn}")
condition1 = not ignore_spawn and (time_left<=0 or time_left==9999)
condition2 = (time_left < (threshold + map_distant_offset) and time_left > map_distant_offset)
print(f"con1: {condition1}")
print(f"con2: {condition2}")
if (condition1) or (condition2):
    print("boss fight")