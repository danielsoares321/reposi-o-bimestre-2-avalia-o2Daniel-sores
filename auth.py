from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)
@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        
        return redirect(url_for("registro"))
    generate_password_hash()
    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = session["usuario_nome"]
        senha = session["usuario_senha"]
        return redirect(url_for("login"))
    check_password_hash
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    return redirect(url_for("index"))


