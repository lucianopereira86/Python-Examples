![titulo](/docs/titulo.JPG)

# Python-Examples

Simple examples of Python operations.

## Instructions

Inside the '/examples' folder there are multiple files. Each one contains a short example of a Python functionality.

## Topics

- [input.py](#inputpy)
- [error.py](#errorpy)
- [string.py](#stringpy)
- [number.py](#numberpy)
- [date.py](#datepy)
- [error_handling.py](#error_handlingpy)
- [conditional.py](#conditionalpy)
- [collection.py](#collectionpy)
- [loop.py](#looppy)
- [function.py](#functionpy)
- [module.py](#modulepy)
- [venv.py](#venvpy)
- [api\post.py](#api_postpy)

### input.py

A variable receives the result of an input and has its value printed.

![code01](/docs/code01.JPG)

Executing the command below:

```batch
python .\examples\input.py
```

The result is:

![code02](/docs/code02.JPG)

### error.py

Multiple math operations are done sequentially until an error occurs.

![code03](/docs/code03.JPG)

Executing the command below:

```batch
python .\examples\error.py
```

The result is:

![code04](/docs/code04.JPG)

An error occured at line 8 because it was not possible to divide by zero.

### string.py

Using multiple string functions.

![code05](/docs/code05.JPG)

Executing the command below:

```batch
python .\examples\strings.py
```

The result is:

![code06](/docs/code06.JPG)

### number.py

Testing math operations with numbers and numeric strings

![code07](/docs/code07.JPG)

Executing the command below:

```batch
python .\examples\numbers.py
```

The result is:

![code08](/docs/code08.JPG)

### date.py

Testing datetime functions and formats.

![code09](/docs/code09.JPG)

Executing the command below:

```batch
python .\examples\date.py
```

The result is:

![code10](/docs/code10.JPG)

### error_handling.py

Handling runtime errors.

![code11](/docs/code11.JPG)

Executing the command below:

```batch
python .\examples\error_handling.py
```

The result is:

![code12](/docs/code12.JPG)

### conditional.py

Conditional logic examples.

![code13](/docs/code13.JPG)

Executing the command below:

```batch
python .\examples\conditional.py
```

The result is:

![code14](/docs/code14.JPG)

### collection.py

Manipulating arrays and lists.

![code15](/docs/code15.JPG)

Executing the command below:

```batch
python .\examples\collection.py
```

The result is:

![code16](/docs/code16.JPG)

### loop.py

Controlling loops.

![code17](/docs/code17.JPG)

Executing the command below:

```batch
python .\examples\loop.py
```

The result is:

![code18](/docs/code18.JPG)

### function.py

Creating functions.

![code19](/docs/code19.JPG)

Executing the command below:

```batch
python .\examples\function.py
```

The result is:

![code20](/docs/code20.JPG)

### module.py

Importing the "math_module.py".

![code21](/docs/code21.JPG)

Using its functions.

![code22](/docs/code22.JPG)

Executing the command below:

```batch
python .\examples\module.py
```

The result is:

![code23](/docs/code23.JPG)

### venv.py

Create a virtual environment, install a package and use it in a module.

Execute the command below to create a folder called 'venv':

```bash
python -m venv venv
```

Press the 'Yes' button inside the popup that shows up inside the VSCode.

![code24](/docs/code24.JPG)

The virtual environment will be available in the project root folder.

![code25](/docs/code25.JPG)

Run the command below to use it:

```bash
.\venv\Scripts\Activate.ps1
```

The word '(venv)' will be visible in the left side of the current path.

![code26](/docs/code26.JPG)

And at the bottom of the VSCode, as well.

![code27](/docs/code27.JPG)

Create a file named 'requirements.txt' at the project root folder and type 'colorama' inside of it.

![code28](/docs/code28.JPG)

Install the colorama package inside the venv with the following command:

```bash
pip install -r requirements.txt
```

The result will be:

![code29](/docs/code29.JPG)

Import _colorama_ inside the _math_module.py_ to write colored messages.

![code30](/docs/code30.JPG)

Finally, run the command below:

```bash
python .\examples\module.py
```

The result will be:

![code31](/docs/code31.JPG)

### api\post.py

Example of a POST request to a web API.

![code32](/docs/code32.JPG)

First, install the 'requests' library:

```bash
pip install requests
```

The result will be:

![code33](/docs/code33.JPG)

Then, run this command:

```bash
python .\examples\api\post.py
```

The result will be:

![code34](/docs/code34.JPG)

## References

Many of these examples are based on those found in the [Python for Beginners](https://www.youtube.com/watch?v=jFCNu1-Xdsw&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6) series, presented by Microsoft.
