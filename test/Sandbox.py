import math

lat = 16.538
assumedLat = -53.64
long = 95.693
assumedLong = 74.5883
LHA = long + assumedLong

A = math.sin(math.radians(lat))
B = math.sin(math.radians(assumedLat))
C = math.cos(math.radians(lat))
D = math.cos(math.radians(assumedLat))
E = math.cos(math.radians(LHA))

print A
print B
print C
print D
print E

print ((A * B) + (C * D * E))
