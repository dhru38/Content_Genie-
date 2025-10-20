import ffmpeg

def create_video () : 
    input_video = ffmpeg.input("background.webm")
    input_audio = ffmpeg.input("Story.mp3")
    (
        ffmpeg
        .output(input_video, input_audio, "final_video.mp4", shortest=None, vcodec="libx264", acodec="aac")
        .run()
    )
