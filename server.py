from fastmcp import FastMCP

mcp = FastMCP("Simple Math & Text Tools")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse any text string"""
    return text[::-1]

@mcp.tool()
def count_words(text: str) -> int:
    """Count the number of words in a text"""
    return len(text.split())

@mcp.tool()
def to_uppercase(text: str) -> str:
    """Convert text to uppercase"""
    return text.upper()

@mcp.tool()
def to_lowercase(text: str) -> str:
    """Convert text to lowercase"""
    return text.lower()

@mcp.tool()
def calculate_factorial(n: int) -> int:
    """Calculate factorial of a number"""
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@mcp.tool()
def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome"""
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]