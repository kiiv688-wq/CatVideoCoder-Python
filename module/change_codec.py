import subprocess
from pathlib import Path

def change_codec(file, format_type, codec):
    if format_type=="Video":
        if codec == 0:
            p=Path(file)
            file2 = str(p.with_suffix(".mov"))
            subprocess.run(["ffmpeg", "-i", file, "-c:v", "prores", "-profile:v", "3", "-c:a", "pcm_s24le", file2])
            subprocess.run(["rm", file])
        elif codec == 1:
            p=Path(file)
            file2 = str(p.with_suffix(".mxf"))
            subprocess.run(["ffmpeg", "-i", file, "-c:v", "dnxhd", "-profile:v", "dnxhr_hq", "-c:a", "pcm_s24le", file2])
            subprocess.run(["rm", file])
        elif codec == 2:
            p=Path(file)
            file2 = str(p.with_suffix(".mkv"))
            if str(p) == file2:
                file2=str(p.with_name(p.stem + "1" + p.suffix))
            else:
                pass
            subprocess.run(["ffmpeg", "-i", file, "-c:v", "libsvtav1", "-crf", "30", "-preset", "6", "-c:a", "pcm_s24le", file2])
            subprocess.run(["rm", file])
    elif format_type=="Only Audio":
        p=Path(file)
        file2 = str(p.with_suffix(".wav"))
        subprocess.run(["ffmpeg", "-i", file, "-acodec", "pcm_s24le", file2])
        subprocess.run(["rm", file])
    else:
        if codec == 0:
            p=Path(file)
            file2 = str(p.with_suffix(".mov"))
            subprocess.run(["ffmpeg", "-i", file, "-c:v", "prores", "-profile:v", "3", "-an", file2])
        elif codec == 1:
            p=Path(file)
            file2 = str(p.with_suffix(".mxf"))
            subprocess.run(["ffmpeg", "-i", file, "-c:v", "dnxhd", "-profile:v", "dnxhr_hq", "-an", file2])
            subprocess.run(["rm", file])
        elif codec == 2:
            p=Path(file)
            file2 = str(p.with_suffix(".mkv"))
            subprocess.run(["ffmpeg", "-i", file, "-c:v", "libsvtav1", "-crf", "30", "-preset", "6", "-an", file2])
            subprocess.run(["rm", file])