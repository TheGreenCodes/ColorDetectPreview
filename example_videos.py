from colordetect import VideoColor


my_video = VideoColor('media/SampleTree.mp4')

video_colors = my_video.get_video_frames( progress=True)

print(f"{video_colors} \n")

#print(my_video.color_sort(color_count=6))