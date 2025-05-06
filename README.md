# LeetCode Solutions

## Summary

This repository contains my solutions to LeetCode problems, along with notes on my approach, thought process, and algorithms used. Some problems may have multiple solutions in different programming languages as I like to sometimes practice languages beyond my primary one, Python.

Additionally, the repository includes a `problem_scraper.py` script that automates the process of:
- Adding completed problems to the `README.md` table.
- Creating solution and notes files.
- Organizing files into appropriate folders based on difficulty.

If you have better solutions to the problems, advice on improving the web scraper, or just want to connect, feel free to reach out! I’m always open to learning and connecting :D.

For more details about the scraper, see the [Web Scraper](#web-scraper) section.

## List of Problems

| # | Problem | Topics | Solution | Notes |
| ----------- | ------ | -------- | -------------- | -------------- |
| 1 | Two Sum | Array, Hash Table | [Python](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/two_sum.py) | [Notes](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/two_sum.md) |
| 9 | Palindrome Number | Math | [Python](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/palindrome_number.py) | [Notes](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/palindrome_number.md) |
| 121 | Best Time to Buy and Sell Stock | Array, Dynamic Programming | [Python](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/best_time_to_buy_and_sell_stock.py) | [Notes](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/best_time_to_buy_and_sell_stock.md) |
| 20 | Valid Parentheses | String, Stack | [Python](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/valid_parentheses.py) | [Notes](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/valid_parentheses.md) |
| 21 | Merge Two Sorted Lists | Linked List, Recursion | [Python](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/merge_two_sorted_lists.py) | [Notes](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/merge_two_sorted_lists.md) |
| 53 | Maximum Subarray | Array, Divide and Conquer, Dynamic Programming | [Python](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/medium/maximum_subarray.py) | [Notes](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/medium/maximum_subarray.md) |
| 11 | Container With Most Water | Array, Two Pointers, Greedy | [C++](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/medium/container_with_most_water.cpp) |  |
| 13 | Roman to Integer | Hash Table, Math, String | [C++](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/roman_to_integer.cpp) |  |
| 167 | Two Sum II - Input Array Is Sorted | Array, Two Pointers, Binary Search | [Python](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/medium/two_sum_ii_-_input_array_is_sorted.py) | [Notes](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/medium/two_sum_ii_-_input_array_is_sorted.md) |
| 70 | Climbing Stairs | Math, Dynamic Programming, Memoization | [Python](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/climbing_stairs.py) | [Notes](https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/easy/climbing_stairs.md) |



## Web Scraper

This web scraper automates the process of adding solutions to the `README.md` file, creating solution files, and organizing them into appropriate folders based on difficulty. It eliminates the need for manual updates and file creation.

The program uses:
- **CustomTkinter** for a more modern GUI compared to Tkinter.
- **Requests** for HTTP requests.
- **BeautifulSoup** (currently unused but planned for future enhancements, such as HackerRank scraping).

### How to Use

#### Prerequisites
1. Clone this repository or copy the program files (`problem_scraper.py` and `requirements.txt`) into the same folder.
2. Install the required Python modules using `pip`. I would recommended to use a virtual environment for better module management.

#### Setting Up a Virtual Environment
- On **Windows**:
  ```
  python -m venv env
  env\Scripts\Activate
  ```
- On **Mac**:
  ```
  python3 -m venv env
  source env/bin/activate
  ```

You’ll know the virtual environment is active when its name appears as a prefix in your terminal.

#### Installing Dependencies
Run the following command to install the required modules:
```
pip install -r requirements.txt
```

#### Running the Program
Execute the program with, once done a small window will pop up:
```
python problem_scraper.py
```

![Screenshot 2025-05-04 232519](https://github.com/user-attachments/assets/f5362525-4b70-45be-bf2a-5dd0b34ae6a1)


#### Using the GUI
1. Enter the **LeetCode problem link** in the top input box.
2. Select the **programming language** from the dropdown menu.
3. (Optional) Check the box to create a **notes file** for the problem.
4. Click **Submit**.

#### What Happens Next
- If a `README.md` file doesn’t exist, the program creates one. Otherwise, it updates the existing file by adding the problem to the table.
- A new folder named `leetcode` is created (if it doesn’t already exist) to store:
  - The solution file.
  - The notes file (if selected).

You can then paste your solution into the generated file, and the `README.md` will be updated automatically.
