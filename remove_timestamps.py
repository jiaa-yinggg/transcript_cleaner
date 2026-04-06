import re

# Open the transcript file and read all lines
with open("transcript.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
# "r": reading mode

cleaned_lines = []

# Go through each line
for line in lines:
    stripped_line = line.strip()
    # changes "2:39\n" to "2:39"

    # Check if the line is just a timestamp like 2:39 or 12:05
    if re.fullmatch(r"\d{1,2}:\d{2}", stripped_line):
    # r"\d{1,2}:\d{2}""
    # \d: a digit    
    # \d{1,2}: repeat \d between 1 and 2 times (aka can be 1 or 2 digits)
    # \d: exactly 2 digits
    # re.fullmatch(): the entire line must match this pattern
        continue  # skip this line

    if stripped_line == "":
        continue

    cleaned_lines.append(line)
    # add the non time-stamped lines

# Save the cleaned transcript to a new file
with open("cleaned_transcript.txt", "w", encoding="utf-8") as file:
    file.writelines(cleaned_lines)
# new files "cleaned_transcript.txt" is created
# clean text is put into the new file
# "w": writing mode
# encoding = "utf-8": tells python how to read or write the text characters (this one supports normal eng letters and others)


print("Done! Timestamps removed and saved to cleaned_transcript.txt")