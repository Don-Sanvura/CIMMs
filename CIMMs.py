"""
COMPREHENSIVE PYTHON LOGIC DEMONSTRATION
This script covers fundamental Python concepts with detailed explanations.
References: 
- Ramalho, L. (2022). Fluent Python
- Slatkin, B. (2020). Effective Python
- Python Software Foundation. (2024). Python Documentation
"""

# =============================================================================
# 1. PYTHON OBJECT MODEL & MUTABILITY
# =============================================================================

def demonstrate_object_model():
    """
    Demonstrates Python's object model and the concept of mutability.
    Key concept: Everything in Python is an object with identity, type, and value.
    """
    
    print("=== OBJECT MODEL & MUTABILITY ===")
    
    # Immutable objects (cannot be changed after creation)
    x = 10          # integer - immutable
    y = "hello"     # string - immutable  
    z = (1, 2, 3)   # tuple - immutable
    
    # Mutable objects (can be changed after creation)
    a_list = [1, 2, 3]          # list - mutable
    a_dict = {'key': 'value'}    # dictionary - mutable
    a_set = {1, 2, 3}           # set - mutable
    
    print(f"Integer (immutable): {x}, id: {id(x)}")
    print(f"List (mutable): {a_list}, id: {id(a_list)}")
    
    # Demonstrate mutability in action
    original_list = [1, 2, 3]
    list_reference = original_list  # Both names point to SAME object
    
    list_reference.append(4)  # Modifies the shared object
    
    print(f"Original list after modification: {original_list}")
    print(f"Both point to same object: {original_list is list_reference}")
    
    # For immutable objects, "modification" creates a new object
    original_string = "hello"
    new_string = original_string + " world"  # Creates NEW string object
    
    print(f"Original string unchanged: '{original_string}'")
    print(f"New string: '{new_string}'")
    print(f"Different objects: {original_string is not new_string}")

# =============================================================================
# 2. FUNCTION ARGUMENT HANDLING - COMMON PITFALLS
# =============================================================================

def dangerous_default_argument(item, target_list=[]):
    """
    DANGEROUS: Default mutable argument pattern.
    The default list is created ONLY once when the function is defined.
    This leads to unexpected behavior across multiple calls.
    
    Citation: Ramalho, L. (2022). Fluent Python - Chapter 6
    """
    target_list.append(item)
    return target_list

def safe_default_argument(item, target_list=None):
    """
    SAFE: Proper way to handle default mutable arguments.
    Create a new mutable object inside the function if none provided.
    """
    if target_list is None:
        target_list = []  # New list created each time function is called
    target_list.append(item)
    return target_list

def demonstrate_function_pitfalls():
    """Demonstrates common function-related pitfalls and proper patterns."""
    
    print("\n=== FUNCTION ARGUMENT PITFALLS ===")
    
    # Dangerous pattern demonstration
    print("Dangerous default argument behavior:")
    result1 = dangerous_default_argument(1)
    result2 = dangerous_default_argument(2)  # Unexpectedly shares the list!
    print(f"First call: {result1}")
    print(f"Second call: {result2}")  # Output: [1, 2] - Not expected!
    
    # Safe pattern demonstration
    print("\nSafe default argument behavior:")
    result1 = safe_default_argument(1)
    result2 = safe_default_argument(2)  # Creates new list each time
    print(f"First call: {result1}")  # Output: [1]
    print(f"Second call: {result2}")  # Output: [2] - As expected!

# =============================================================================
# 3. PYTHONIC CONSTRUCTS & IDIOMS
# =============================================================================

def demonstrate_pythonic_patterns():
    """
    Demonstrates Pythonic ways of writing code that are efficient and readable.
    Citation: Slatkin, B. (2020). Effective Python - Item 7: Use list comprehensions
    """
    
    print("\n=== PYTHONIC PATTERNS ===")
    
    # Traditional vs Pythonic list creation
    numbers = [1, 2, 3, 4, 5]
    
    # Non-Pythonic way (verbose)
    squares_verbose = []
    for num in numbers:
        squares_verbose.append(num ** 2)
    
    # Pythonic way using list comprehension (concise and faster)
    squares_pythonic = [num ** 2 for num in numbers]
    
    print(f"Numbers: {numbers}")
    print(f"Squares (verbose): {squares_verbose}")
    print(f"Squares (pythonic): {squares_pythonic}")
    
    # Generator expressions for memory efficiency
    print("\nGenerator Expressions (memory efficient):")
    
    # List comprehension - creates entire list in memory
    big_list = [x * 2 for x in range(1000)]  # Stores all 1000 elements
    
    # Generator expression - yields items one at a time
    big_generator = (x * 2 for x in range(1000))  # Creates generator object
    
    print(f"Type of list: {type(big_list)}")
    print(f"Type of generator: {type(big_generator)}")
    print(f"Generator first few values: {[next(big_generator) for _ in range(5)]}")

# =============================================================================
# 4. CONTEXT MANAGERS & RESOURCE HANDLING
# =============================================================================

class DatabaseConnection:
    """Simulates a database connection to demonstrate context managers."""
    
    def __init__(self, database_name):
        self.database_name = database_name
        self.connected = False
    
    def connect(self):
        """Simulate connecting to database."""
        self.connected = True
        print(f"Connected to {self.database_name}")
    
    def disconnect(self):
        """Simulate disconnecting from database."""
        self.connected = False
        print(f"Disconnected from {self.database_name}")
    
    # Context manager protocol methods
    def __enter__(self):
        """Called when entering 'with' block."""
        self.connect()
        return self  # This object is assigned to the 'as' variable
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting 'with' block, even if exception occurs."""
        self.disconnect()
        # Return False to propagate exceptions, True to suppress them
        return False

def demonstrate_context_managers():
    """
    Demonstrates proper resource management using context managers.
    The 'with' statement ensures resources are properly cleaned up.
    
    Citation: Python Documentation - Context Manager Types
    """
    
    print("\n=== CONTEXT MANAGERS ===")
    
    # Proper resource management with context manager
    print("Using context manager (recommended):")
    with DatabaseConnection("my_database") as db:
        print(f"Database is connected: {db.connected}")
        # Connection automatically closed when leaving 'with' block
    # Connection is automatically disconnected here
    
    # Manual resource management (error-prone)
    print("\nManual resource management (not recommended):")
    db = DatabaseConnection("manual_db")
    try:
        db.connect()
        print(f"Database is connected: {db.connected}")
    finally:
        db.disconnect()  # Easy to forget this!

# =============================================================================
# 5. ADVANCED FUNCTION FEATURES
# =============================================================================

def demonstrate_advanced_functions():
    """
    Demonstrates advanced Python function features.
    """
    
    print("\n=== ADVANCED FUNCTION FEATURES ===")
    
    # Lambda functions (anonymous functions)
    square = lambda x: x ** 2
    print(f"Lambda function - square(5): {square(5)}")
    
    # Using lambda with map and filter (functional programming)
    numbers = [1, 2, 3, 4, 5, 6]
    even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
    print(f"Even squares: {even_squares}")
    
    # Equivalent using list comprehensions (more Pythonic)
    even_squares_pythonic = [x ** 2 for x in numbers if x % 2 == 0]
    print(f"Even squares (pythonic): {even_squares_pythonic}")

# =============================================================================
# 6. CLASSES AND INHERITANCE
# =============================================================================

class Animal:
    """Base class demonstrating Python class features."""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement speak()")
    
    def __str__(self):
        """String representation of the object."""
        return f"{self.name} the {self.species}"
    
    def __repr__(self):
        """Official string representation for debugging."""
        return f"Animal(name='{self.name}', species='{self.species}')"

class Dog(Animal):
    """Subclass demonstrating inheritance."""
    
    def __init__(self, name, breed):
        # Call parent class constructor
        super().__init__(name, "Dog")
        self.breed = breed
    
    def speak(self):
        """Override parent class method."""
        return "Woof!"
    
    def __str__(self):
        """Extend parent's string representation."""
        return f"{super().__str__()} ({self.breed})"

def demonstrate_classes():
    """Demonstrates Python class features and inheritance."""
    
    print("\n=== CLASSES AND INHERITANCE ===")
    
    # Create instances
    generic_animal = Animal("Generic", "Unknown")
    my_dog = Dog("Buddy", "Golden Retriever")
    
    print(f"Animal: {generic_animal}")
    print(f"Dog: {my_dog}")
    print(f"Dog speaks: {my_dog.speak()}")
    
    # Demonstrate method resolution order
    print(f"Method Resolution Order for Dog: {Dog.__mro__}")

# =============================================================================
# 7. ERROR HANDLING - PYTHONIC WAY
# =============================================================================

def demonstrate_error_handling():
    """
    Demonstrates proper error handling in Python.
    Python philosophy: "Easier to ask for forgiveness than permission" (EAFP)
    """
    
    print("\n=== ERROR HANDLING ===")
    
    # Non-Pythonic: Look Before You Leap (LBYL)
    def lbyl_approach(data, key):
        """Check if key exists before accessing."""
        if key in data:
            return data[key]
        else:
            return None
    
    # Pythonic: Easier to Ask for Forgiveness than Permission (EAFP)
    def eafp_approach(data, key):
        """Try to access and handle exception if it fails."""
        try:
            return data[key]
        except KeyError:
            return None
    
    sample_dict = {'a': 1, 'b': 2}
    
    print("LBYL result for 'a':", lbyl_approach(sample_dict, 'a'))
    print("EAFP result for 'a':", eafp_approach(sample_dict, 'a'))
    print("LBYL result for 'z':", lbyl_approach(sample_dict, 'z'))
    print("EAFP result for 'z':", eafp_approach(sample_dict, 'z'))

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    """
    Main execution block. This code only runs when the script is executed directly,
    not when it's imported as a module.
    """
    
    print("PYTHON LOGIC & FUNCTIONALITY DEMONSTRATION")
    print("=" * 50)
    
    # Run all demonstrations
    demonstrate_object_model()
    demonstrate_function_pitfalls()
    demonstrate_pythonic_patterns()
    demonstrate_context_managers()
    demonstrate_advanced_functions()
    demonstrate_classes()
    demonstrate_error_handling()
    
    print("\n" + "=" * 50)
    print("DEMONSTRATION COMPLETE")
    print("\nKey Takeaways:")
    print("1. Understand Python's object model and mutability")
    print("2. Use context managers for resource handling")
    print("3. Prefer Pythonic constructs (comprehensions, EAFP)")
    print("4. Avoid mutable default arguments")
    print("5. Use proper error handling patterns")
