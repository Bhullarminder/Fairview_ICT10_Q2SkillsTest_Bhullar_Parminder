from pyscript import display, document

def elements(e):
    # Gets the value from the inputted text field
    Element = document.getElementById("Element").value

    # Gets the information from the dictionary
    element_display = non_metals.get(Element, ["Not a nonmetal", "", ""])

    # Formats the values
    document.getElementById("result").innerHTML = f"""
     <b> Symbol: <b> {Element} <br>
     <b>  Element: <b> {element_display[0]} <br>
     <b>  Atomic number: <b> {element_display[1]} <br>
     <b>  Atomic mass: <b> {element_display[2]} <br>
    """


# Different data types compiled in one dictionary
non_metals = {
    "H": ["Hydrogen", 1, 1.008],
    "He": ["Helium", 2, 4.003],
    "C": ["Carbon", 6, 12.011],
    "N": ["Nitrogen", 7, 14.007],
    "O": ["Oxygen", 8, 15.999],
    "F": ["Fluorine", 9, 18.998],
    "Ne": ["Neon", 10, 20.180],
    "P": ["Phosphorus", 15, 30.974],
    "S": ["Sulfur", 16, 32.06],
    "Cl": ["Chlorine", 17, 35.45],
    "Ar": ["Argon", 18, 39.948],
    "Se": ["Selenium", 34, 78.971],
    "Br": ["Bromine", 35, 79.904],
    "Kr": ["Krypton", 36, 83.798],
    "I": ["Iodine", 53, 126.904],
    "Xe": ["Xenon", 54, 131.293]
}