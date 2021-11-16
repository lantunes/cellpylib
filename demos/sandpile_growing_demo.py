import cellpylib as cpl

"""
We repeatedly drop a grain of sand in the middle, allowing the sandpile to grow. 
After a grain is dropped, the system is allowed to evolve until a fixed point, 
where no further change occurs, before the next grain is dropped.
"""
n = 50
sandpile = cpl.Sandpile(n, n)
ca = cpl.init_simple2d(n, n, val=5)

for i in range(300):
    ca[-1, n//2, n//2] += 1
    ca = cpl.evolve2d(ca, apply_rule=sandpile,
                      timesteps=cpl.until_fixed_point(), neighbourhood='Moore')

cpl.plot2d_animate(ca)
