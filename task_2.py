"""Task 2. Module to convert TikTok video to GIF."""
import os
from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip


def tiktok_video_to_gif(url):
    """function that converts TikTok video to GIF"""
    # Downloading TikTok video to local PC
    # Connecting via TikTokApi
    with TikTokApi() as api:
        print("Downloading video from TikTok.......")
        video = api.video(url=url)
        video_data = video.bytes()
        # Unique video file name using TikTok video id
        video_name = video.info()['id']
        # Writing video to file
        with open(video_name, "wb") as out_file:
            out_file.write(video_data)
        out_file.close()
        print("Download completed!")

    # Converting downloaded video to GIF
    # Using TikTok id for the name of .gif file
    gif_name = video_name + ".gif"
    video_clip = VideoFileClip(video_name)
    video_clip.write_gif(gif_name)
    print("Converting video to GIF completed!")
    # Removing the video file
    os.remove(video_name)
    print("Path of the created GIF: " + os.path.abspath(gif_name))
    return os.path.abspath(gif_name)


def main():
    """main() function"""
    user_url = input("Enter the TikTok video url:\n")
    tiktok_video_to_gif(user_url)


main()
