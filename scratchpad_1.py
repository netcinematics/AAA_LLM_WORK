
import time

# --- MODEL A (Iterative) ---
def digital_root_A(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# --- MODEL B (Mathematical) ---
def digital_root_B(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


# --- BENCHMARK ---
iterations = 1000000
test_number = 493193  # A medium-sized number to test

print(f"Benchmarking {iterations:,} iterations...")

# Measure Model A
start_time = time.time()
for _ in range(iterations):
    digital_root_A(test_number)
end_time = time.time()
time_A = (end_time - start_time) * 1000  # Convert to milliseconds
print(f"Model A Time: {time_A:.4f} ms")

# Measure Model B
start_time = time.time()
for _ in range(iterations):
    digital_root_B(test_number)
end_time = time.time()
time_B = (end_time - start_time) * 1000  # Convert to milliseconds
print(f"Model B Time: {time_B:.4f} ms")

# Comparison
if time_B < time_A:
    print(f"\nModel B is {time_A / time_B:.2f}x faster!")
else:
    print(f"\nModel A is {time_B / time_A:.2f}x faster!")