import time
import random

print("\033[91m")
print("TikTok Bot by SpeedCoder")
print("------------------------")
print("1. Send Followers")
print("2. Send Likes")
print("3. Send Views")
print("4. Send Saves")
print("------------------------")

option = input("Enter your choice: ")

video_link = input("Enter the TikTok video link: ")

if option == "1":
    num_followers = int(input("Enter the number of followers to send: "))
    print(f"Sending followers to {video_link}...")
    for i in range(num_followers):
        print(f"Sending follower {i+1} of {num_followers}...")
        time.sleep(random.uniform(0.001, 0.005))  # Simulate a delay
    print("Followers successfully sent!")
elif option == "2":
    num_likes = int(input("Enter the number of likes to send: "))
    print(f"Sending likes to {video_link}...")
    for i in range(num_likes):
        print(f"Sending like {i+1} of {num_likes}...")
        time.sleep(random.uniform(0.001, 0.005))  # Simulate a delay
    print("Likes successfully sent!")
elif option == "3":
    num_views = int(input("Enter the number of views to send: "))
    print(f"Sending views to {video_link}...")
    for i in range(num_views):
        print(f"Sending view {i+1} of {num_views}...")
        time.sleep(random.uniform(0.001, 0.005))  # Simulate a delay
    print("Views successfully sent!")
elif option == "4":
    num_saves = int(input("Enter the number of saves to send: "))
    print(f"Sending saves to {video_link}...")
    for i in range(num_saves):
        print(f"Sending save {i+1} of {num_saves}...")
        time.sleep(random.uniform(0.001, 0.005))  # Simulate a delay
    print("Saves successfully sent!")
else:
    print("Invalid option. Please try again.")