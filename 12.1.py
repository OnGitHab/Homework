def clean_html(input_filename, output_filename="cleaned.txt"):
    with open(input_filename, "r", encoding="utf-8") as infile:
        content = infile.read()

    clean_content = []
    in_tag = False

    for char in content:
        if char == "<":
            in_tag = True
        elif char == ">":
            in_tag = False
        elif not in_tag:
            clean_content.append(char)

    clean_content = "".join(clean_content)

    lines = clean_content.splitlines()

    clean_lines = [line for line in lines if line.strip()]

    cleaned_text = "\n".join(clean_lines)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write(cleaned_text)


input_file = "draft.html"
output_file = "clean.txt"
clean_html(input_file, output_file)

print(output_file)
