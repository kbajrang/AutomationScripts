# Define the input and output folders
$input_folder = "C:\Users\kaila\OneDrive\Desktop\Dump"
$output_folder = "C:\Users\kaila\OneDrive\Desktop\Dump\DDumps"

# Create the output folder if it doesn't exist
New-Item -ItemType Directory -Force -Path $output_folder

# Read package names from the text file
Get-Content "$input_folder\apks.txt" | ForEach-Object {
    $package_name = $_.Trim() -replace '^package:', ''  # Trim to remove leading/trailing whitespaces and remove "package:"

    # Generate dump for each package
    adb shell dumpsys package "$package_name" | Out-File -FilePath "$output_folder\$package_name.txt" -Encoding UTF8

    # Print a message indicating completion
    Write-Host "Dump for $package_name generated and saved in $output_folder\$package_name.txt"
}
