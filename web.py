import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    todo_item = st.session_state["new_todo"] + "\n"
    todos.append(todo_item)
    write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("Alberto's Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter todo", placeholder="Add new todo...", label_visibility="hidden", key="new_todo",
              on_change=add_todo)

