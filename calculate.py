import math

# Function to check if the input is numeric
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Get user inputs for a, b, and c
a = input("Enter the value for a: ")
b = input("Enter the value for b: ")
c = input("Enter the value for c: ")

# Check if a, b, and c are numeric
if not (is_numeric(a) and is_numeric(b) and is_numeric(c)):
    print("Error: All inputs must be numeric.")
else:
    # Convert the inputs to float
    a = float(a)
    b = float(b)
    c = float(c)

    # Perform conditional checks and calculations
    if a < 1:
        print("The value of 'a' is too small.")
    elif b == 0:
        print("The value of 'b' will not affect the result.")
    
    if c < 0:
        print("Error: The value of 'c' cannot be negative.")
    else:
        c_cubed = c ** 3
        print(f"The value of c^3 is: {c_cubed}")
        
        # Calculate the result based on the condition for c^3
        if c_cubed > 1000:
            result = math.sqrt(c_cubed) * 10
        else:
            result = math.sqrt(c_cubed) / a
        
        # Add b to the result
        result += b
        
        # Generate HTML output
        html_output = f"""
        <html>
        <head><title>Calculation Result</title></head>
        <body>
            <h1>Calculation Results</h1>
            <p>Value of a: {a}</p>
            <p>Value of b: {b}</p>
            <p>Value of c: {c}</p>
            <p>Result: {result}</p>
        </body>
        </html>
        """
        
        # Print the HTML output to the console (or save to a file if desired)
        with open("result.html", "w") as file:
            file.write(html_output)
        
        print("Calculation complete. Results saved in 'result.html'.")
