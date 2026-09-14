import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: AliceBlue;
}

h1 {
    color: Navy;
    text-align: center;
    font-size: 42px;
    font-weight: 800;
}

h2, h3 {
    color: MidnightBlue !important;
}

p {
    color: Black !important;
}

label {
    color: Black !important;
}

section[data-testid="stSidebar"] {
    background-color: LightSteelBlue;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label {
    color: Black !important;
}

div[data-testid="stMetric"] {
    background-color: White;
    border: 1px solid SteelBlue;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 5px 15px LightGray;
}

div[data-testid="stMetricLabel"] {
    color: DimGray !important;
}

div[data-testid="stMetricValue"] {
    color: Navy !important;
    font-size: 30px;
    font-weight: bold;
}

div[data-testid="stMetricDelta"] {
    color: Black !important;
}

.stButton > button {
    background-color: Teal;
    color: White;
    border-radius: 12px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background-color: DarkCyan;
    color: White;
}

.stTextInput input {
    background-color: White;
    color: Black;
}

.stNumberInput input {
    background-color: White;
    color: Black;
}

.stSelectbox div {
    color: Black;
}

.stSelectbox input {
    color: Black;
}

[data-baseweb="select"] {
    background-color: White;
}

[data-baseweb="select"] div {
    color: Black !important;
}

[data-baseweb="select"] span {
    color: Black !important;
}

.stDataFrame {
    background-color: White;
}

[data-testid="stDataFrame"] {
    background-color: White;
}

.stAlert {
    color: Black;
}

.dashboard-card {
    background-color: White;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid SteelBlue;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

if "students" not in st.session_state:

    st.session_state.students = pd.DataFrame(
        columns=[
            "ID",
            "Name",
            "Age",
            "Course",
            "Marks",
            "City"
        ]
    )

st.title("🎓 Student Management System")

st.markdown(
    "<p style='text-align:center; color:Black !important;'>"
    "Manage Student Records using Python, Pandas & Streamlit"
    "</p>",
    unsafe_allow_html=True
)

st.sidebar.title("📌 MENU")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "➕ Add Student",
        "👀 View Students",
        "🔍 Search Student",
        "✏️ Update Student",
        "🗑️ Delete Student",
        "📊 Dashboard"
    ]
)

if menu == "➕ Add Student":

    st.header("➕ Add New Student")

    col1, col2 = st.columns(2)

    with col1:

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        name = st.text_input(
            "Student Name"
        )

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            step=1
        )

    with col2:

        course = st.selectbox(
            "Course",
            [
                "Python",
                "Data Science",
                "Data Analytics",
                "Full Stack",
                "AI"
            ]
        )

        marks = st.number_input(
            "Marks",
            min_value=0,
            max_value=100,
            step=1
        )

        city = st.text_input(
            "City"
        )

    st.write("")

    if st.button("➕ ADD STUDENT"):

        if student_id in st.session_state.students["ID"].values:

            st.error(
                "❌ Student ID already exists!"
            )

        elif name == "":

            st.warning(
                "⚠️ Please enter student name."
            )

        else:

            new_student = {
                "ID": student_id,
                "Name": name,
                "Age": age,
                "Course": course,
                "Marks": marks,
                "City": city
            }

            st.session_state.students = pd.concat(
                [
                    st.session_state.students,
                    pd.DataFrame([new_student])
                ],
                ignore_index=True
            )

            st.success(
                "✅ Student added successfully!"
            )

elif menu == "👀 View Students":

    st.header("👀 Student Records")

    df = st.session_state.students

    if len(df) == 0:

        st.info(
            "🎓 No student records available."
        )

    else:

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.write(
            f"Total Records: **{len(df)}**"
        )

elif menu == "🔍 Search Student":

    st.header("🔍 Search Student")

    search = st.text_input(
        "Enter student name"
    )

    if search:

        df = st.session_state.students

        result = df[
            df["Name"]
            .str.contains(
                search,
                case=False,
                na=False
            )
        ]

        if len(result) > 0:

            st.success(
                f"Found {len(result)} student(s)"
            )

            st.dataframe(
                result,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning(
                "❌ Student not found."
            )

elif menu == "✏️ Update Student":

    st.header("✏️ Update Student Marks")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1
    )

    new_marks = st.number_input(
        "Enter New Marks",
        min_value=0,
        max_value=100,
        step=1
    )

    if st.button("✏️ UPDATE MARKS"):

        index = st.session_state.students[
            st.session_state.students["ID"]
            == student_id
        ].index

        if len(index) > 0:

            st.session_state.students.loc[
                index,
                "Marks"
            ] = new_marks

            st.success(
                "✅ Marks updated successfully!"
            )

        else:

            st.error(
                "❌ Student ID not found."
            )

elif menu == "🗑️ Delete Student":

    st.header("🗑️ Delete Student")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1
    )

    if st.button("🗑️ DELETE STUDENT"):

        old_count = len(
            st.session_state.students
        )

        st.session_state.students = (
            st.session_state.students[
                st.session_state.students["ID"]
                != student_id
            ]
        )

        new_count = len(
            st.session_state.students
        )

        if old_count != new_count:

            st.success(
                "✅ Student deleted successfully!"
            )

        else:

            st.error(
                "❌ Student ID not found."
            )

elif menu == "📊 Dashboard":

    st.header("📊 Student Analytics Dashboard")

    df = st.session_state.students

    if len(df) == 0:

        st.info(
            "🎓 No student data available. "
            "Please add students first."
        )

    else:

        total_students = len(df)

        average_marks = round(
            df["Marks"].mean(),
            2
        )

        highest_marks = df["Marks"].max()

        lowest_marks = df["Marks"].min()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "👨‍🎓 TOTAL STUDENTS",
            total_students
        )

        col2.metric(
            "📈 AVERAGE MARKS",
            average_marks
        )

        col3.metric(
            "🏆 HIGHEST MARKS",
            highest_marks
        )

        col4.metric(
            "📉 LOWEST MARKS",
            lowest_marks
        )

        st.divider()

        st.subheader(
            "🎯 Student Performance"
        )

        pass_count = len(
            df[df["Marks"] >= 40]
        )

        fail_count = len(
            df[df["Marks"] < 40]
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "✅ PASSED",
            pass_count
        )

        col2.metric(
            "❌ FAILED",
            fail_count
        )

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "📚 Students by Course"
            )

            course_count = (
                df["Course"]
                .value_counts()
            )

            st.bar_chart(
                course_count
            )

        with col2:

            st.subheader(
                "📈 Student Marks"
            )

            marks_data = (
                df[["Name", "Marks"]]
                .set_index("Name")
            )

            st.bar_chart(
                marks_data
            )

        st.divider()

        st.subheader(
            "🏆 Top 5 Performing Students"
        )

        top_students = (
            df.sort_values(
                "Marks",
                ascending=False
            )
            .head(5)
        )

        st.dataframe(
            top_students,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader(
            "📊 Course Statistics"
        )

        course_stats = (
            df.groupby("Course")
            .agg(
                Students=("ID", "count"),
                Average_Marks=("Marks", "mean"),
                Highest_Marks=("Marks", "max"),
                Lowest_Marks=("Marks", "min")
            )
            .round(2)
            .reset_index()
        )

        st.dataframe(
            course_stats,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

        st.subheader(
            "🏙️ Students by City"
        )

        city_count = (
            df["City"]
            .value_counts()
        )

        st.bar_chart(
            city_count
        )

st.sidebar.divider()

st.sidebar.subheader(
    "📥 Export Data"
)

csv = st.session_state.students.to_csv(
    index=False
)

st.sidebar.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="students.csv",
    mime="text/csv"
)

st.markdown(
    """
    <p style="
        text-align:center;
        color:Gray;
        margin-top:40px;">
        🎓 Student Management System |
        Built with Python + Pandas + Streamlit
    </p>
    """,
    unsafe_allow_html=True
)