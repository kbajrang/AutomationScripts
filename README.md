# Android Data Pipeline for Model Input Generation

## Overview

This repository contains a data pipeline for generating model input using Android Debug Bridge (ADB). 
The pipeline involves creating a list of packages and generating ADB dumps for these packages.
 Due to limitations in Kotlin libraries for retrieving specific static features, ADB is leveraged to extract a comprehensive set of features.

## Prerequisites

- Android Debug Bridge (ADB) installed on your machine
- Kotlin libraries limitations in accessing required static features

## Setup



1. **Create a List of Packages:**
   - Edit the `apks.txt` file to include the list of Android package names for which you want to generate dumps.

2. **Run the Data Pipeline:**
   - Execute the PowerShell script to initiate the data pipeline:
     ```powershell
     PowerShell -NoProfile -ExecutionPolicy Bypass -File 'GenerateDumps.ps1'
     ```
     Ensure that the script path and filenames are correctly set.

3. **Generated Dumps:**
   - The dumps for each package will be generated in the 'DDumps' folder. The filenames will correspond to the package names.

## Notes

- ADB is utilized to create comprehensive data dumps, capturing features not easily accessible through Kotlin libraries.
- The generated dumps may have a different format than the model's input format. A parsing script is provided ('ParseDump.ps1') to convert dumps into a format compatible with the model's input requirements.

## Directory Structure

- `GenerateDumps.ps1`: PowerShell script to initiate the data pipeline.
- `ParseDump.ipynb`: PowerShell script for parsing ADB dumps into the required model input format.
- `package_names.txt`: Text file containing a list of Android package names.
- `DDumps/`: Folder containing the generated dumps.

