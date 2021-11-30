import cellpylib as cpl
import time

start = time.time()
cpl.evolve(cpl.init_simple(600), timesteps=300,
           apply_rule=lambda n, c, t: cpl.nks_rule(n, 30))
print(f"Without memoization: {time.time() - start:.2f} seconds elapsed")

start = time.time()
cpl.evolve(cpl.init_simple(600), timesteps=300,
           apply_rule=lambda n, c, t: cpl.nks_rule(n, 30), memoize=True)
print(f"With memoization: {time.time() - start:.2f} seconds elapsed")
