from flask import Flask, render_template, request
import os
import uuid
import subprocess
from pathlib import Path
import glob
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    terminal_output = ''
    result_images = []
    content_preview = None
    style_preview = None

    if request.method == 'POST':
        terminal_output = ''  # ✅ Reset terminal log on new upload
        num_images = int(request.form['num_images'])
        content_image = request.files['content_image']
        style_image = request.files['style_image']

        if content_image and style_image:
            content_filename = f"{uuid.uuid4()}_{content_image.filename}"
            style_filename = f"{uuid.uuid4()}_{style_image.filename}"

            content_path = os.path.join(UPLOAD_FOLDER, content_filename)
            style_path = os.path.join(UPLOAD_FOLDER, style_filename)
            content_image.save(content_path)
            style_image.save(style_path)

            content_preview = Path(content_path).as_posix()
            style_preview = Path(style_path).as_posix()

            result_prefix = Path(os.path.join(RESULT_FOLDER, str(uuid.uuid4()))).as_posix()

            try:
               
                process = subprocess.Popen(
                    ['python', 'inetwork_tf.py', content_preview, style_preview, result_prefix, '--num_iter', str(num_images)],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
                output_lines = []
                for line in process.stdout:
                    output_lines.append(line)
                    terminal_output = ''.join(output_lines)

                    # Simulate progress by updating every 5% completion
                    time.sleep(1)

                process.wait()

                pattern = result_prefix + "_at_iteration_*.png"
                result_images = sorted(
                    glob.glob(pattern),
                    key=lambda x: int(x.split('_')[-1].split('.')[0])
                )
                result_images = [Path(path).as_posix() for path in result_images]

            except Exception as e:
                terminal_output = str(e)

    return render_template(
        'index.html',
        result_images=result_images,
        terminal_output=terminal_output,
        content_preview=content_preview,
        style_preview=style_preview
    )

if __name__ == '__main__':
    app.run(debug=True)
