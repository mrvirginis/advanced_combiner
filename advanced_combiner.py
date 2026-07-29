import os
import sys
import itertools

# Hardcoded pool of special characters requested by the user
ALLOWED_SPECIAL_CHARS = "!@#$&*-_"

# 25 GB in Bytes (25 * 1024 * 1024 * 1024)
MAX_FILE_SIZE_BYTES = 26843545600

BANNER = r"""

  █████╗  ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗
  ███████║██║  ██║██║   ██║███████║██╔██╗ ██║██║     █████╗  ██║  ██║
  ██╔══██║██║  ██║╚██╗ ██╔╝██╔══██║██║╚██╗██║██║     ██╔══╝  ██║  ██║
  ██║  ██║██████╔╝ ╚████╔╝ ██║  ██║██║ ╚████║╚██████╗███████╗██████╔╝
  ╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═════╝ 
  ██████╗  ██████╗ ███╗   ███╗██████╗ ██╗███╗   ██╗███████╗██████╗   
  ██╔════╝ ██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║██╔════╝██╔══██╗  
  ██║      ██║   ██║██╔████╔██║██████╔╝██║██╔██╗ ██║█████╗  ██████╔╝  
  ██║      ██║   ██║██║╚██╔╝██║██╔══██╗██║██║╚██╗██║██╔══╝  ██╔══██╗  
  ╚██████╗ ╚██████╔╝██║ ╚═╝ ██║██████╔╝██║██║ ╚████║███████╗██║  ██║  
   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝v1
                [ Designed & Coded by BlackzodiaK. ]
     [Version 1.01 - Released 2026 - TheBlackzodaiK.blogspot.com]

"""

def display_banner_and_wait():
    """Displays the custom ASCII banner and waits for user to press Enter before clearing."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    input("                 Press ENTER to start combining...")
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_file(prompt):
    """Prompts user for a file path and validates it."""
    while True:
        path = input(prompt).strip().strip('"').strip("'")
        if os.path.isfile(path):
            return path
        print(f"❌ Error: File not found at '{path}'. Please try again.")

def get_integer_input(prompt, min_val=0, max_val=10):
    """Safely gets an integer within a range from the user."""
    while True:
        try:
            val = int(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
            print(f"❌ Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("❌ Please enter a valid number.")

def get_choice(prompt, options):
    """Forces user to pick from a list of valid string choices."""
    while True:
        val = input(prompt).strip().lower()
        if val in options:
            return val
        print(f"❌ Invalid choice. Choose from: {', '.join(options)}")

def get_special_chars_combos(chars_str, length):
    """Generates all possible repeating combinations of a string of symbols up to a certain length."""
    if not chars_str or length == 0:
        return [""]
    all_combos = [""]
    for l in range(1, length + 1):
        for combo in itertools.product(chars_str, repeat=l):
            all_combos.append("".join(combo))
    return all_combos

def get_split_filename(base_path, part_num):
    """Generates sequential filenames like combined_1.txt, combined_2.txt."""
    dir_name, file_name = os.path.split(base_path)
    name, ext = os.path.splitext(file_name)
    new_file_name = f"{name}_{part_num}{ext}"
    return os.path.join(dir_name, new_file_name)

def main():
    display_banner_and_wait()
    
    print("=== Advanced Combiner v1.01 - Interactive Hashcat Wordlist Combiner ===")
    print("                 [ Designed & Coded by BlackzodiaK. ]")
    print("      [Version 1.01 - Released 2026 - TheBlackzodaiK.blogspot.com]")
    print(" ")
    print(" ")
    print(" ")
    print(f"Special char preset configured to: { ' '.join(ALLOWED_SPECIAL_CHARS) }\n")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    
    # 1. File Inputs
    file1_path = get_valid_file(" -> Enter path to Wordlist 1: ")
    file2_path = get_valid_file(" -> Enter path to Wordlist 2: ")
    base_output_path = input(" -> Enter path for output TXT file (e.g., combined.txt): ").strip().strip('"').strip("'")
    
    # 2. Digit Settings
    num_digits = get_integer_input("\nHow many digits do you want to insert? (e.g., 1, 2, 3, 4): ", min_val=0, max_val=8)
    
    digit_position = "m"
    if num_digits > 0:
        digit_position = get_choice(
            "Where should the digits be placed? (F-front / M-middle / E-end): ", 
            ["f", "m", "e"]
        )
        
    # 3. Front Special Characters
    use_front_chars = get_choice("\nAdd special characters to beginning of passwords? (y/n): ", ["y", "n"])
    front_combos = [""]
    if use_front_chars == 'y':
        max_len = get_integer_input("Maximum combination length of special characters? (1-4): ", min_val=1, max_val=4)
        front_combos = get_special_chars_combos(ALLOWED_SPECIAL_CHARS, max_len)

    # 4. End Special Characters
    use_end_chars = get_choice("\nAdd special characters to end of passwords? (y/n): ", ["y", "n"])
    end_combos = [""]
    if use_end_chars == 'y':
        max_len = get_integer_input("Maximum combination length of special characters? (1-4): ", min_val=1, max_val=4)
        end_combos = get_special_chars_combos(ALLOWED_SPECIAL_CHARS, max_len)

    print("\nReading source wordlists...")
    try:
        with open(file1_path, 'r', encoding='utf-8', errors='ignore') as f1:
            words1 = [line.strip() for line in f1 if line.strip()]
        with open(file2_path, 'r', encoding='utf-8', errors='ignore') as f2:
            words2 = [line.strip() for line in f2 if line.strip()]
    except Exception as e:
        print(f"❌ Failed to read files: {e}")
        return

    digit_pool = [""]
    if num_digits > 0:
        digit_pool = [f"{i:0{num_digits}d}" for i in range(10**num_digits)]

    word_pairs_count = len(words1) * len(words2) * 2
    total_combos = word_pairs_count * len(digit_pool) * len(front_combos) * len(end_combos)
    print(f"📊 Words Loaded: List 1 ({len(words1)}), List 2 ({len(words2)})")
    print(f"🚀 Generating approximately {total_combos:,} total unique combinations...")

    try:
        count = 0
        part_number = 1
        current_file_size = 0
        
        # Open the very first partition file (e.g., combined_1.txt)
        current_output_path = get_split_filename(base_output_path, part_number)
        out_file = open(current_output_path, 'w', encoding='utf-8')
        print(f"📂 Writing to file partition: {os.path.basename(current_output_path)}...")

        directions = [(words1, words2), (words2, words1)]
        
        for w1_list, w2_list in directions:
            for w1 in w1_list:
                for w2 in w2_list:
                    for d_val in digit_pool:
                        
                        # Construct core word-digit combo based on placement choice
                        if num_digits == 0:
                            base_combo = f"{w1}{w2}"
                        elif digit_position == "f":
                            base_combo = f"{d_val}{w1}{w2}"
                        elif digit_position == "m":
                            base_combo = f"{w1}{d_val}{w2}"
                        elif digit_position == "e":
                            base_combo = f"{w1}{w2}{d_val}"
                        
                        # Multiply by special character loops
                        for f_char in front_combos:
                            for e_char in end_combos:
                                password_line = f"{f_char}{base_combo}{e_char}\n"
                                line_bytes_len = len(password_line.encode('utf-8'))
                                
                                # Check if adding this line violates our 25 GB limit
                                if current_file_size + line_bytes_len > MAX_FILE_SIZE_BYTES:
                                    out_file.close()
                                    print(f"✅ Finished partition {part_number} ({current_file_size / (1024**3):.2f} GB).")
                                    
                                    # Increment partition and swap file streams
                                    part_number += 1
                                    current_output_path = get_split_filename(base_output_path, part_number)
                                    out_file = open(current_output_path, 'w', encoding='utf-8')
                                    print(f"📂 Swapped to new file partition: {os.path.basename(current_output_path)}...")
                                    current_file_size = 0
                                
                                # Write out the word string and keep tabs on file size accumulation
                                out_file.write(password_line)
                                current_file_size += line_bytes_len
                                count += 1
                                
        # Safely wrap up and shut down the last operational file stream
        out_file.close()
        print(f"\n✅ Success! Total generated dictionary items: {count:,} words across {part_number} file partition(s).")
        print(f"📂 Final files directory output: {os.path.dirname(os.path.abspath(base_output_path))}")
        
    except Exception as e:
        print(f"❌ Failed to write output file split: {e}")

if __name__ == "__main__":
    main()
    input("\nPress Enter to close this window...")
