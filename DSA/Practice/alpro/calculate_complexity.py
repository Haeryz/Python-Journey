import time

def measure_complexity(n):
    start = time.time()
    for i in range(n):
        print(i)  # Simulating the loop
    end = time.time()
    return end - start

# Test for different n values
for n in [10, 100, 1000]:
    runtime = measure_complexity(n)
    print(f"n={n}: {runtime:.4f} seconds")