import random
import statistics
import matplotlib.pyplot as plt
def calculate_clock_skew(clock_times):
    return max(clock_times) - min(clock_times)
def calculate_clock_jitter(clock_edges):
    return statistics.stdev(clock_edges)
def main():

    print("CLOCK SKEW AND JITTER ANALYSIS TOOL\n")

    num_flops = int(input("Enter number of flip-flops: "))

    clock_times = []
    print("\nEnter clock arrival times (in ns):")
    for i in range(num_flops):
        time = float(input(f"Flip-Flop {i+1}: "))
        clock_times.append(time)

    skew = calculate_clock_skew(clock_times)
    print("\nClock Skew:", round(skew, 4), "ns")

    clock_edges = [random.uniform(9.8, 10.2) for _ in range(20)]
    jitter = calculate_clock_jitter(clock_edges)
    print("Clock Jitter:", round(jitter, 4), "ns")
    flops = [f"FF{i+1}" for i in range(num_flops)]
    plt.figure()
    plt.bar(flops, clock_times)
    plt.xlabel("Flip-Flops")
    plt.ylabel("Clock Arrival Time (ns)")
    plt.title("Clock Skew Analysis")
    plt.figure()
    plt.plot(clock_edges, marker='o')
    plt.xlabel("Clock Cycles")
    plt.ylabel("Clock Edge Time (ns)")
    plt.title("Clock Jitter Analysis")
    plt.show()
    if skew < 0.2 and jitter < 0.1:
        print("\nTiming Status: SAFE ")
    else:
        print("\nTiming Status: RISKY ")

if __name__ == "__main__":
    main()
