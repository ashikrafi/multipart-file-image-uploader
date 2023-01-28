Multi-Part Image Uploader
This is a simple Python application that allows for the uploading of multiple images using a multipart form. The images are then converted to base64 encoded data and returned in a JSON response.

Getting Started
The application is built using the Starlette web framework, and Uvicorn as the ASGI server.

To run the application, you will need to have Python (3.6 or higher) and pip installed on your machine.

Install the required packages by running pip install -r requirements.txt
Run the application using uvicorn main:app --host=0.0.0.0 --port=8009
Usage
To use the application, make a POST request to the endpoint /upload with a multipart/form-data content type and a file field containing the images you wish to upload.

The response will be a JSON object containing the status of the upload, and an array of base64 encoded images.

Example
bash
Copy code
curl -X POST \
  http://localhost:8009/upload \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F file=@/path/to/image1.jpg \
  -F file=@/path/to/image2.jpg
json
Copy code
{
  "result": "success",
  "base64_images": [
    "encoded_data_for_image1",
    "encoded_data_for_image2"
  ]
}
Note
This app allows only jpg, jpeg, png, tif, tiff file types to be uploaded. If you want to allow other types, you can modify ALLOWED_EXTENSIONS variable in the code.

License
This project is licensed under the MIT License - see the LICENSE file for details.
