from flask import Blueprint, render_template, request, session, redirect, flash
from ..helpers import login_required
from ..config import Config
import boto3
from werkzeug.utils import secure_filename

add_images_blueprint = Blueprint("add_images_blueprint", __name__, static_folder="static", template_folder="templates")

@add_images_blueprint.route("/add-images", methods=["GET", "POST"])
@login_required
def add_images():
    user_id = session.get("user_id")
    client = boto3.client('s3')

    if request.method == "POST":
        if 'screenshot' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['screenshot']
        trade_id = request.form.get("trade_id")
        formatted_tid = trade_id[0:3] + trade_id[3:6]
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            complete_path =  str(user_id) + "/" + formatted_tid + "/" + filename
            client.put_object(Body=file, Bucket=Config.S3_BUCKET_NAME, Key=complete_path, ContentType="image/jpeg")
  
        return render_template("add-images.html", user_id=user_id)
    else:
        return render_template("add-images.html", user_id=user_id)