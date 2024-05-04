
Here you’ll learn how to set up Visual Studio Code for Python development.

## Introduction to the Visual Studio Code


Visual Studio Code is a lightweight source code editor. The Visual Studio Code is often called VS Code. The VS Code runs on your desktop. It’s available for Windows, macOS, and Linux.

VS Code comes with many features such as IntelliSense, code editing, and extensions that allow you to edit Python source code effectively. The best part is that the VS Code is open-source and free.

## Setting up Visual Studio Code

To set up the VS Code, you follow these steps:

First, navigate to the [VS Code official](https://code.visualstudio.com/) website and download the VS code based on your platform (Windows, macOS, or Linux).

Second, launch the setup wizard and follow the steps.

Once the installation is completed, you can launch the VS code application:

Trouble in Installation : -
**Pro Tip** : - Simply search How to install VS code for ( Your OS like- Windows, macOS, or Linux ) on any browser (Suggested Chrome or Brave) now follow the steps and you will successed.

## Install Python Extension

To make the VS Code work with Python, you need to install the Python extension from the Visual Studio Marketplace.

* First, click the **Extensions** tab.
* Second, type the `python` keyword on the search input.
* Third, click the `Python` extension. It’ll show detailed information on the right pane.
* Finally, click the **Install** button to install the Python extension.

Now, you’re ready to develop the program in python using VS code.

**Pro Tip**: - Install one more extenstion which is game changer you only need to click on run button icon and your code will executed.

Extension name :- Code Runner
Simply follow the steps same as you done before for installing python extension, only need to search for code runner instead of python.

After installing this you will see a "run icon" in top right side. Now simply goto the file you want to run and click that "run icon" this will execute the code from that file and open a terminal within the vs code here you can see the output of the program.

 You can also launch the Terminal within the VS code by:

* Accessing the menu **Terminal > New Terminal**
* Or using the keyboard shortcut `Ctrl+Shift+``.

Typically, the backtick key (```) located under the `Esc` key on the keyboard.

## Solution

**If got some error like** -->  /bin/sh: 1: python: not found
Follow this and you will able to solve the error --> 

Step1 : Goto settings of Code Runner extension

Step2 : Find the section

> **Code-runner: Executor Map**

And click on

> **Edit in settings.json**

Step3 : Now change the setting for python

Before

```python
"code-runner.executorMap": {
    ...
    "python": "python -u"
    ...
}
```

Change this to

```python
"code-runner.executorMap": {
    ...
    "python": "python3 -u"
    ...
}
```

Or you can find solution here--> https://stackoverflow.com/questions/61620036/how-to-run-python3-code-in-vscode-bin-sh-1-python-not-found

Note: I'm using linux so process may me little bit differ for other platforms (Windows, Mac OS)

Happy coding.................................................................................................................................
