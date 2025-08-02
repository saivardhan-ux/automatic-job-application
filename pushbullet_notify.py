from pushbullet import Pushbullet

def send_push(message):
    pb = Pushbullet("o.tzmin6P5fPFdv4Pbh5howNXaKSVqGekw")
    push = pb.push_note("Job Application Status", message)
    print("Pushbullet notification sent!")

if __name__ == "__main__":
    send_push("Applied to a job successfully!")