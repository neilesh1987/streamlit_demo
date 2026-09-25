import streamlit as st
import sqlite3
import random
from datetime import date


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_connection():
    return sqlite3.connect("railway.db")


# =========================================================
# CREATE TABLE
# =========================================================

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pnr TEXT UNIQUE NOT NULL,
            customer_name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            mobile TEXT,
            train_name TEXT,
            train_number TEXT,
            from_station TEXT,
            to_station TEXT,
            journey_date TEXT,
            coach TEXT,
            seat_number TEXT,
            meal TEXT,
            booking_status TEXT
        )
    """)

    conn.commit()
    conn.close()


create_table()


# =========================================================
# GENERATE PNR
# =========================================================

def generate_pnr():

    while True:

        pnr = str(random.randint(1000000000, 9999999999))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT pnr FROM bookings WHERE pnr = ?",
            (pnr,)
        )

        result = cursor.fetchone()

        conn.close()

        if result is None:
            return pnr


# =========================================================
# INSERT BOOKING
# =========================================================

def save_booking(data):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO bookings (
            pnr,
            customer_name,
            age,
            gender,
            mobile,
            train_name,
            train_number,
            from_station,
            to_station,
            journey_date,
            coach,
            seat_number,
            meal,
            booking_status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()


# =========================================================
# SEARCH BY PNR
# =========================================================

def search_by_pnr(pnr):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM bookings
        WHERE pnr = ?
    """, (pnr,))

    result = cursor.fetchone()

    conn.close()

    return result


# =========================================================
# SEARCH BY CUSTOMER NAME
# =========================================================

def search_by_customer(name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM bookings
        WHERE customer_name LIKE ?
    """, ("%" + name + "%",))

    results = cursor.fetchall()

    conn.close()

    return results


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Railway Reservation System",
    page_icon="🚆",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fa;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #1f4e79;
}

.sub-title {
    text-align: center;
    color: #6c757d;
    font-size: 17px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 23px;
    font-weight: bold;
    color: #1f4e79;
    margin-bottom: 15px;
}

.booking-card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

.stButton > button {
    width: 100%;
    border-radius: 8px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🚆 Railway Reservation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">'
    'Book tickets, retrieve bookings and search customer details'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# SIDEBAR MENU
# =========================================================

st.sidebar.title("🚆 Railway System")

menu = st.sidebar.radio(
    "Select Operation",
    [
        "📝 New Booking",
        "🔎 Search Booking",
        "👤 Customer Details"
    ]
)


# =========================================================
# NEW BOOKING
# =========================================================

if menu == "📝 New Booking":

    st.markdown(
        '<div class="section-title">📝 New Railway Booking</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        st.subheader("👤 Customer Information")

        col1, col2 = st.columns(2)

        with col1:

            customer_name = st.text_input(
                "Customer Name"
            )

            age = st.number_input(
                "Age",
                min_value=5,
                max_value=100,
                value=18
            )

            mobile = st.text_input(
                "Mobile Number"
            )

        with col2:

            gender = st.selectbox(
                "Gender",
                [
                    "Male",
                    "Female",
                    "Other"
                ]
            )


    st.write("")


    with st.container(border=True):

        st.subheader("🚆 Journey Information")

        col1, col2 = st.columns(2)

        with col1:

            train_name = st.selectbox(
                "Train Name",
                [
                    "Rajdhani Express",
                    "Shatabdi Express",
                    "Duronto Express",
                    "Vande Bharat Express",
                    "Deccan Express"
                ]
            )

            train_number = st.text_input(
                "Train Number"
            )

            from_station = st.text_input(
                "From Station"
            )

            to_station = st.text_input(
                "To Station"
            )

        with col2:

            journey_date = st.date_input(
                "Journey Date",
                min_value=date.today()
            )

            coach = st.selectbox(
                "Coach",
                [
                    "1A",
                    "2A",
                    "3A",
                    "SL",
                    "CC",
                    "2S"
                ]
            )

            seat_number = st.text_input(
                "Seat Number"
            )

            meal = st.multiselect(
                "Meal Preference",
                [
                    "Veg",
                    "Non-Veg",
                    "Jain",
                    "No Meal"
                ],
                max_selections=1
            )


    st.write("")

    if st.button("🚆 Confirm Booking"):

        if customer_name.strip() == "":
            st.error("Please enter customer name.")

        elif mobile.strip() == "":
            st.error("Please enter mobile number.")

        elif train_number.strip() == "":
            st.error("Please enter train number.")

        elif from_station.strip() == "":
            st.error("Please enter boarding station.")

        elif to_station.strip() == "":
            st.error("Please enter destination.")

        else:

            pnr = generate_pnr()

            meal_value = meal[0] if meal else "No Meal"

            booking_status = "Confirmed"

            data = (
                pnr,
                customer_name,
                age,
                gender,
                mobile,
                train_name,
                train_number,
                from_station,
                to_station,
                str(journey_date),
                coach,
                seat_number,
                meal_value,
                booking_status
            )

            save_booking(data)

            st.success(
                f"✅ Booking Confirmed! Your PNR is: {pnr}"
            )

            st.info(
                f"Please save your PNR number: **{pnr}**"
            )


# =========================================================
# SEARCH BOOKING
# =========================================================

elif menu == "🔎 Search Booking":

    st.markdown(
        '<div class="section-title">🔎 Search Railway Booking</div>',
        unsafe_allow_html=True
    )

    search_type = st.radio(
        "Search By",
        [
            "PNR Number",
            "Customer Name"
        ],
        horizontal=True
    )

    st.write("")


    # -----------------------------------------------------
    # SEARCH BY PNR
    # -----------------------------------------------------

    if search_type == "PNR Number":

        pnr = st.text_input(
            "Enter PNR Number"
        )

        if st.button("🔎 Search PNR"):

            if pnr.strip() == "":
                st.warning("Please enter PNR number.")

            else:

                result = search_by_pnr(pnr)

                if result:

                    st.success("Booking Found!")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.write(
                            f"**PNR:** {result[1]}"
                        )

                        st.write(
                            f"**Customer Name:** {result[2]}"
                        )

                        st.write(
                            f"**Age:** {result[3]}"
                        )

                        st.write(
                            f"**Gender:** {result[4]}"
                        )

                        st.write(
                            f"**Mobile:** {result[5]}"
                        )

                        st.write(
                            f"**Train:** {result[6]}"
                        )

                        st.write(
                            f"**Train Number:** {result[7]}"
                        )

                    with col2:

                        st.write(
                            f"**From:** {result[8]}"
                        )

                        st.write(
                            f"**To:** {result[9]}"
                        )

                        st.write(
                            f"**Journey Date:** {result[10]}"
                        )

                        st.write(
                            f"**Coach:** {result[11]}"
                        )

                        st.write(
                            f"**Seat Number:** {result[12]}"
                        )

                        st.write(
                            f"**Meal:** {result[13]}"
                        )

                        st.write(
                            f"**Status:** {result[14]}"
                        )

                else:

                    st.error(
                        "❌ No booking found for this PNR."
                    )


    # -----------------------------------------------------
    # SEARCH BY CUSTOMER
    # -----------------------------------------------------

    else:

        customer_name = st.text_input(
            "Enter Customer Name"
        )

        if st.button("🔎 Search Customer"):

            if customer_name.strip() == "":
                st.warning(
                    "Please enter customer name."
                )

            else:

                results = search_by_customer(
                    customer_name
                )

                if results:

                    st.success(
                        f"{len(results)} booking(s) found."
                    )

                    for result in results:

                        with st.expander(
                            f"PNR: {result[1]} | "
                            f"{result[6]} | "
                            f"{result[10]}"
                        ):

                            col1, col2 = st.columns(2)

                            with col1:

                                st.write(
                                    f"**Customer:** {result[2]}"
                                )

                                st.write(
                                    f"**Mobile:** {result[5]}"
                                )

                                st.write(
                                    f"**Train:** {result[6]}"
                                )

                                st.write(
                                    f"**Train Number:** {result[7]}"
                                )

                                st.write(
                                    f"**From:** {result[8]}"
                                )

                                st.write(
                                    f"**To:** {result[9]}"
                                )

                            with col2:

                                st.write(
                                    f"**Journey Date:** {result[10]}"
                                )

                                st.write(
                                    f"**Coach:** {result[11]}"
                                )

                                st.write(
                                    f"**Seat:** {result[12]}"
                                )

                                st.write(
                                    f"**Meal:** {result[13]}"
                                )

                                st.write(
                                    f"**Status:** {result[14]}"
                                )

                else:

                    st.error(
                        "❌ No booking found for this customer."
                    )


# =========================================================
# CUSTOMER DETAILS
# =========================================================

elif menu == "👤 Customer Details":

    st.markdown(
        '<div class="section-title">👤 Customer Details</div>',
        unsafe_allow_html=True
    )

    customer_name = st.text_input(
        "Enter Customer Name"
    )

    if st.button("👤 Get Customer Details"):

        results = search_by_customer(
            customer_name
        )

        if results:

            # Display customer summary
            first = results[0]

            st.success(
                f"Customer found: {first[2]}"
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Customer Name",
                    first[2]
                )

            with col2:
                st.metric(
                    "Mobile",
                    first[5]
                )

            with col3:
                st.metric(
                    "Total Bookings",
                    len(results)
                )

            st.divider()

            st.subheader(
                "📋 Customer Booking History"
            )

            for result in results:

                st.write(
                    f"**PNR:** {result[1]}"
                )

                st.write(
                    f"**Train:** {result[6]} "
                    f"({result[7]})"
                )

                st.write(
                    f"**Journey:** {result[8]} → {result[9]}"
                )

                st.write(
                    f"**Date:** {result[10]}"
                )

                st.write(
                    f"**Coach:** {result[11]} | "
                    f"**Seat:** {result[12]}"
                )

                st.write(
                    f"**Status:** {result[14]}"
                )

                st.divider()

        else:

            st.error(
                "❌ Customer not found."
            )