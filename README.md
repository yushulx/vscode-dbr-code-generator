# Code Generator for Dynamsoft Barcode SDK 

The Code Generator helps developers to quickly get started with [Dynamsoft Barcode Reader SDK](https://www.dynamsoft.com/barcode-reader/overview/) using JavaScript, Python, C/C++, .NET, Android, and iOS in Visual Studio Code.

## Dynamsoft Barcode Reader Version
v9.0.0

## Supported Platforms
- **Android**
- **iOS**
- **Windows**
- **Linux**
- **macOS**
- **Web**

## Supported Barcode Symbologies
- Linear Barcodes (1D)
  - Code 39 (including Code 39 Extended)
  - Code 93
  - Code 128
  - Codabar
  - Interleaved 2 of 5
  - EAN-8
  - EAN-13
  - UPC-A
  - UPC-E
  - Industrial 2 of 5

- 2D Barcodes
  - QR Code (including Micro QR Code and Model 1)
  - Data Matrix
  - PDF417 (including Micro PDF417)
  - Aztec Code
  - MaxiCode (mode 2-5)
  - DotCode

- Patch Code
- GS1 Composite Code
- GS1 DataBar
  - Omnidirectional,
  - Truncated, Stacked, Stacked
  - Omnidirectional, Limited,
  - Expanded, Expanded Stacked

- Postal Codes
  - USPS Intelligent Mail
  - Postnet
  - Planet
  - Australian Post
  - UK Royal Mail  

## Dev Requirements for Windows, Linux and macOS
- [Visual Studio](https://visualstudio.microsoft.com/downloads/)
- [CMake](https://cmake.org/download/)
- [.NET SDK](https://dotnet.microsoft.com/en-us/download/visual-studio-sdks)
- [Python](https://www.python.org/downloads/)
- [Android Studio](https://developer.android.com/studio)
- [Xcode](https://developer.apple.com/xcode/)

## Usage

### Create DBR Projects
1. Press `F1` to show command palette and run **DBR** to list all supported projects.
    
    ![vscode-dbr-extension](https://www.dynamsoft.com/codepool/img/2022/05/vscode-dbr-extension.png)

2. Select the project you want to generate code for.
3. Build and run the project:
    - **Web**
        ```bash
        python -m http.server
        ```
    - **Python** (**Windows**, **Linux**, and **macOS**)
        ```bash
        pip install dbr pyside2 opencv-python
        python app.py
        ```
    - **.NET** (**Windows**, **Linux**, and **macOS**)
        ```bash
        dotnet restore
        dotnet run
        ```
    - **C/C++** (**Windows**, **Linux**, and **macOS**)
        ```bash
        mkdir build
        cd build

        # if Windows
        cmake -DCMAKE_GENERATOR_PLATFORM=x64 ..
        # else
        cmake ..

        cmake --build .
        ```
    - **Android**
        
        Import the project to Android Studio.

    - **iOS**
        
        Run `pod install` and import the project to Xcode.

### Generate DBR Code Snippets in Python, C/C++, C#, Java, Swift and HTML
In corresponding language files, you can find the code snippets with prefix `dbr`.

![dbr code snippets](https://www.dynamsoft.com/codepool/img/2022/05/vscode-dbr-snippets.gif)
