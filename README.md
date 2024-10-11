# Give_name_to_files_in_serial_number
in this program we rename the file name in to a serial number 
This Python script renames all PDF files in a specified directory, assigning them sequential numbers (e.g., `1.pdf`, `2.pdf`, etc.).

### Explanation:

1. **Importing `os` module**: The script uses the `os` module to interact with the file system.
2. **Listing Files**: `os.listdir("meargpdf")` lists all the files in the specified directory `"meargpdf"`.
3. **Loop Through Files**: A loop checks each file in the directory:
   - If the file has a `.pdf` extension (`file.endswith(".pdf")`), it's processed.
4. **Renaming Files**: `os.rename()` is used to rename each PDF file to a number. For example:
   - `file` is renamed to `1.pdf`, `2.pdf`, etc.
5. **Incrementing the Counter**: The counter `i` increments with each PDF file to maintain the numbering.

### Example Output:

```
report1.pdf
1.pdf
summary.pdf
2.pdf
```

In this example, all `.pdf` files in the directory are renamed to sequential numbers. Make sure to update the directory path in the code as needed.
