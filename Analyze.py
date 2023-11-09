#!/usr/bin/env python3

from OpenAIAnalyst import OpenAIAnalyst

if __name__ == "__main__":
    analyst = OpenAIAnalyst("./data/motions/deck")
    analyst.analyze_images()
    