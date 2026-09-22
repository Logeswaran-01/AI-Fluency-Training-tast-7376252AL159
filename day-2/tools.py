"""Tools the agent is allowed to use, plus their JSON Schema descriptions."""
import ast
import operator
from config import TRIP_PRICES
 
def get_trip_price(item_code: str) -> str:
    """Look up the price for one trip item code."""
    price = TRIP_PRICES.get(item_code.strip().upper())
    return str(price) if price is not None else f"Unknown item code: {item_code}"
 
# A safe calculator: only numbers and + - * / ( ) are allowed. Never use eval().
_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.USub: operator.neg}
 
def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.left), _evaluate(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_evaluate(node.operand))
    raise ValueError("Unsupported expression")
 
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression such as (12000 + 18000) * 0.9."""
    try:
        return str(_evaluate(ast.parse(expression, mode="eval").body))
    except Exception as error:
        return f"Calculator error: {error}"
 
TOOL_FUNCTIONS = {"get_trip_price": get_trip_price, "calculator": calculator}
 
# These descriptions are what the LLM reads when deciding which tool to call
TOOLS = [
    {"type": "function", "function": {
        "name": "get_trip_price",
        "description": "Get the price in rupees for a single trip item code, for example FLIGHT or HOTEL_3STAR.",
        "parameters": {"type": "object",
                       "properties": {"item_code": {"type": "string"}},
                       "required": ["item_code"]}}},
    {"type": "function", "function": {
        "name": "calculator",
        "description": "Evaluate an arithmetic expression using + - * / and brackets.",
        "parameters": {"type": "object",
                       "properties": {"expression": {"type": "string"}},
                       "required": ["expression"]}}},
]
 
if __name__ == "__main__":
    print("get_trip_price('hotel_3star') ->", get_trip_price("hotel_3star"))
    print("calculator('(9200 + 7600) * 0.95') ->", calculator("(9200 + 7600) * 0.95"))
    print("calculator('11000 - 7600') ->", calculator("11000 - 7600"))