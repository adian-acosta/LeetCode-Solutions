# Leetcode Solutions

## Summary

This repo has all my solutions to LeetCode questions that I have completed with notes on my approach and thoughts of the solution at the time to completion. I break down my thought process of handling the problem and the algorithm used, or algorithms if there are more than one, and how I would improve it. In the future I would like to include HackerRank problems as well. There may be more than one input of the same problem within the table this means the problem was solved with multiple programming languages and each one links to their solution to the same problem but in their respective languages, this may be done as I wanted to practice in another language other than my primary Python.

As for the `problem_scraper.py` this is a web scraper I made to sorta automate the process of adding the completed problem to the `README.md` table down below in the order that I complete them and creating files for faster pasting of my solutions and notes, more info about it found [here](#web-scraper).

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
Execute the program with:
```
python problem_scraper.py
```

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
