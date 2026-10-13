import json 
import pandas as pd

with open("/home/mohan/Desktop/01_insta_likes_1_year/your_instagram_activity/likes/liked_posts.json", "r") as file:
    data = json.load(file)


df = pd.DataFrame(data)

print(f"Maine 1 saal me {len(df)} reels like kari hain.")


with open("/home/mohan/Desktop/01_insta_likes_1_year/your_instagram_activity/likes/liked_comments.json", "r") as file2:
    data_02 = json.load(file2)

df_02 = pd.DataFrame(data_02)

print(f"comments liker: {len(df_02)}")



