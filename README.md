## Calculator 

Simple inputs. Handles two numbers and one operation at a time. 


![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/PyQt6-512BD4?style=for-the-badge&logo=python&logoColor=white)


---

## Screenshots

<p align="center">
  <img src="https://lh3.googleusercontent.com/d/16RAB2sc5SgkDcN0T6Ue7XOSczrmsSHgD" alt="Calculator App Screenshot">
</p>

<p align="center">
  <img src="https://lh3.googleusercontent.com/d/19l7AV4TV330T6iBizhTAf0Ftb2BCVphW" alt="Calculator App Screenshot 2">
</p>

<p align="center">
  <img src="https://lh3.googleusercontent.com/d/1DZbNxP1cf8-mb-gu6CnYJVo19lZ6YcIG" alt="Calculator App Screenshot 3">
</p>

<p align="center">
  <img src="https://lh3.googleusercontent.com/d/1P7llXTmpn7qImBULVMj3vyTpCTkjA7da" alt="Calculator App UI">
</p>


---

## Platform Compatibility

- Tested to work on Windows 11 properly. UI looks fine.
- Might not work well with Linux distributions

---

## Try it

<a href="https://drive.google.com/uc?export=download&id=1xAALMAyzZl4ewpXzfnpBtmKhxRqHxnWz">Download EXE File</a>


---


## Architectural Notes

Everything starts from `main.py`

It creates the calculator window object, which further initializes the UI elements and the styling.

Clicking on any button calls the connector module which applies the logic behind that specific button.

Furthermore, the expressions are calculated using `sympy.sympify()` which parses and resolves the expressions. One important thing to note is that if the answer is a fraction, it will return the fraction as a string rather than a decimal number.


---


## Documentation 

> The code is mostly self-documented using python type hints and docstrings.
> 
> These bellow are details of what each module does. (click to expand)

<!-- logic dir -->
<details>
  <summary><code>./logic/</code></summary>
  <br />
  <blockquote>Logic for the functionality of the calculator. Basically, sub-modules that help perform calculations</blockquote>
  <details>
    <summary><code>./logic/operator</code></summary>
    <br />
    <blockquote>Main sub-module for calculation functions that solve expressions</blockquote>
    <br />
  </details>
  <details>
    <summary><code>./logic/expression</code></summary>
    <br />
    <blockquote>Expression class to "contain" the expression in two forms: a calculatable, and a displayable string</blockquote>
  </details>
  <br />
</details>

<!-- ui dir -->
<details>
  <summary><code>./ui/</code></summary>
  <br />
  <blockquote>Houses code for initializing, styling and handling UI</blockquote>
  <details>
    <summary><code>./ui/elements</code></summary>
    <br />
    <blockquote>This module has classes for each UI element the calculator has.</blockquote>
    <br />
  </details>
  <details>
    <summary><code>./ui/calculator</code></summary>
    <br />
    <blockquote>Main calculator file. Initializes the main app, it's layout, and calls functions to initialize it's elements</blockquote>
  </details>
  <details>
    <summary><code>./ui/styling</code></summary>
    <br />
    <blockquote>Styling sub-module with functions to style elements of the calculator.</blockquote>
  </details>
  <br />
</details>

<!-- connector module -->
<details>
  <summary><code>./connector</code></summary>
  <br />
  <blockquote>The bridge between the UI and the logic functions. This allows the UI to use the logic functions with adapter-style functions.</blockquote>
  <br />
</details>

<!-- engine module -->
<details>
  <summary><code>./engine</code></summary>
  <br />
  <blockquote>The boss. This is where the workflow starts running.</blockquote>
  <blockquote>Any normal run of the calculator is done with 'python engine.py'. This file also decides whether to run the calculator in debug mode.</blockquote>
  <br />
</details>

<!-- exceptions module -->
<details>
  <summary><code>./exceptions</code></summary>
  <br />
  <blockquote>This module defines all kinds of exceptions that can occur in the app. Exceptions and their reason of occurence is documented with each function using google-style function docstrings.</blockquote>
  <br />
</details>

<!-- tests module -->
<details>
  <summary><code>./tests</code></summary>
  <br />
  <blockquote>This contains module-by-module tests for the codebase. Verifies that the modules are working properly with each other to carry out their expected functions.</blockquote>
  <br />
</details>


---


## Developer Setup

- Clone this repository:

```bash
git clone https://github.com/ShahzaibAhmad05/calculator-python
```

- Make sure you have python 3.13 or above.

- Create a virtual environment and activate it:

```bash
python -m venv .venv
# the activation command is different depending on OS, figure it out yourself
```

- Install the requirements (only one):

```bash
pip install -r requirements.txt
```

- Run from the engine file:

```bash
python main.py
```

That's the GUI.

