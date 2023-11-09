#!/usr/bin/env python3

# here we should import env
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

rtsp_address = os.getenv("RTSP_ADDRESS")
rtsp_port = os.getenv("RTSP_PORT")
rtsp_username = os.getenv("RTSP_USERNAME")
rtsp_password = os.getenv("RTSP_PASSWORD")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")