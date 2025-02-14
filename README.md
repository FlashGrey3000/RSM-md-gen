# RSM-style Markdown Generator

This repo is *under development*. Open Source contributions are welcome *(and appreciated!)*.  

Made particularly for the course *UCS2403 - Design and Analysis of Algorithms.* Cause creating the entire documentation for each question is 😭  

## TODO
- Add the `unittest` section
- Add CSS styling to HTML documentation
- Fix the copy-to-clipboard button
- Enhance PDF parsing and improve text extraction accuracy
- Improve error handling and logging
- Add support for more Markdown flavors (maybe a shakespearean theme because sir likes it a lot ig)
- Disable and add a loading button after <kbd>generate markdown</kbd> is clicked

## Important Info
- The site is running on [`render`](https://render.com/), and due its free deployment limitations the **server takes around 1 minute to load up the first time after long inactivity.** Please be patient.
- When clicking on the <kbd>generate markdown</kbd>, it makes a few calls to the `Groq API` for the entire documentation. Number of calls/tokens per day is limited, **so please don't abuse it**
- The unittest api call hasn't been added yet.
- You can use this tool to complete the cumbersome parts, but I'd recommend to not use this to directly finish your assignments. The AI can not be trusted, please review the entire information multiple times. *(At least)*.


## Disclaimer
This project was created to make documentation easier and more efficient for the UCS2403 course. However, writing your own documentation is an essential skill in the industry and a good coding practice. This tool aims to assist just in case, not replace the learning experience. ~~Although I believe creating documentations for algorithms isn't best way to learn it.~~

## Contributing
Open-source contributions are heavily encouraged! If you find an issue or an area for improvement *(please help)*:

1. **Report it:** Create an issue in the GitHub Issues section describing the problem or feature request.
2. **Fix it:** Fork the repository, make your changes, and test them.
3. **Submit a PR:** Open a pull request with a clear description of the fix or enhancement.
4. **Review & Merge:** Once reviewed, your contribution will be merged into the project!

## Program Flow
Below is a high-level overview of how the program processes input and generates Markdown:

1. User uploads the pdf file of the assignment.  
![homepage](/imgs/homepage.png)

2. The system parses the input and applies formatting rules. The user has to fix it in case because pdf parsing is very bad rn  
![quesblocks](/imgs/quesblocks.png)

3. Markdown is generated based on a predefined template. **PLEASE NOTE THAT MARKDOWN GENERATION CAN TAKE UPTO 2 MINUTES**  
![generated md](/imgs/generatedMD.png)

4. The user can copy the Markdown code to clipboard (sometimes has issues) or can copy it directly.    

You can check out an example Markdown file generated [here](/sample_readme.md)