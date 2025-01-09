from fasthtml.common import *
from passlib.context import CryptContext
from functools import wraps

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def getPasswordHash(password):
    return pwd_context.hash(password)

def verifyPassword(plaintext, hashedtext):
    return pwd_context.verify(plaintext, hashedtext)

def registerForm(btn_text, target):
    return Form(
        Input(id="first_name", type="name", placeholder="First Name", required=True),
        Input(id="last_name", type="name", placeholder="LastName", required=True),
        Input(id="email", type="email", placeholder="Email", required=True),
        Input(id="password", type="password", placeholder="Password", required=True),
        Button(btn_text, type="submit"),
        Span(id="error", style="color:red"),
        hx_post=target,
        hx_target="#error",
    )

def loginForm(btn_text, target):
    return Form(
        Input(id="email", type="email", placeholder="Email", required=True),
        Input(id="password", type="password", placeholder="Password", required=True),
        Button(btn_text, type="submit"),
        Span(id="error", style="color:red"),
        hx_post=target,
        hx_target="#error",
    )


