#!/bin/Python3

import mysql.connector

from mysql.connector import Error

try:
	db_connection = mysql.connector.connect(
	host ="localhost",
	user ="root",
	password ="********"
	)

	if db_connection.is_connected():
		cursor_obj = db_connection.cursor()

	cursor_obj.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
	print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error:
	print(f"Error, failing to connect to the MySQL Server: {Error}")

finally:
	if "cursor_obj" in locals():
		cursor_obj.close()
	if "db_connection" in locals() and db_connection.is_connected():
		db_connection.close()
