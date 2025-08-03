# Cooper The WatchDog - AI-Powered Home Security Monitoring System

Cooper is an intelligent home security monitoring system that combines CCTV surveillance with advanced AI capabilities from OpenAI GPT-4 Vision and Amazon Rekognition to detect and alert you about suspicious activities around your property.

## Overview

This project provides automated surveillance monitoring by:
- Capturing video streams from RTSP-compatible CCTV cameras
- Processing video frames to detect motion and changes in specific regions of interest
- Using AI (OpenAI GPT-4 Vision or AWS Rekognition) to analyze captured images for suspicious activities
- Generating alerts when potential security concerns are detected

## Key Components

- **Monitor.py**: Captures video streams from CCTV cameras via RTSP, detects motion in configured regions of interest, and saves relevant frames
- **Analyze.py**: Processes captured images using AI to identify suspicious activities or security concerns
- **OpenAIAnalyst.py**: Implements GPT-4 Vision analysis for image interpretation
- **AWSAnalyst.py**: Alternative implementation using Amazon Rekognition for image analysis
- **SituationHandler.py**: Manages alert generation and response actions based on analysis results

## Features

- **Real-time Video Monitoring**: Connects to RTSP-compatible CCTV systems for continuous surveillance
- **Motion Detection**: Identifies changes in specific regions of the video frame to trigger analysis
- **AI-Powered Analysis**: Uses state-of-the-art computer vision AI to understand what's happening in captured images
- **Configurable Regions of Interest**: Focus monitoring on specific areas (e.g., excluding public roads)
- **Multi-Channel Support**: Monitor multiple camera feeds simultaneously
- **Automated Alert System**: Receive notifications when suspicious activities are detected

## Prerequisites

- CCTV system with RTSP support (accessible via network)
- Python 3.x environment
- OpenAI API key (for GPT-4 Vision) OR AWS credentials (for Rekognition)
- Sufficient local storage for captured images

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd cooper-watchdog
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your settings:
   - Copy `config.py.example` to `config.py` (if provided)
   - Add your RTSP camera details (address, port, username, password)
   - Add your OpenAI API key or AWS credentials

## Usage

### Step 1: Start Video Monitoring
```bash
./Monitor.py
```
This process continuously monitors your camera feeds, detects motion, and saves relevant frames to the `./data/motions/` directory.

### Step 2: Analyze Captured Events
```bash
./Analyze.py
```
This analyzes the captured images using AI to identify potential security concerns and triggers appropriate alerts.

## Configuration

The system can be configured to:
- Monitor specific camera channels (front door, deck, etc.)
- Define custom regions of interest to exclude areas like public roads
- Adjust motion detection sensitivity
- Choose between OpenAI or AWS for image analysis

## Architecture

```
CCTV Cameras (RTSP) → Monitor.py → Motion Detection → Image Capture
                                                           ↓
                                                      Analyze.py
                                                           ↓
                                          AI Analysis (OpenAI/AWS)
                                                           ↓
                                                  SituationHandler
                                                           ↓
                                                    Alert/Action
```

## Current Limitations

- AI analysis consistency can vary - the same image may produce different results
- Local video processing is CPU-intensive
- Both Monitor and Analyze currently run as foreground processes

## Planned Improvements

- WhatsApp/SMS integration for instant alerts
- Improved AI prompts for more consistent analysis
- Optimized motion detection algorithms
- Daemon mode for background operation
- Web interface for remote monitoring
- Historical event logging and review

## Security Note

This system is designed for legitimate home security monitoring. Ensure you comply with local laws regarding video surveillance and privacy when deploying this system.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Contact

For questions or support, please reach out to [@lipingtababa](https://github.com/lipingtababa)


