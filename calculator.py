import tkinter as tk
import ast, operator, traceback


OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.FloorDiv: operator.floordiv,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

def _ast_eval(node):
    if isinstance(node, ast.BinOp):
        left = _ast_eval(node.left)
        right = _ast_eval(node.right)
        op_type = type(node.op)
        if op_type in OPS:
            return OPS[op_type](left, right)
        raise ValueError(f"Unsupported operator: {op_type.__name__}")
    if isinstance(node, ast.UnaryOp):
        operand = _ast_eval(node.operand)
        op_type = type(node.op)
        if op_type in OPS:
            return OPS[op_type](operand)
        raise ValueError("Unsupported unary operator")
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only integers and floats are allowed")
    if isinstance(node, ast.Num):  # older nodes
        return node.n
    raise ValueError(f"Unsupported expression element: {type(node).__name__}")

def safe_eval(expr):
    
    expr = expr.replace('−', '-')
   
    parsed = ast.parse(expr, mode='eval')
    return _ast_eval(parsed.body)

expression = ""

def press(ch):
    global expression
    expression += str(ch)
    print(f"Pressed: {ch!r}  -> expression now: {expression!r}")
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equalpress():
    global expression
    try:
        print("Evaluating expression:", expression)
    
        if expression.strip() == "":
            raise ValueError("Empty expression")
        result = safe_eval(expression)
        equation.set(str(result))
        print("Result:", result)
        expression = ""
    except Exception as e:
        tb = traceback.format_exc()
        print("Error while evaluating:\n", tb)
        equation.set("error: " + str(e))
        expression = ""


gui = tk.Tk()
gui.title("Basic Calculator (debug)")
gui.geometry("320x380")

equation = tk.StringVar()
entry = tk.Entry(gui, textvariable=equation, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, ipady=8, pady=10, padx=8, sticky='we')

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

for (text, r, c) in buttons:
    if text == '=':
        btn = tk.Button(gui, text=text, height=2, width=6, command=equalpress)
    else:
      
        btn = tk.Button(gui, text=text, height=2, width=6, command=lambda t=text: press(t))
    btn.grid(row=r, column=c, padx=5, pady=5)

clear_btn = tk.Button(gui, text='Clear', height=2, width=26, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, pady=10, padx=8)


def on_key(ev):
    global expression
    if ev.keysym == 'Return':
        equalpress()
    elif ev.keysym == 'BackSpace':
        expression = expression[:-1]
        equation.set(expression)
    else:
        ch = ev.char
        if ch in '0123456789.+-*/()':
            press(ch)

gui.bind("<Key>", on_key)
entry.focus_set()

gui.mainloop()



