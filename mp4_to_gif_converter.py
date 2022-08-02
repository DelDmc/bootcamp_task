import os
import string
import random
import re

from TikTokApi import TikTokApi
from moviepy.video.io.VideoFileClip import VideoFileClip

dump_directory = os.path.join(os.getcwd(), 'mp4')
gif_directory = os.path.join(os.getcwd(), 'gif')


def find_video_id_from_url(tiktok_url):
    return re.findall(r'/.*/(\d*)?', tiktok_url)


def fetch_video_from_tik_tok(video_id, file_name):
    with TikTokApi() as api:
        video = api.video(id=video_id)
        video_data = video.bytes()
        with open(f"{dump_directory}/{file_name}.mp4", "wb") as f:
            f.write(video_data)


def tiktok_mp4_to_gif(file_name, fps=4, target_resolution=(256, 144)):
    os.makedirs(dump_directory, exist_ok=True)
    os.makedirs(gif_directory, exist_ok=True)
    video = VideoFileClip(f"{dump_directory}/{file_name}.mp4", target_resolution)
    video.write_gif(f"{gif_directory}/{file_name}.gif", fps)


def convert_tiktok_mp4_to_gif(tiktok_url, file_name, fps=4, target_resolution=(256, 144)):
    video_id = find_video_id_from_url(tiktok_url)[0]
    fetch_video_from_tik_tok(video_id, file_name)
    tiktok_mp4_to_gif(file_name, fps, target_resolution)
    os.remove(f"{dump_directory}/{file_name}.mp4")


if __name__ == "__main__":
    name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    url = 'https://www.tiktok.com/@semihvarol/video/7124254103219277058?is_from_webapp=1&sender_device=pc'
    convert_tiktok_mp4_to_gif(url, name, fps=1)


