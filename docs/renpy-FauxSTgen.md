# Ren'Py Visual Novel Music Extraction and Track Numbering Workflow

This workflow is designed to extract music files from a Ren'Py visual novel game and organize them in a sorted order based on their appearance in the game's scripts. It also adds track numbers to the filenames. Please note that this workflow is specifically created for macOS.

## Prerequisites

Ensure that you have the following software installed on your macOS system:

-  Ren'Py visual novel game
-  Python (to run Ren'Py scripts)
-  id3tag (to add track numbers to the filenames)
-  Terminal or Command Line access

## Workflow Steps

Follow these steps to execute the workflow:

1. Launch the Ren'Py visual novel game and locate the script files.

2. Copy and paste the provided script to extract and sort the music filenames in the desired order based on their appearance in the scripts. Replace the placeholders in the script with the appropriate commands.

```
<Insert Ren'Py script extraction and sorting command here>
```

3. Execute the modified script to extract and sort the music filenames.

4. Copy and paste the list of sorted filenames into a text editor, ensuring they are in the desired order.

5. Copy and paste the provided script to add track numbers to the music filenames. Replace the placeholders in the script with the appropriate commands.

```bash
<Insert track numbering script command here>
```

6. Execute the modified script to add track numbers to the music filenames.

7. Review the output to ensure that the track numbers are added correctly.

8. Verify that the track-numbered music files are sorted in the desired order.

## Limitations

-  This workflow assumes that the Ren'Py visual novel game's scripts contain the music filenames in the order of their appearance.

-  Make sure to replace the placeholders in the provided scripts with the appropriate commands for Ren'Py script extraction, sorting, and track numbering.

-  This workflow is specific to macOS. Please ensure that the necessary dependencies (Ren'Py, Python, id3tag) are installed and compatible with macOS systems.

## Conclusion

With this workflow, you can easily extract music files from Ren'Py visual novel games, organize them in a sorted order according to their appearance in the game scripts, and add track numbers to the filenames. The resulting music files will be ready for use in any music player or for further processing.

Note that this workflow assumes the correct structure and naming conventions of the Ren'Py visual novel game scripts. It's important to verify the accuracy of the sorted order and track numbering based on the game's actual content.

Please ensure you have appropriate rights and permissions to extract and modify the music files from the Ren'Py visual novel game. Always respect the game developer's intellectual property rights.

**Disclaimer:** Use this workflow responsibly and in accordance with local laws and regulations.


```bash
#!/bin/bash

filenames=(
  "Leila.mp3" "Calm Guitar.mp3" "Tranquil.mp3" "Scheming.mp3" "Somber Strings.mp3"
  "Horror.mp3" "Decisions.mp3" "Solemnnight Loop.mp3" "My Oath To You(Slow).mp3"
  "Wrong Turn.mp3" "Volatile.mp3" "Clown.mp3" "Somber.mp3" "Solemnnight.mp3"
  "Water Lily.mp3" "Fragments.mp3" "Wacky.mp3" "Hyperfun.mp3" "Lullaby Guitar.mp3"
  "Snowdrop.mp3" "Cafe Music.mp3" "Beastsonata.mp3" "Batty.mp3" "Soothing Rain.mp3"
  "Jazz.mp3" "Meloncholy.mp3" "Moonheart Guitar.mp3" "Siren.mp3" "Blue Feather.mp3"
  "Army.mp3" "Mother.mp3" "Mother Slow.mp3" "Jinny Ringtone.mp3" "Moonheart.mp3"
  "Hanahaki Slow Piano.mp3" "Little Something Slow.mp3" "Cozy.mp3" "Nighthunter.mp3"
  "Easy Lemon.mp3" "Ghost2.mp3" "Hitman.mp3" "Drift.mp3" "Asphodel.mp3" "Snowy Street.mp3"
  "Compassion.mp3"
)

total_files=${#filenames[@]}

for (( i=0; i<total_files; i++ )); do
  filename="${filenames[i]}"
  track_number=$((i+1))
  id3tag -t "$track_number" "$filename"
done
```