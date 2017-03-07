from content_management import Content
from dbconnect import connection


from flask import Flask, render_template, flash, request, url_for, redirect, session
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc




password = sha256_crypt.encrypt("1")
password2 = sha256_crypt.encrypt("2")

print(password)
print(password2)

print(sha256_crypt.verify("password", password))



def resgister():
    c,conn = connection()
    c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                          (thwart('ashwin'), thwart('$5$rounds=535000$gPbA0dpDhVJO.eUz$n23Xyj7GuXK7EfgyYw44EbmYajn2.KZobuyjPfyhVzB'), thwart('test@gmail.com'), thwart("/introduction-to-python-programming/")))
    conn.commit()
    flash("Thanks for registering!")
    c.close()
    conn.close()
    gc.collect()

resgister()




