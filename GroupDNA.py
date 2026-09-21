import numpy as np
from datetime import datetime

with open("chat.md", "r", encoding="utf-8") as file:
    chat_lines = file.readlines()

messages = []
current_date = None
current_message = None

for line in chat_lines:

    line = line.rstrip()

    if line.strip() == "":
        continue

    if line.startswith("## "):

        date_text = line[3:].strip()

        try:
            current_date = datetime.strptime(
                date_text,
                "%B %d, %Y"
            )
        except ValueError:
            current_date = None

        continue

    if line.startswith("[") and "]" in line:

        time_end = line.find("]")
        time_text = line[1:time_end]

        rest = line[time_end + 1:].strip()

        if rest.startswith("**") and ":**" in rest:

            sender_end = rest.find(":**")

            sender = rest[2:sender_end]
            text = rest[sender_end + 3:].strip()

            if current_message is not None:
                messages.append(current_message)

            current_message = {
                "date": current_date,
                "time": time_text,
                "sender": sender,
                "text": text
            }

        else:

            if current_message is not None:
                messages.append(current_message)
                current_message = None

    else:

        if current_message is not None:
            current_message["text"] += " " + line.strip()

if current_message is not None:
    messages.append(current_message)

participants = {}
dates = []

for message in messages:

    sender = message["sender"]

    if sender not in participants:
        participants[sender] = 0

    participants[sender] += 1

    if message["date"] is not None:
        dates.append(message["date"])

sorted_participants = sorted(
    participants.items(),
    key=lambda x: x[1],
    reverse=True
)

day_counts = {}
hour_counts = {}

for message in messages:

    date = message["date"]
    time_text = message["time"]

    date_key = date.strftime("%d %B %Y")

    if date_key not in day_counts:
        day_counts[date_key] = 0

    day_counts[date_key] += 1

    time_value = datetime.strptime(
        time_text,
        "%I:%M %p"
    )

    hour = time_value.hour

    if hour not in hour_counts:
        hour_counts[hour] = 0

    hour_counts[hour] += 1

busiest_day = max(
    day_counts,
    key=day_counts.get
)

busiest_hour = max(
    hour_counts,
    key=hour_counts.get
)

participants_list = [
    name for name, count in sorted_participants
]

activity_matrix = np.zeros(
    (len(participants_list), 24),
    dtype=int
)

for message in messages:

    sender = message["sender"]

    time_value = datetime.strptime(
        message["time"],
        "%I:%M %p"
    )

    hour = time_value.hour

    row = participants_list.index(sender)

    activity_matrix[row][hour] += 1

word_counts = {}

for message in messages:

    text = message["text"].lower()

    words = text.split()

    for word in words:

        word = word.strip(
            ".,!?;:()[]{}\"'"
        )

        if len(word) > 2:

            if word not in word_counts:
                word_counts[word] = 0

            word_counts[word] += 1

top_words = sorted(
    word_counts.items(),
    key=lambda x: x[1],
    reverse=True
)

message_times = []

for message in messages:

    time_value = datetime.strptime(
        message["time"],
        "%I:%M %p"
    )

    message_datetime = message["date"].replace(
        hour=time_value.hour,
        minute=time_value.minute
    )

    message_times.append(message_datetime)

gaps = []

for i in range(1, len(message_times)):

    gap = (
        message_times[i]
        - message_times[i - 1]
    )

    gaps.append(
        gap.total_seconds() / 60
    )

if gaps:

    average_gap = sum(gaps) / len(gaps)
    longest_gap = max(gaps)

else:

    average_gap = 0
    longest_gap = 0

archetypes = {}

for name, count in sorted_participants:

    if count >= 20:
        archetype = "The Chatterbox"

    elif count >= 10:
        archetype = "The Regular"

    elif count >= 5:
        archetype = "The Supporter"

    else:
        archetype = "The Silent Observer"

    archetypes[name] = archetype

print()
print("=" * 65)
print("                         GROUPDNA")
print("=" * 65)

print()
print("GROUP OVERVIEW")
print("-" * 65)

print(f"Total messages     : {len(messages)}")
print(f"Total participants : {len(participants)}")

if dates:

    print(
        f"Chat started       : "
        f"{min(dates).strftime('%d %B %Y')}"
    )

    print(
        f"Chat ended         : "
        f"{max(dates).strftime('%d %B %Y')}"
    )

print()
print("MESSAGES BY PARTICIPANT")
print("-" * 65)

for name, count in sorted_participants:

    percentage = (count / len(messages)) * 100

    print(
        f"{name}: {count} messages "
        f"({percentage:.1f}%)"
    )

print()
print("MOST ACTIVE")
print("-" * 65)

print(
    f"Busiest day  : "
    f"{busiest_day} "
    f"({day_counts[busiest_day]} messages)"
)

print(
    f"Busiest hour : "
    f"{busiest_hour:02d}:00 - "
    f"{(busiest_hour + 1) % 24:02d}:00 "
    f"({hour_counts[busiest_hour]} messages)"
)

print()
print("ACTIVITY HEATMAP")
print("-" * 65)

print(
    "Participant".ljust(25),
    end=""
)

for hour in range(24):
    print(f"{hour:02d}", end=" ")

print()

for i, name in enumerate(participants_list):

    print(name.ljust(25), end="")

    for hour in range(24):

        count = activity_matrix[i][hour]

        if count == 0:
            symbol = " "

        elif count <= 1:
            symbol = "░"

        elif count <= 3:
            symbol = "▒"

        else:
            symbol = "█"

        print(f" {symbol} ", end="")

    print()

print()
print("TOP 10 WORDS")
print("-" * 65)

for word, count in top_words[:10]:

    print(
        f"{word}: {count}"
    )

print()
print("RESPONSE SPEED & SILENT STREAKS")
print("-" * 65)

print(
    f"Average message gap : "
    f"{average_gap:.1f} minutes"
)

print(
    f"Longest silent gap  : "
    f"{longest_gap:.1f} minutes"
)

print()
print("PERSONALITY ARCHETYPES")
print("-" * 65)

for name, archetype in archetypes.items():

    print(
        f"{name}: {archetype}"
    )

print()
print("=" * 65)