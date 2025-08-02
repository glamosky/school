type = input("Input your file together with its extension: ")

# map extensions to media types. you can add more extensions to the dictionary if you want.
EXTENSIONS = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg', 
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}

type = type.strip()

"""we have to use rfind since it looks for the LAST dot, a better fallback if there are multiple dots in the filename. 
the if statement handles the case where the extension is in uppercase. the else statement handles the case where there is no extension."""
last_dot = type.rfind('.')
if last_dot != -1:
    extension = type[last_dot:].lower()  # get extension and make lowercase
else:
    extension = ""  # no extension found

# look up in dictionary, return default if not found
media_type = EXTENSIONS.get(extension, 'application/octet-stream')

print(f"The media type of {type} is {media_type}")