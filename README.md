# Stop doing your math homework
Tool collection to automate the solution of mathematical exercises

```py
import sdymh
sdymh.thank_you() # :)
```

## Installation
If you don't know what is programming, try with [this method](#installation-for-newbies).

Be sure you installed Python 3 and Git. \
Clone the repository : `git clone https://github.com/antoninhrlt/sdymh`

## Usage
> You will probably need to install dependencies by running `pip3 install -r requirements.txt`
> 
After sdymh has been installed, we can now use it. I made a file to simplify 
everything for everyone, open `use.py` in your favorite editor, **do not delete
the current content**, and start calling super sdymh functions :)

To run what you did, type : `python3 use.py` in your command shell.

> Let's check the [wiki](https://github.com/antoninhrlt/sdymh/wiki) to know
> which functions to call

 - ## Example
    ```py
    ...

    values = [
        1.86, 1.88, 1.84, 1.84, 
        1.90, 1.88, 1.88, 1.88, 
        1.86, 1.86, 1.88, 1.86, 
        1.84, 1.86, 1.88
    ]

    sdymh.stats.generate_headcount_table(values)
    ```
    Will be show you, this :
    ```
    value           | 1.84  | 1.86  | 1.88  | 1.9   | total | 
    headcount       | 3     | 5     | 6     | 1     | 15    |
    ```

## Installation for newbies
At first, we need to install the "Python" program, don't worry, it's simple.
On Windows 10, open the Microsoft Store, type "python 3" in the search bar, 
select the latest version, and click to "install" or go [here](https://python.org).

Open the Windows command shell : *Windows logo key* + R, and then type "cmd". \
Check if python is installed by writing : `python3 --version`.

If not, try another way to install Python (Google is here to help you or submit
an issue on this repository to get help)

Congratulations ! Now, check [usage](#usage).
