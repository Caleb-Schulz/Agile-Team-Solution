import streamlit as st
import pandas as pd
from logic import calculate_stats, get_grade_distribution

#Caleb Schulz - Task B - inputs
# Creating session state
if "students" not in st.session_state:
    st.session_state.students = []

st.sidebar.header("Add Student")

# sidebar for data entry 
name = st.sidebar.text_input("First and Last Name")
grade = st.sidebar.number_input("Grade", min_value=0, max_value=100, step=1)

# Add Student button
if st.sidebar.button("Add Student"):
    if name:
        st.session_state.students.append({
            "Name": name,
            "Grade": grade
        })

# Student Dropdown
if st.session_state.students:
    student_options = [
        f"{i}: {s['Name']} ({s['Grade']})"
        for i, s in enumerate(st.session_state.students)
    ]

    selected = st.sidebar.selectbox("Select Student", student_options)
    selected_index = int(selected.split(":")[0])

    # Remove student
    if st.sidebar.button("Remove Student"):
        st.session_state.students.pop(selected_index)
        st.rerun()

    # Modify student

    student = st.session_state.students[selected_index]

    new_name = st.sidebar.text_input("Edit Name", value=student["Name"])
    new_grade = st.sidebar.number_input(
        "Edit Grade", min_value=0, max_value=100, value=student["Grade"]
    )

    
    if st.sidebar.button("Update Student"):
        st.session_state.students[selected_index] = {
            "Name": new_name,
            "Grade": new_grade
        }
        st.rerun()

# Convert to DataFrame
df = pd.DataFrame(st.session_state.students)

# Testing display
# st.write("Current Student Data:")
# st.dataframe(df)

#End of Task B

# Start of Task D - Johnathan Nguyen
st.title("Faculty Grade Dashboard")

if not df.empty:
    stats = calculate_stats(df)
    distribution = get_grade_distribution(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Average", round(stats["average"], 1))
    col2.metric("Highest", stats["highest"])
    col3.metric("Lowest", stats["lowest"])

    st.subheader("Grade Distribution")
    st.bar_chart(distribution)

    st.subheader("Current Roster")
    st.dataframe(df)
else:
    st.info("No students added yet.")