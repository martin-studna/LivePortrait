import ffmpeg

# File paths
base_video = '1part.mp4'
insert_video1 = 'einstein.mp4'
insert_video2 = 'shiba.mp4'
output = 'output_video.mp4'

# Define crop position and size
x1 = 1507  # top-right x
y1 = 697  # top-right y
w1 = 320  # width of cropped area
h1 = 230  # height of cropped area

x2 = 1920 - 1507 - 320  # top-left x
y2 = 697  # top-left y
w2 = 320  # width of cropped area
h2 = 230  # height of cropped area

# Load base and overlay video
main = ffmpeg.input(base_video)
overlay1 = ffmpeg.input(insert_video1)
overlay2 = ffmpeg.input(insert_video2)

# Resize overlay video to match cropped area
overlay_scaled1 = overlay1.video.filter('scale', w1, h1)
overlay_scaled2 = overlay2.video.filter('scale', w2, h2)

# Overlay the resized video onto the base video at (x, y)
out1 = ffmpeg.overlay(main.video, overlay_scaled1, x=x1, y=y1)
out2 = ffmpeg.overlay(out1.video, overlay_scaled2, x=x2, y=y2)


out2.output(output).run()
