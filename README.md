# Voice Assistant Loki

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Functionality](#functionality)

## Introduction

Voice Assistant Loki is a Python-based voice assistant designed to perform a variety of tasks through voice commands. It uses text-to-speech and speech recognition technologies to interact with users and execute commands such as searching Wikipedia, opening web pages, playing music, and sending emails. 

<img width="735" alt="image" src="https://github.com/user-attachments/assets/772c17ac-338f-4487-9fcb-dd43d2813357">

## Features

- **Speech Recognition**: Listens to and processes voice commands.
- **Text-to-Speech**: Responds to user commands with audible speech.
- **Wikipedia Search**: Searches Wikipedia for a given query and reads out a summary.
- **Web Browsing**: Opens popular websites like YouTube, Google, and Stack Overflow.
- **Music Playback**: Plays specified music from the local system.
- **Time Query**: Provides the current time.
- **Video Playback**: Plays a specific video file from the local system.
- **Email Sending**: Sends emails using a Gmail account.

## Functionality

### Speech Recognition
- **Library**: `speech_recognition`
- **Function**: `takecommand()`
- **Description**: Captures audio input from the microphone and converts it to text using Google Web Speech API.

### Text-to-Speech
- **Library**: `pyttsx3`
- **Function**: `speak()`
- **Description**: Converts text to speech and speaks it out.

### Wikipedia Search
- **Library**: `wikipedia`
- **Function**: `search Wikipedia`
- **Description**: Searches for a query on Wikipedia and reads out the summary.

### Web Browsing
- **Library**: `webbrowser`
- **Functions**: `open YouTube`, `open Google`, `open Stack Overflow`
- **Description**: Opens specified websites in the default web browser.

### Music Playback
- **Library**: `os`
- **Function**: `play music`
- **Description**: Plays a specified music file from the local system.

### Time Query
- **Library**: `datetime`
- **Function**: `time`
- **Description**: Provides the current time.

### Video Playback
- **Library**: `os`
- **Function**: `introduce`
- **Description**: Plays a specified video file from the local system.

### Email Sending
- **Library**: `smtplib`
- **Function**: `sendemail()`
- **Description**: Sends an email using a Gmail account.

## Technologies Used

- **Python**: The primary programming language used.
- **Libraries**: `pyttsx3`, `speech_recognition`, `wikipedia`, `webbrowser`, `os`, `smtplib`, `datetime`




