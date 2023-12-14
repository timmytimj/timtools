def convert_transcript(input_text):
    # Split lines and initiate variables
    lines = input_text.strip().split('\n')
    markdown_lines = []

    for i, line in enumerate(lines):
        # Check if the line is a timestamp or text
        if line.strip().isdigit():
            # The current line is a timestamp
            timestamp = f"{line.strip()}:00"
            text_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
            markdown_lines.append(f"### [{timestamp}]\n{text_line}\n\n")
        elif (i == 0) or (lines[i - 1].strip().isdigit() and line.strip() != "English (auto-generated)"):
            # The line is a Section-Title or the first line
            markdown_lines.append(f"## {line.strip()}\n\n")

    # Join the converted text
    markdown_text = ''.join(markdown_lines)

    return markdown_text

# Input prompt for the user
input_text = input("Please paste the YouTube transcript here:\n")

# Process and Convert the Transcript
converted_markdown = convert_transcript(input_text)

# Output the formatted Markdown text
print("Converted Markdown Transcript:")
print(converted_markdown)

# Optionally, you can save the output to a file
with open("output_transcript.md", "w", encoding="utf-8") as file:
    file.write(converted_markdown)

# Indicate the file has been saved
print("\nThe converted transcript has been saved to 'output_transcript.md'")
