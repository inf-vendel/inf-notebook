def get_items():
    # Return a sorted list of all .md files' names (without extension) as a list
    return sorted([i.replace(".md", "") for i in os.listdir(data) if ".md" in i], reverse=True)
