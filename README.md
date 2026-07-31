# 🛠️ Advanced Combiner (v1.01)

An advanced, interactive terminal-based Python utility designed for high-performance security auditing and Hashcat dictionary generation. It merges two source wordlists cross-product style (both list1+list2 and list2+list1), with options to inject sequential padded numeric strings and repeating structural loops of special characters.

To prevent filesystem crashes, the utility automatically enforces smart partition chunking, seamlessly splitting oversized dictionaries into predictable file segments once data boundaries are reached.

## 📌 Features

* **Bi-Directional Cross-Combinations** - Automatically pairs strings in both permutations: `Wordlist1 + Wordlist2` AND `Wordlist2 + Wordlist1`.
* **Flexible Padded Digit Pools** - Generates up to 8-digit sequential numeric pools (`00000001` through `99999999`) and strategically places them at the **Front**, **Middle**, or **End** of the merged base strings.
* **Dual-Zone Special Characters** - Permits variable length configurations (1 to 4 characters deep) of high-frequency password symbols (`!@#$&*-_`) to be appended independently to the *beginning*, *end*, or *both* sides of every entry.
* **Automated Smart Partitioning** - Continuously monitors target data payload generation in real-time. If the cumulative byte density hits threshold limits, it automatically closes, increments, and spins up sequential output shards (e.g., `combined_1.txt`, `combined_2.txt`).
* **Fault-Tolerant Streaming** - Implements strict `UTF-8` error ignoring routines to process large data payloads without crashing over broken encodings.

---------------------------------------------------------

## 🛠️ Prerequisites

The script runs fully out-of-the-box using built-in, core Python components. No external pip installations are necessary.
* **Python 3.6 or higher**
* Standard modules used: `os`, `sys`, `itertools`

---------------------------------------------------------

## 🚀 Installation & Setup

1. **Clone this repository** to your local environment:
   ```bash
   git clone https://github.com/mrvirginis/advanced_combiner
   cd advanced_combiner
   ```

2. **Verify your Python installation:**
   ```bash
   python --version
   ```

3. **Run the utility:**
   ```bash
   python advanced_combiner.py
   ```

---------------------------------------------------------

## 📖 Usage Guide

The tool walks you through an automated, interactive setup:

1. **Path Configurations**: Enter valid files for your source lists and establish a baseline target filename (e.g., `combined.txt`). 
2. **Numeric Settings**: Pick a digit length parameter (0 to 8). If enabled, choose to position the sequential integers at the front (`f`), split the base words in the middle (`m`), or stick them on the end (`e`).
3. **Special Character Boundaries**: Opt-in to generate comprehensive multi-length combinatorial symbol layers up to 4 places deep for both the beginning and trailing ends of your words.
4. **Execution Matrix**: The script calculates expected output metrics, automatically prepares file streams, and initiates structured disk writes across segmented storage paths.

---------------------------------------------------------

## 📝 Example Session

```text
=== Advanced Combiner v1.01 - Interactive Hashcat Wordlist Combiner ===
 [ Designed & Coded by BlackzodiaK. ]
 [Version 1.01 - Released 2026 - TheBlackzodaiK.blogspot.com]
 

Special char preset configured to: ! @ # \$ & * - _

 -> Enter path to Wordlist 1: list1.txt
 -> Enter path to Wordlist 2: list2.txt
 -> Enter path for output TXT file (e.g., combined.txt): output/dictionary.txt

How many digits do you want to insert? (e.g., 1, 2, 3, 4): 2
Where should the digits be placed? (F-front / M-middle / E-end): m

Add special characters to beginning of passwords? (y/n): y
Maximum combination length of special characters? (1-4): 1

Add special characters to end of passwords? (y/n): n

Reading source wordlists...
📊 Words Loaded: List 1 (500), List 2 (500)
🚀 Generating approximately 51,000,000 total unique combinations...
📂 Writing to file partition: dictionary_1.txt...

✅ Success! Total generated dictionary items: 51,000,000 words across 1 file partition(s).
📂 Final files directory output: /user/desktop/output
```

---------------------------------------------------------

## 👤 Credits

* **Author:** BlackzodiaK.
* **Release Version:** v1.01 (2026)
* **Official Blog:** [TheBlackzodaiK.blogspot.com](https://theblackzodiak.blogspot.com/)

---------------------------------------------------------

## 📝 License

Distributed under the MIT License. Feel free to use, modify, and distribute this script for personal or professional security evaluations.
