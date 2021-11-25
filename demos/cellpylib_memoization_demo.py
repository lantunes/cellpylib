import cellpylib as cpl
import time

start = time.time()
cpl.evolve(cpl.init_simple(1000), timesteps=500,
           apply_rule=lambda n, c, t: cpl.nks_rule(n, 30), memoize=True)

print(f"Elapsed: {time.time() - start:.2f} seconds")
