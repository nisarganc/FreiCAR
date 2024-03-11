from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("3_localization/localization_lowvariance.mp4")

videoClip.write_gif("3_localization/localization_lowvariance.gif")