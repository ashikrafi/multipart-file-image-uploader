<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="styles.css">
  </head>
  <body>
    <h1>Multipart File/Image Uploader</h1>
    <p>This is a file/image uploader application built using Starlette, Uvicorn and Base64. It allows for the uploading of multiple image files in the following formats: jpg, jpeg, png, tif, and tiff.</p>
    <h2>Getting Started</h2>
    <p>These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.</p>
    <h3>Prerequisites</h3>
    <ul>
      <li>Python 3.6+</li>
      <li>pip</li>
    </ul>
    <h3>Installing</h3>
    <ol>
      <li>Clone the repository to your local machine</li>
      <li>Change into the project directory</li>
      <li>Install the required packages</li>
      <li>Start the server</li>
      <li>Test the application by making a POST request to `http://0.0.0.0:8009/upload` with `file` as a key and an image file as the value</li>
    </ol>
    <h2>Deployment</h2>
    <p>The application can be deployed on any web server that supports ASGI (such as Daphne or Gunicorn) or can be containerized using Docker.</p>
    <h2>Built With</h2>
    <ul>
      <li>Starlette</li>
      <li>Uvicorn</li>
      <li>Base64</li>
    </ul>
    <h2>Authors</h2>
    <p>Your Name - Initial work</p>
    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details</p>
    <h2>Acknowledgments</h2>
    <p>Inspiration</p>
  </body>
</html>

