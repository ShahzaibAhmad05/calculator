## GUI-based Calculator

Simple inputs. Handles two numbers and one operation at a time.


## Screenshots

![Calculator Demo](https://lh3.googleusercontent.com/d/1qmJnaHaNTClUwiuom7mkL4r1suFoBkig)


<table>
  <tr>
    <td><a href="">Download the Exe</a></td>
  </tr>
</table>


## Documentation 

> The code is mostly self-documented using python type hints and docstrings.
> 
> These bellow are details of what each module does. (click to expand)

<!-- logic dir -->
<details>
  <summary><code>./logic/</code></summary>
  <br />
  <blockquote>Logic for the functionality of the calculator. Basically, functions that perform calculations</blockquote>
  <details>
    <summary><code>./logic/operators</code></summary>
    <br />
    <blockquote>Main logic file housing basic calculation functions</blockquote>
    <br />
  </details>
  <details>
    <summary><code>./logic/utils</code></summary>
    <br />
    <blockquote>Utility functions, currently has only one function which is for decoding the operator class</blockquote>
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
    <!-- I was working here -->
    <blockquote>This module has classes for each UI element the calculator has. UI elements import styling functions from</blockquote>
    <br />
  </details>
  <details>
    <summary><code>./ui/calculator</code></summary>
    <br />
    <blockquote>Main calculator file. Initializes the app, calls functions to initialize it's elements</blockquote>
  </details>
  <br />
</details>


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
python engine.py
```

That's the GUI.

