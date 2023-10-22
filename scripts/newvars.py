def update_variables(var_block, preserve=False):
    new_block = {}
    invalid_lines = []

    # Split the block into lines
    lines = var_block.strip().split('\n')

    # Loop over each line in the block
    for line_number, line in enumerate(lines, start=1):
        # Skip empty lines
        if not line.strip():
            continue

        # Find the first colon or equal sign in the line
        first_colon_index = line.find(':')
        first_equal_index = line.find('=')

        # Determine which separator was used
        if first_colon_index != -1 and (first_equal_index == -1 or first_colon_index < first_equal_index):
            separator_index = first_colon_index
            separator = ':'
        elif first_equal_index != -1 and (first_colon_index == -1 or first_equal_index < first_colon_index):
            separator_index = first_equal_index
            separator = '='
        else:
            invalid_lines.append(line_number)
            continue

        # Extract the field name and value
        field_name = line[:separator_index].strip()
        old_value = line[separator_index + 1:].strip()

        # Prompt for new value, showing old value if applicable
        new_value = input(f"Enter a new value for {field_name} (old value: '{old_value}'): ").strip()

        # If preserve flag is set and no new value is provided, keep the old value
        if preserve and not new_value:
            new_block[field_name] = old_value
        else:
            # Set new value or blank if input is "--"
            new_block[field_name] = "" if new_value == "--" else new_value

    # Convert the new block back to a string
    new_block_str = '\n'.join(f"{k}: {v}" for k, v in new_block.items())

    return new_block_str, invalid_lines


if __name__ == "__main__":
    print("Enter variables block, one line per variable. End input with a blank line containing 'end'.")
    
    # Initialize an empty string to store the user input
    var_block = ""
    
    # Keep reading lines until a blank line with "end" is encountered
    while True:
        line = input().strip()
        if line == "end":
            break
        var_block += line + "\n"

    new_block_str, invalid_lines = update_variables(var_block, preserve=False)
    print("Updated block:")
    print(new_block_str)
    print("Invalid lines:")
    print(invalid_lines)
