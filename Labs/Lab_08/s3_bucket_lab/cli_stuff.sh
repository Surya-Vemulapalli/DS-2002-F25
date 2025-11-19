#!/bin/bash

set -e

IMG_URL="https://thumbs.dreamstime.com/b/chicken-business-suit-looking-like-high-powered-executive-his-desk-wearing-businessman-sitting-image-has-surreal-396635149.jpg"
EXP_DATE=604800
BUCKET="ds2002-f25-jrn2kf"
FILE_NM="fl.jpg"

echo "Uploading to bucket"

touch "$FILE_NM"

curl "$IMG_URL" > "$FILE_NM"

aws s3 cp "$FILE_NM" "s3://$BUCKET/"

aws s3 presign --expires-in "$EXP_DATE" "s3://$BUCKET/$FILE_NM"

echo "Process complete"
