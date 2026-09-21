# Minor_project_1
About GroupDNA
# 🧬 GroupDNA

### Spotify Wrapped, but for your Friend Group 💬📊

**GroupDNA** is a Python-based WhatsApp chat analysis project that transforms a WhatsApp chat export into meaningful group statistics and activity insights.

It analyzes communication patterns and generates a text-based report showing participant activity, busiest periods, frequently used words, response gaps, activity patterns, and simple personality-style archetypes.

---

## 🚀 Features

* 📊 Total number of messages
* 👥 Total number of participants
* 📅 Chat start and end dates
* 🗣️ Messages sent by each participant
* 📈 Message percentage of each participant
* 🔥 Busiest day
* ⏰ Busiest hour
* 🌡️ 24-hour activity heatmap
* 🔤 Top 10 frequently used words
* ⚡ Average message gap
* 🤫 Longest silent gap
* 🧩 Participant activity archetypes

---

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Datetime**
* **WhatsApp Chat Export**

---

## ⚙️ How It Works

The project follows a simple data-analysis pipeline:

```text
WhatsApp Chat Export
        ↓
      chat.md
        ↓
Message Parsing
        ↓
Extract Date, Time, Sender & Message
        ↓
Data Analysis
        ↓
 ┌──────────────────────────────┐
 │ Participant Statistics       │
 │ Busiest Day & Hour          │
 │ Activity Heatmap             │
 │ Word Frequency               │
 │ Response/Silent Gaps         │
 │ Activity Archetypes          │
 └──────────────────────────────┘
        ↓
   GROUPDNA REPORT
```

### 1. Import the chat

Export your WhatsApp group chat and convert/use the chat data in the required Markdown format.

GroupDNA reads the `chat.md` file and processes it line by line.

### 2. Parse the messages

The program identifies:

* Date
* Time
* Sender
* Message text

It stores the extracted information so that it can be analyzed later.

### 3. Analyze participants

The program counts how many messages each participant has sent and sorts participants according to their message count.

It also calculates the percentage of total messages contributed by each participant.

### 4. Find the most active periods

GroupDNA calculates the number of messages for each day and each hour.

It then identifies:

* **Busiest day**
* **Busiest hour**

### 5. Generate an activity heatmap

The project creates a 24-hour activity matrix.

Each participant gets a row, while the columns represent hours from `00` to `23`.

Different symbols represent different activity levels:

```text
░  Low activity
▒  Medium activity
█  High activity
```

### 6. Analyze frequently used words

The program splits message text into individual words, removes basic punctuation, counts word occurrences, and displays the **Top 10 words**.

### 7. Analyze response and silent gaps

The time difference between consecutive messages is calculated.

GroupDNA reports:

* Average message gap
* Longest silent gap

This gives an idea of the communication rhythm of the group.

### 8. Generate activity archetypes

Participants are assigned simple activity-based archetypes according to their message count:

| Messages    | Archetype           |
| ----------- | ------------------- |
| 20 or more  | The Chatterbox      |
| 10–19       | The Regular         |
| 5–9         | The Supporter       |
| Less than 5 | The Silent Observer |

These are simple project labels based on message activity, not psychological assessments.

---

## 📋 Example Output

```text
=================================================================
                         GROUPDNA
=================================================================

GROUP OVERVIEW
-----------------------------------------------------------------
Total messages     : 94
Total participants : 8
Chat started       : 16 April 2026
Chat ended         : 9 May 2026

MESSAGES BY PARTICIPANT
-----------------------------------------------------------------
Participant 1: 25 messages (26.6%)
Participant 2: 18 messages (19.1%)
Participant 3: 14 messages (14.9%)

MOST ACTIVE
-----------------------------------------------------------------
Busiest day  : 28 April 2026
Busiest hour : 19:00 - 20:00

ACTIVITY HEATMAP
-----------------------------------------------------------------
Participant                00 01 02 03 ... 18 19 20 21 22 23

TOP 10 WORDS
-----------------------------------------------------------------
project: 12
guys: 10
today: 8
...

RESPONSE SPEED & SILENT STREAKS
-----------------------------------------------------------------
Average message gap : 18.4 minutes
Longest silent gap  : 620.0 minutes

PERSONALITY ARCHETYPES
-----------------------------------------------------------------
Participant 1: The Chatterbox
Participant 2: The Regular
Participant 3: The Supporter
```

*Example values above are illustrative.*

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your system.

Check using:

```bash
python --version
```

### Step 2: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/GroupDNA.git
```

```bash
cd GroupDNA
```

### Step 3: Install dependencies

```bash
pip install numpy
```

Or:

```bash
pip install -r requirements.txt
```

### Step 4: Add your chat file

Place your `chat.md` file in the same folder as `GroupDNA.py`.

```text
GroupDNA/
├── GroupDNA.py
├── chat.md
└── README.md
```

### Step 5: Run the project

```bash
python GroupDNA.py
```

The analysis will be displayed directly in the terminal.

---

## 📁 Input Format

The project works with a Markdown-formatted WhatsApp chat export containing dates, times, participants, and messages.

Example:

```text
## April 16, 2026

[10:13 AM] **Aditi:** Hello everyone
[10:15 AM] **Bhavini:** Hi!
[10:20 AM] **Aditi:** Let's start the project
```

---

## 🎯 Project Purpose

GroupDNA was created to explore how simple Python data processing can be used to discover patterns in everyday conversations.

Instead of manually going through hundreds of messages, the project automatically extracts useful statistics and presents them in an easy-to-understand report.

---

## 🔮 Future Improvements

* 📊 Graphical dashboards
* 📈 Interactive charts
* 😊 Sentiment analysis
* 😂 Emoji analysis
* 🕒 Individual response-time analysis
* ☁️ Word clouds
* 📱 Support for direct WhatsApp `.txt` exports
* 🌐 Web-based interface using Flask or Streamlit
* 📥 Export results as PDF/CSV

---

## ⚠️ Privacy

This project analyzes chat data locally.

Do not upload private or sensitive conversations to a public repository.

For GitHub, it is recommended to keep your real `chat.md` file private or add it to `.gitignore`.

---

## 👩‍💻 Author

**Kshithija P**

Python | Data Analysis | Machine Learning | Software Development

---

## ⭐ If you like this project

Give the repository a ⭐ and feel free to explore, modify, and improve GroupDNA!
