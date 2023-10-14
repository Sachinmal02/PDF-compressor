import os
from zipfile import ZipFile
import shutil
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    save_path= r"d:/flask_compression/input"
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        if filename:
            print(filename)
            save_path=os.path.join(save_path, os.path.splitext(filename)[0])
        try:
            os.mkdir(save_path)
        except:
            shutil.rmtree(save_path)
            os.mkdir(save_path)
            save_location=os.path.join(save_path,filename)
            file.save(save_location)
            # with ZipFile(os.path.join("compressed",os.path.splitext(filename)[0]+".zip"), 'w') as zip:
            #     zip.write(save_location)
            shutil.make_archive(os.path.join(r"d:/flask_compression/compressed",os.path.splitext(filename)[0]),'zip',save_path)
            return send_from_directory(r"d:/flask_compression/compressed",
                                    os.path.splitext(filename)[0]+'.zip', as_attachment=True)
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000,use_reloader=False)