from flask import Flask, render_template, request, send_file, redirect, url_for, flash
from pytube import YouTube
import os
import tempfile

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this for production

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url or 'youtube.com' not in url:
            flash('Please enter a valid YouTube URL.', 'danger')
            return redirect(url_for('index'))
        try:
            yt = YouTube(url)
            # Get highest resolution stream >= 720p
            stream = None
            for res in ['1440p', '1080p', '720p']:
                stream = yt.streams.filter(progressive=True, file_extension='mp4', res=res).first()
                if stream:
                    break
            if not stream:
                flash('No suitable video quality found (min 720p).', 'danger')
                return redirect(url_for('index'))
            temp_dir = tempfile.mkdtemp()
            file_path = stream.download(output_path=temp_dir)
            filename = os.path.basename(file_path)
            return send_file(file_path, as_attachment=True, download_name=filename)
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
