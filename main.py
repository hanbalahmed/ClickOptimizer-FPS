import os

# Prompt user for Minecraft version location
version_location = input(
    "Enter the location of the Minecraft version folder (e.g. C:/Users/Username/AppData/Roaming/.minecraft/versions/1.19.1/): ")

# Set the path to the options files
options_path = os.path.join(version_location, "options.txt")
optionsof_path = os.path.join(version_location, "optionsof.txt")

# Open and read the contents of the options.txt file
with open(options_path, "r") as f:
    options_contents = f.readlines()

# Open and read the contents of the optionsof.txt file
with open(optionsof_path, "r") as f:
    optionsof_contents = f.readlines()

# Modify the options.txt file
for i in range(len(options_contents)):
    if options_contents[i].startswith("clouds"):
        options_contents[i] = "clouds:0\n"
    elif options_contents[i].startswith("particles"):
        options_contents[i] = "particles:Minimal\n"
    elif options_contents[i].startswith("fog"):
        options_contents[i+1] = "fog:Fast\n"

# Modify the optionsof.txt file
for i in range(len(optionsof_contents)):
    if optionsof_contents[i].startswith("ofRenderDistanceChunks"):
        optionsof_contents[i] = "ofRenderDistanceChunks:2\n"
    elif optionsof_contents[i].startswith("ofFastRender"):
        optionsof_contents[i] = "ofFastRender:true\n"
    elif optionsof_contents[i].startswith("ofFastMath"):
        optionsof_contents[i] = "ofFastMath:true\n"

# Write the modified contents back to the options.txt file
with open(options_path, "w") as f:
    f.writelines(options_contents)

# Write the modified contents back to the optionsof.txt file
with open(optionsof_path, "w") as f:
    f.writelines(optionsof_contents)

# Print a confirmation message
print("Settings changed successfully!")
