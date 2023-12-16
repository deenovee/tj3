from flask import Blueprint, render_template, request, session
from ..helpers import login_required
from ..config import Config
import boto3
from werkzeug.utils import secure_filename

delete_images_blueprint = Blueprint("delete_images_blueprint", __name__, static_folder="static", template_folder="templates")

@delete_images_blueprint.route("/delete-images", methods=["POST"])
@login_required
def delete_images():
    images_list=[]
    user_id = session.get("user_id")
    trade_id = request.form.get("trade_id")
    image_id = request.form.get("image_id")
    prefix = str(user_id) + "/" + trade_id + "/"
    client.delete_object(Bucket=Config.S3_BUCKET_NAME, Key=image_id)
    try:
        response = client.list_objects_v2(Bucket=Config.S3_BUCKET_NAME, Prefix = prefix, Delimiter = "/")
        for object in response['Contents']:
            images_list.append(object['Key'])
    except:
        images_list=[]
    return render_template("screenshots.html", images=images_list, user_id=user_id, trade_id=trade_id)