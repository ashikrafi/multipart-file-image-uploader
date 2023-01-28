<!DOCTYPE html>
<html>
<body>
  <h1>Multipart Image Uploader</h1>
  <p>This application allows you to upload multiple images at once, and returns the base64 encoded data for each image.</p>
  <h2>Getting Started</h2>
  <p>The application is built using the Starlette web framework, and Uvicorn as the ASGI server.</p>
  <p>To run the application, you will need to have Python (3.6 or higher) and pip installed on your machine.</p>
  <p>Install the required packages by running <code>pip install -r requirements.txt</code></p>
  <p>Run the application using <code>uvicorn main:app --host=0.0.0.0 --port=8009</code></p>
  <h2>Usage</h2>
  <p>To use the application, make a POST request to the endpoint <code>/upload</code> with a <code>multipart/form-data</code> content type and a file field containing the images you wish to upload.</p>
  <p>The response will be a JSON object containing the status of the upload, and an array of base64 encoded images.</p>
  <h3>Example</h3>
  <h4>Bash</h4>
  <pre>
  <code>
curl -X POST http://localhost:8009/upload
-H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'
-F file=@/path/to/image1.jpg
-F file=@/path/to/image2.jpg
  </code>
  </pre>
  <h4>JSON</h4>
  <pre>
  <code>
{ "result": "success", "base64_images": [ "encoded_data_for_image1", "encoded_data_for_image2" ] }
  </code>
  </pre>
  <p>Note: This app allows only jpg, jpeg, png, tif, tiff file types to be uploaded. If you want to allow other types, you can modify ALLOWED_EXTENSIONS variable in the code.</p>
  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the LICENSE file for details.</p>
</body>
</html>
