from flask import Blueprint, render_template, request, session
from ..helpers import login_required
from ..config import Config
import boto3
from werkzeug.utils import secure_filename

trade_images_blueprint = Blueprint("trade_images", __name__, static_folder="static", template_folder="templates")

client = boto3.client('s3')

@trade_images_blueprint.route("/trade-images", methods=["POST"])
@login_required
def trade_images_template():
    images_list =[]
    user_id = session.get("user_id")
    trade_id = request.form.get("images")
    formatted_tid = trade_id[0:3] + trade_id[4:7]
    prefix = str(user_id) + "/" + formatted_tid + "/"
    try:
        response = client.list_objects_v2(Bucket=Config.S3_BUCKET_NAME, Prefix = prefix, Delimiter = "/")
        for object in response['Contents']:

            images_list.append(object['Key'])
    except:
        images_list=[]

    return render_template("screenshots.html", images=images_list, user_id=user_id, trade_id=formatted_tid)