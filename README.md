# 🚆 Railway Reservation System

A simple and user-friendly **Railway Reservation System** built using **Python, Streamlit, and SQLite3**.

This application allows users to create railway bookings, automatically generate a unique PNR number, and retrieve booking/customer details using either the **PNR number** or **customer name**.

---

## 📌 Project Overview

The Railway Reservation System is a beginner-friendly Python application designed to demonstrate how to build a database-driven web application using Streamlit.

The application provides functionality for:

* 👤 Entering customer details
* 🚆 Entering train and journey details
* 🎫 Creating railway reservations
* 🔢 Automatically generating PNR numbers
* 🔎 Searching bookings using PNR
* 👤 Searching bookings using customer name
* 📋 Viewing customer booking history
* 🗄️ Storing data using SQLite3
* ✅ Displaying booking confirmation and status

---

## 🛠️ Technologies Used

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python     | Application programming  |
| Streamlit  | Web application frontend |
| SQLite3    | Database                 |
| HTML/CSS   | Custom UI styling        |
| SQL        | Database operations      |

---

## ✨ Features

### 1. 📝 New Booking

Users can enter:

* Customer Name
* Age
* Gender
* Mobile Number
* Train Name
* Train Number
* From Station
* To Station
* Journey Date
* Coach
* Seat Number
* Meal Preference

After submitting the booking, the application automatically generates a unique **PNR number**.

Example:

```text
Booking Confirmed!

PNR: 8245632190
Status: Confirmed
```

---

### 2. 🔎 Search Booking by PNR

Users can enter a PNR number to retrieve the complete booking information.

Example:

```text
Enter PNR:
8245632190
```

The application displays:

```text
PNR
Customer Name
Age
Gender
Mobile
Train Name
Train Number
From Station
To Station
Journey Date
Coach
Seat Number
Meal
Booking Status
```

---

### 3. 👤 Search Booking by Customer Name

Users can search for bookings using the customer's name.

For example:

```text
Customer Name:
Rahul
```

The application can retrieve matching customer bookings using SQL `LIKE`.

```sql
SELECT *
FROM bookings
WHERE customer_name LIKE '%Rahul%';
```

This allows partial-name searching.

---

### 4. 📋 Customer Booking History

The Customer Details section displays:

* Customer name
* Mobile number
* Total bookings
* PNR numbers
* Train details
* Journey information
* Coach
* Seat number
* Booking status

This is useful when a customer has multiple railway bookings.

---

## 🗄️ Database

The application uses **SQLite3** as the database.

The database file is automatically created:

```text
railway.db
```

### Database Table

The application creates a table named:

```text
bookings
```

### Table Structure

| Column         | Data Type | Description         |
| -------------- | --------- | ------------------- |
| id             | INTEGER   | Primary key         |
| pnr            | TEXT      | Unique PNR number   |
| customer_name  | TEXT      | Customer name       |
| age            | INTEGER   | Customer age        |
| gender         | TEXT      | Gender              |
| mobile         | TEXT      | Mobile number       |
| train_name     | TEXT      | Train name          |
| train_number   | TEXT      | Train number        |
| from_station   | TEXT      | Boarding station    |
| to_station     | TEXT      | Destination station |
| journey_date   | TEXT      | Journey date        |
| coach          | TEXT      | Coach type          |
| seat_number    | TEXT      | Seat number         |
| meal           | TEXT      | Meal preference     |
| booking_status | TEXT      | Booking status      |

---

## 📂 Project Structure

The basic project structure is:

```text
RailwayReservation/
│
├── app.py
├── railway.db
└── README.md
```

### `app.py`

Contains the Streamlit application, database operations, booking functionality, search functionality, and UI.

### `railway.db`

SQLite database file contai



[alt text](diagram.png)