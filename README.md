# Intro to Cooper The WatchDog 
Cooper is a vigilant watchdog equipped with CCTV and OpenAI GPT/Amazon Rekognition capabilities, 
dedicated to monitoring any suspicious activities in and around your house.

# Features
- Analyzes events captured in videos.
- Alerts you in case of any suspicious activities detected.

# Prerequisite
- A CCTV system supporting RTSP. You need to set up the hardware and ensure it's accessible, either via the Internet or locally.
- A Python environment
- A OpenAI API Key or AWS access credential

# Installation
To run Cooper the WatchDog, follow these steps:

1) Install dependencies:
```bash
pip install -r requirements.txt
```

2) Read the video stream and capture events
```bash
./Monitor.py
```

3) Analyze events
```bash
./Analyze.py
```

# Current Issues
- While the analysis by GPT-4 Vision is impressive, it lacks consistency. The same photo may yield vastly different results.
- Event capturing is processed locally, which is CPU-intensive and prone to failure.

# Todo
- Implement alerts via WhatsApp or other messaging channels.
- Refine the prompts to ensure stable and predictable analysis.
- Improve the algorithm for local event capturing.
- Make both Analyze and Monitor daemon process.

# Contact
For more information, please feel free to reach out to me at [@lipingtababa](https://github.com/lipingtababa)


