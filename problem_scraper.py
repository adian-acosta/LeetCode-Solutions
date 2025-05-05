import customtkinter as ctk
from tkinter import messagebox
import requests
# from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse


# file extensions mapping
LANG_EXT = {
    "Python": "py",
    "Java": "java",
    "C++": "cpp",
    "C": "c",
    "C#": "cs",
    "JavaScript": "js",
    "TypeScript": "ts",
    "PHP": "php",
    "Swift": "swift",
    "Kotlin": "kt",
    "Dart": "dart",
    "Go": "go",
    "Ruby": "rb",
    "Scala": "scala",
    "Rust": "rs",
    "Racket": "rkt",
    "Erlang": "erl",
    "Elixir": "ex"
}


def extract_slug(url):
    path_parts = urlparse(url).path.strip("/").split("/")
    if "problems" in path_parts:
        idx = path_parts.index("problems")
        if idx + 1 < len(path_parts):
            return path_parts[idx + 1]
    
    raise ValueError("Could not extract slug from URL.")


def scrape_leetcode(link):
    slug = extract_slug(link)
    query = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            content
            difficulty
            topicTags {
              name
            }
          }
        }
        """
    }

    headers = {
        "Content-Type": "application/json",
        "Referer": link,
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.post("https://leetcode.com/graphql", json=query, headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch data from LeetCode GraphQL")

    data = response.json()
    question = data['data']['question']
    if not question:
        raise Exception("Question not found.")

    number = question['questionFrontendId']
    name = question['title']
    difficulty = question['difficulty'].lower()
    # description = BeautifulSoup(question['content'], 'html.parser').get_text(separator="\n").strip()
    topics = ", ".join(tag['name'] for tag in question['topicTags'])

    return number, name, topics, difficulty


def run(url, lang, create_md):
    try:
        number, name, topics, difficulty = scrape_leetcode(url)
    except Exception as e:
        messagebox.showerror("Error", f"LeetCode scraping faled: {e}")
        return
    
    ext = LANG_EXT.get(lang, lang)
    safe_name = name.lower().replace(" ", "_")
    solution_link = f"https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/{difficulty}/{safe_name}.{ext}"
    notes_link = f"https://github.com/adian-acosta/LeetCode-Solutions/tree/main/leetcode/{difficulty}/{safe_name}.md"
    
    # update markdown file
    md_path = os.path.join(os.getcwd(), "README.md")
    # This assumes the README does not exist yet. If it does, where the the table was created within the README put the following lines right above it for the table to work
    # Another solution would be to change the name of the .md file this is getting put into then run this and get the output within that file and copy and paste into the README
    if not os.path.exists(md_path):
        with open(md_path, "w") as f:
            f.write("| # | Problem | Topics | Solution | Notes |\n")
            f.write("| ----------- | ------ | -------- | -------------- | -------------- |\n")
    
    with open(md_path, "a", encoding="utf-8") as f:
        if create_md:
            f.write(f"| {number} | {name} | {topics} | [{lang}]({solution_link}) | [Notes]({notes_link}) |\n")
        else:
            f.write(f"| {number} | {name} | {topics} | [{lang}]({solution_link}) |  |\n")
    
    # create solution and optional note file
    base_dir = os.path.join(os.getcwd(), "leetcode", difficulty)
    os.makedirs(base_dir, exist_ok=True)
    
    code_file = os.path.join(base_dir, f"{safe_name}.{ext}")
    notes_file = os.path.join(base_dir, f"{safe_name}.md")
    
    open(code_file, "a").close()
    if create_md:
        open(notes_file,"a").close()
    
    msg = f"'{name}' added successfully!\n\nFiles created:\n- {code_file}"
    if create_md:
        msg += f"\n= {notes_file}"
    msg += "\n\nPaste your code and notes in the respective files."
    
    messagebox.showinfo("Success", msg)


def main():
    def submit():
        url = url_entry.get()
        lang = lang_var.get()
        create_md = md_var.get()
        if not url or not lang:
            messagebox.showerror("Error", "Please provide both a URL and select a language.")
            return
        #window.destroy()
        run(url, lang, create_md)
    

    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    # main window
    window = ctk.CTk()
    window.title("LeetCode Problem Logger")
    window.geometry("500x260")
    window.resizable(False, False)

    # frame for layout
    frame = ctk.CTkFrame(master=window)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    # URL entry
    url_label = ctk.CTkLabel(master=frame, text="LeetCode problem URL:", font=("Segoe UI", 11))
    url_label.grid(row=0, column=0, sticky="w", pady=10)
    url_entry = ctk.CTkEntry(master=frame, width=300)
    url_entry.grid(row=0, column=1, padx=10)

    # language dropdown
    lang_label = ctk.CTkLabel(master=frame, text="Programming language:", font=("Segoe UI", 11))
    lang_label.grid(row=1, column=0, sticky="w", pady=10)
    lang_var = ctk.StringVar()
    lang_menu = ctk.CTkComboBox(master=frame, variable=lang_var, values=list(LANG_EXT.keys()), width=300)
    lang_menu.grid(row=1, column=1, padx=10)
    lang_menu.set(list(LANG_EXT.keys())[0])  # Set default option

    # markdown checkbox
    md_var = ctk.BooleanVar(value=True)
    md_checkbox = ctk.CTkCheckBox(master=frame, text="Also create a .md (notes) file", variable=md_var)
    md_checkbox.grid(row=2, column=0, columnspan=2, pady=10, sticky="w")

    # submit button
    submit_btn = ctk.CTkButton(master=frame, text="Submit", command=submit)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

    window.mainloop()


if __name__ == "__main__":
    main()