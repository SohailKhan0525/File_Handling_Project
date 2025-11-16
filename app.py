import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="File Handling App", page_icon="📁", layout="centered")

# -----------------------------------------
# Helper: list files/folders
# -----------------------------------------
def list_items():
    path = Path("")
    items = list(path.rglob("*"))
    return items


# -----------------------------------------
# Create File
# -----------------------------------------
def create_file():
    st.subheader("📄 Create a New File")

    items = list_items()
    st.write("### Existing Files & Folders")
    for i, item in enumerate(items):
        st.write(f"{i+1}. {item}")

    filename = st.text_input("Enter filename to create (example: myfile.txt)")

    content = st.text_area("File content (optional)")

    if st.button("Create File"):
        p = Path(filename)

        if not filename.strip():
            st.error("❌ Please enter a valid filename")
            return

        if p.exists():
            st.warning("⚠️ This file already exists.")
        else:
            try:
                with open(p, "w") as f:
                    f.write(content)
                st.success("✅ File created successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")


# -----------------------------------------
# Read File
# -----------------------------------------
def read_file():
    st.subheader("📖 Read a File")

    items = [i for i in list_items() if i.is_file()]

    if not items:
        st.info("No files found.")
        return

    file_choice = st.selectbox("Choose a file to read:", items)

    if st.button("Read File"):
        try:
            with open(file_choice, "r") as f:
                data = f.read()

            st.code(data, language="text")
        except Exception as e:
            st.error(f"Error reading file: {e}")


# -----------------------------------------
# Delete File
# -----------------------------------------
def delete_file():
    st.subheader("🗑️ Delete a File")

    items = [i for i in list_items() if i.is_file()]

    if not items:
        st.info("No files to delete.")
        return

    file_choice = st.selectbox("Choose a file to delete:", items)

    if st.button("Delete File"):
        try:
            os.remove(file_choice)
            st.success("🗑️ File deleted successfully")
            st.rerun()
        except Exception as e:
            st.error(f"Error deleting file: {e}")


# -----------------------------------------
# MAIN UI
# -----------------------------------------
st.title("📁 File Handling System")
st.write("A simple file management tool built with Streamlit.")

menu = st.radio(
    "Select an option:",
    ["Create File", "Read File", "Delete File"],
    horizontal=True
)

if menu == "Create File":
    create_file()
elif menu == "Read File":
    read_file()
elif menu == "Delete File":
    delete_file()

