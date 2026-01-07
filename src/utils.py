import os

def list_audio_files(base_dir):
    files = []
    for root, _, filenames in os.walk(base_dir):
        for f in filenames:
            if f.lower().endswith(".wav"):
                files.append(os.path.join(root, f))
    return files
