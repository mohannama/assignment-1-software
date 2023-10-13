# Explanation: This program searches for "near misses" of Fermat's Last Theorem,
# where xn + yn ≠ zn, for various combinations of positive integers x, y, z, n, and k.
# Function to calculate the smallest miss and relative miss
def calculate_miss(x, y, z, n):
    result = x**n + y**n
    zn = int(result ** (1/n))
    z_plus_1n = zn + 1
    miss1 = result - zn**n
    miss2 = z_plus_1n**n - result
    smallest_miss = min(abs(miss1), abs(miss2))
    relative_miss = (smallest_miss / result) * 100
    return smallest_miss, relative_miss

# Main function
def main():
    n = int(input("Enter the value of n (2 < n < 12): "))
    k = int(input("Enter the value of k (k > 10): "))

    smallest_relative_miss = float('inf')
    best_x, best_y, best_z, best_miss = None, None, None, None

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            for z in range(1, 100):  # Adjust this range as needed
                if x != y:
                    miss, relative_miss = calculate_miss(x, y, z, n)
                    if relative_miss < smallest_relative_miss:
                        smallest_relative_miss = relative_miss
                        best_x, best_y, best_z, best_miss = x, y, z, miss

    print("Best Near Miss:")
    print(f"x: {best_x}, y: {best_y}, z: {best_z}")
    print(f"Actual Miss: {best_miss}")
    print(f"Relative Miss: {smallest_relative_miss}%")

if __name__ == "__main__":
    main()
