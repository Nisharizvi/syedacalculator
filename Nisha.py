def add(num1 , num2):
    return num1 + num2

def subtract(num1, num2):
        return num1 - num2

def multiply(num1, num2):
        return num1 * num2

def divide(num1,num2):
        if num2 == 0:
            return "error: cannot divide by zero"
            return num1 / num2
import streamlit as st

st.title('Zahra Calculator')

def perform_operation(num1, num2, operation):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
operation = st.selectbox("Select an operation", ('+', '-', '*', '/'))


if st.button('Result'):
    result = perform_operation(num1, num2, operation)
    st.write(f"Result: {result}")


quit_calc = st.radio("Do you want to quit the calculator?", ('Y', 'N'))
if quit_calc == 'Y':
    st.write("Good luck!")
    st.stop()