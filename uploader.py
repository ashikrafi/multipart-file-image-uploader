import base64
import os
import uvicorn
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

app = Starlette(debug=True)
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])


ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'tif', 'tiff'}
UPLOAD_FOLDER = 'app/static/uploads'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload", methods=["POST"])
async def upload(request):
    try:
        form = await request.form()
        files = form.getlist("file")  # get all files in the form
        base64_images = []
        for file in files:
            filename = file.filename
            if not allowed_file(filename):
                return JSONResponse({'result': 'Invalid file type'}, status_code=400)
            else:
                save_path = os.path.join(UPLOAD_FOLDER, filename)
                with open(save_path, 'wb') as f:
                    f.write(await file.read())
                with open(save_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode()
                    base64_images.append(encoded_string)
        return JSONResponse({'result': 'success', 'base64_images': base64_images}, status_code=200)
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8009)
