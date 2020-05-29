# Mandelbrot approximation of PI:
# Plugin k=c+e into z_next = z^2 + k, where c = 0.25 and k is a small number
# e = 0.000001 => 3.141

e = 0.000001

c = 0.25+e
val = 0
steps = 1

while(val <= 2):
    steps+=1
    val = val*val + c

print('pi is ~ %d' % steps)
