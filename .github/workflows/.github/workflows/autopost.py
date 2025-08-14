import os

LOG_FILE = "posted_files.txt"

def get_posted_files():
    if not os.path.exists(LOG_FILE):
        return set()
    with open(LOG_FILE, "r") as f:
        return set(line.strip() for line in f if line.strip())

def log_posted_file(filename):
    with open(LOG_FILE, "a") as f:
        f.write(filename + "\n")

def pick_new_file_from_drive():
    # TODO: Replace with Google Drive API code to list files in folder
    all_files = ["video1.mp4", "video2.mp4", "photo1.jpg"]  # Example placeholder
    posted_files = get_posted_files()

    for file in all_files:
        if file not in posted_files:
            return file
    return None

if __name__ == "__main__":
    file_to_post = pick_new_file_from_drive()
    if not file_to_post:
        print("No new files to post today.")
        exit()

    # TODO: Add code to post to Meta & TikTok here
    print(f"Posting: {file_to_post}")

    # Log the posted file
    log_posted_file(file_to_post)
