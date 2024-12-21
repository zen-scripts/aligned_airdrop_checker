# Updated script to handle stripping and skipping empty lines

# File paths (update these paths as necessary)
eligible_addresses_file = "eligible_addresses.csv"
my_addresses_file = "my_addresses.txt"
output_results_file = "results.txt"

# Initialize lists for eligible addresses and loaded addresses
eligible_addresses = []
my_addresses = []

# Reading eligible addresses from the CSV file, skipping empty lines
with open(eligible_addresses_file, "r") as file:
    next(file)  # Skip the header
    eligible_addresses = [
        line.split(",")[0].strip().lower()
        for line in file if line.strip()
    ]

# Reading my addresses from the TXT file, skipping empty lines
with open(my_addresses_file, "r") as file:
    my_addresses = [line.strip() for line in file if line.strip()]

# Check for eligible addresses
matched_addresses = [address for address in my_addresses if address.lower() in eligible_addresses]

# Output statistics
total_loaded = len(my_addresses)
total_eligible = len(matched_addresses)

print(f"Total addresses loaded: {total_loaded}")
print(f"Eligible addresses found: {total_eligible}")

# Save results to a file if there are eligible addresses
if total_eligible > 0:
    with open(output_results_file, "w") as file:
        file.write("\n".join(matched_addresses))

    print(f"Eligible addresses saved to {output_results_file}")