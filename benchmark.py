import time

def benchmark(func, inputs):
    """
    Benchmarks a function by timing its execution for each input in the list.
    
    This function measures the actual execution time for each input, which can help
    observe performance trends. Note that Big O notation (e.g., O(n), O(log n)) is
    asymptotic complexity analysis and cannot be directly measured. Instead, analyze
    how execution time scales with input size to infer complexity:
    - If time doubles when input size doubles: likely O(n)
    - If time stays constant when input size doubles: likely O(1) or O(log n)
    - Use large enough inputs to see clear trends; small inputs may have noise.
    
    Args:
        func (callable): The function to benchmark. Should accept one argument.
        inputs (list): List of inputs to pass to the function.
    
    Returns:
        list[float]: List of execution times (in seconds) for each input.
    
    Example:
        times = benchmark(lambda x: x**2, [10, 100, 1000])
        print(times)  # Shows times for squaring each number
    """
    times = []
    for inp in inputs:
        start_time = time.perf_counter()
        func(inp)
        end_time = time.perf_counter()
        elapsed = end_time - start_time
        times.append(elapsed)
        print(f"Input: {inp}, Time: {elapsed:.10f} seconds")
    return times
