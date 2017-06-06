# 3rd party installs
from uuid import uuid4
from boto.s3.connection import Key
import boto
import os.path
from flask import current_app as app
from werkzeug.utils import secure_filename


def s3_upload(source_file, upload_dir=None, acl='public-read'):
    """Upload WTForm object to Amazon S3

        Expects following app.config attributes to be set:
        S3_KEY              :   S3 API Key
        S3_SECRET           :   S3 Secret Key
        S3_BUCKET           :   What bucket to upload to
        S3_UPLOAD_DIRECTORY :   Which S3 Directory.

        The default sets the access rights on the uploaded file to public read.
        It also a unique file name via uuid function combined with the file
        extension from the source file.
    """

    if upload_dir is None:
        upload_dir = app.config["S3_UPLOAD_DIRECTORY_1"]

    source_filename = secure_filename(source_file.data.filename)
    source_extension = os.path.splitext(source_filename)[1]

    destination_filename = uuid4().hex + source_extension

    # Connect to S3 and upload file.
    conn = boto.connect_s3(app.config["S3_KEY"], app.config["S3_SECRET"])
    bucket = conn.get_bucket(app.config["S3_BUCKET"])

    sml = bucket.new_key("/".join([upload_dir, destination_filename]))
    sml.set_contents_from_string(source_file.data.read())
    sml.set_acl(acl)

    return destination_filename


def s3_delete(image, upload_dir=None):
    conn = boto.connect_s3(app.config["S3_KEY"], app.config["S3_SECRET"])
    bucket = conn.get_bucket(app.config["S3_BUCKET"])

    if upload_dir is None:
        upload_dir = app.config["S3_UPLOAD_DIRECTORY_1"]

    key = bucket.get_key("/".join([upload_dir, image]))
    key.delete()

