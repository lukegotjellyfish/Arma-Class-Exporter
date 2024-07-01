import ast
import operator as op
from decimal import Decimal

# Some mod authors like using string values for int config parameters that
#  require the game to evaluate the expressions to get a number
#  this is not good for numerical operations.
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
}


def decimalize(value: int|float|str) -> Decimal:
    """
    Convert a value/expression to a decimal.



    Parameters:
        value (int|float|str): The value to convert.

    Returns:
        Decimal: The converted value.
    """
    match value:
        case int() | float():
            return Decimal(value)
        case str():
            return Decimal(eval_expr(value))
    return Decimal(value)


def eval_expr(expr):
    """
    Evaluate a mathematical expression given as a string.

    :Parameters
        expr (str): The expression to evaluate.

    Returns:
        float: The result of the evaluation.
    """
    try:
        node = ast.parse(expr, mode='eval').body
        return eval_(node)
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")


def eval_(node):
    """
    Recursively evaluate an AST node.

    Parameters:
        node (ast.AST): The root node of the AST.

    Returns:
        any: The result of the evaluation.
    """
    if isinstance(node, ast.Constant):  # <number>
        return node.value
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        left = eval_(node.left)
        right = eval_(node.right)
        if type(node.op) in operators:
            return operators[type(node.op)](left, right)
        else:
            raise ValueError(f"Unsupported operator: {ast.dump(node.op)}")
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        operand = eval_(node.operand)
        if type(node.op) in operators:
            return operators[type(node.op)](operand)
        else:
            raise ValueError(f"Unsupported unary operator: {ast.dump(node.op)}")
    else:
        raise ValueError(f"Unsupported node type: {ast.dump(node)}")