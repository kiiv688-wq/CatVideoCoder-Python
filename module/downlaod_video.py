import subprocess
from module.change_codec import change_codec

def download_video(path, url, format_type, quality, codec):
    if format_type == "Video":
        result = subprocess.run(["yt-dlp", "-P", path, "-S", f"height:{quality}", "--print", "after_move:filepath", url], capture_output=True, text=True)
    elif format_type == "Only Audio":
        result = subprocess.run(["yt-dlp", "-P", path, "-x", "-f", "bestaudio", "--print", "after_move:filepath", url], capture_output=True, text=True)
    else:
        result = subprocess.run(["yt-dlp", "-P", path, "-f", "bestvideo[acodec=none]", "-S", f"height:{quality}", "--print", "after_move:filepath", url], capture_output=True, text=True)
    file = result.stdout.strip()
    return change_codec(file, format_type, codec)