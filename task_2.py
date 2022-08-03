"""Task 2. Module to convert TikTok video to GIF."""
import os
from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip


# https://www.youtube.com/shorts/NC4G_WnuKYs
# "https://vm.tiktok.com/ZMNqhVbcV/?k=1"
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
    try:
        tiktok_video_to_gif(user_url)
    # TypeError will occur if the link is not broken, but is not TikTok video link
    except TypeError:
        print("Entered URL is not TikTok video URL. Below is an example of a supported URL.\nhttps://www.tiktok.com/@therock/video/6829267836783971589"
              )
    # Exception for broken links
    except:
        print(
            f"Connection error. Please, check the link {user_url} for mistakes.")


main()
