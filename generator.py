import random

def generate_canadian_numbers(area_codes, num_count, output_file):
    unique_numbers = set()
    
    while len(unique_numbers) < num_count:
        area_code = random.choice(area_codes)  # Pick a random area code
        number = f"1{area_code}{random.randint(1000000, 9999999)}"  # Generate a 7-digit number
        unique_numbers.add(number)  # Add to set (ensures no duplicates)

    # Save to file
    with open(output_file, "w") as file:
        for num in unique_numbers:
            file.write(num + "\n")
    
    print(f"✅ Successfully generated {num_count} unique phone numbers in {output_file}")

# Example usage
area_codes = ["418", "438", "450", "514", "579", "581", "819"]
 # You can modify this list
num_count = 10000  # Number of phone numbers to generate
output_file = "canadian_phone_numbers.txt"  # Output file name

generate_canadian_numbers(area_codes, num_count, output_file)
