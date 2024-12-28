import os
import subprocess
import tempfile
#import notepad
#import editor

# Path to Tidy executable
TIDY_PATH = r"C:\Program Files (x86)\Notepad++\plugins\Tidy\Tidy.exe"

# Get the current content from the active document in Notepad++
current_content = editor.getText()

# Create a temporary file in the system's temp directory
temp_file_handle, temp_file_path = tempfile.mkstemp(suffix=".au3")
os.close(temp_file_handle)

try:
    # Write the current content to the temporary file
    with open(temp_file_path, 'w', encoding='utf-8', newline='') as temp_file:
        temp_file.write(current_content)

    # Run Tidy on the temporary file
    subprocess.run([TIDY_PATH, temp_file_path])

    # Read the formatted content from the temporary file
    with open(temp_file_path, 'r', encoding='utf-8') as temp_file:
        formatted_content = temp_file.read()

    # Replace the content of the current tab with the formatted content
    editor.beginUndoAction()
    editor.clearAll()
    editor.insertText(0, formatted_content)
    editor.endUndoAction()

finally:
    # Clean up the temporary file
    os.remove(temp_file_path)