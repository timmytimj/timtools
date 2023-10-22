compare_lists() {
  read -r -p $'Paste the items to find:\n' items_to_find
  read -r -p $'Paste the unfiltered list:\n' unfiltered_list
  read -r -p $'Are the items filenames? [y/n]: ' is_filenames
  read -r -p $'Ignore case? [y/n]: ' ignore_case
  if [[ "$is_filenames" == "y" ]]; then
    read -r -p $'Ignore extension? [y/n]: ' ignore_extension
  fi

  # Normalize the unfiltered list if needed
  unfiltered_list=$(echo "$unfiltered_list" | tr -cd '[:alnum:],()[] ')

  # Clean up and format the items to find
  if [[ "$items_to_find" == *$'\n'* ]]; then
    items_to_find_inputs=("${(@f)items_to_find}")
    items_to_find=$(IFS=","; echo "${items_to_find_inputs[*]}")
  else
    items_to_find=$(echo "$items_to_find" | tr -d '[:blank:]' | tr -d '\n')
  fi

  # Prepare sed options based on user preferences
  sed_options=""
  if [[ "$ignore_case" == "y" ]]; then
    sed_options+="I"
  fi

  # Process the unfiltered list and return matching items in the original order
  IFS=',' read -ra unfiltered_items <<< "$unfiltered_list"
  for item in "${unfiltered_items[@]}"; do
    item_name=$(echo "$item" | sed -E 's/^\s*(.*?)\s*$/\1/')
 
    if [[ "$ignore_case" == "y" ]]; then
      sed_options+="I"
    fi

    # Process the unfiltered list and return matching items in the original order
    IFS=',' read -ra unfiltered_items <<< "$unfiltered_list"
    for item in "${unfiltered_items[@]}"; do
      item_name=$(echo "$item" | sed -E 's/^\s*(.*?)\s*$/\1/')
      if [[ "$ignore_case" == "y" ]]; then
        item_name=$(echo "$item_name" | tr '[:upper:]' '[:lower:]')
      fi
      if [[ "$is_filenames" == "y" && "$ignore_extension" == "y" ]]; then
        item_name=$(echo "$item_name" | awk -F"." '{print $1}')
      fi
      if [[ " ${items_to_find[@]} " =~ " $item_name " ]]; then
        echo "$item"
      fi
    done

  else
    echo "Please enter items in the correct CSV format or one item per line (terminated by an end-of-line)."
  fi
}

