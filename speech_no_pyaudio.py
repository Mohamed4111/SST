#!/usr/bin/env python3
import speech_recognition as sr
import sys
import os

def test_without_pyaudio():
    """
    Test speech recognition without PyAudio dependency.
    """
    print("🎤 Speech-to-Text Demo (No PyAudio Required)")
    print("=" * 50)
    
    recognizer = sr.Recognizer()
    
    # Try different audio sources
    audio_sources = []
    
    # Check for available microphones
    try:
        print("🔍 Checking for available audio sources...")
        mic_list = sr.Microphone.list_microphone_names()
        print(f"Found {len(mic_list)} audio sources:")
        for i, mic in enumerate(mic_list):
            print(f"  {i}: {mic}")
            audio_sources.append(sr.Microphone(device_index=i))
    except Exception as e:
        print(f"❌ Error accessing microphones: {e}")
        return False
    
    if not audio_sources:
        print("❌ No audio sources found!")
        return False
    
    # Try the first available microphone
    try:
        print(f"\n🎯 Using audio source: {mic_list[0]}")
        print("Please say something for 3 seconds...")
        
        with audio_sources[0] as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
        
        print("🔄 Processing...")
        text = recognizer.recognize_google(audio)
        print(f"✅ Success! You said: '{text}'")
        return True
        
    except sr.WaitTimeoutError:
        print("❌ No audio detected. Check your microphone.")
        return False
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
        return False
    except sr.RequestError as e:
        print(f"❌ Speech recognition service error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def install_alternatives():
    """
    Provide installation alternatives for PyAudio.
    """
    print("\n🔧 PyAudio Installation Alternatives:")
    print("=" * 40)
    
    print("1. Try conda (if you have Anaconda/Miniconda):")
    print("   conda install pyaudio")
    print()
    
    print("2. Download pre-compiled wheel:")
    print("   python -m pip install https://download.lfd.uci.edu/pythonlibs/archived/PyAudio-0.2.11-cp312-cp312-win_amd64.whl")
    print()
    
    print("3. Install Microsoft Visual C++ Build Tools first, then:")
    print("   python -m pip install pyaudio")
    print()
    
    print("4. Use Windows Subsystem for Linux (WSL) if available")
    print()
    
    print("5. Try this alternative audio library:")
    print("   python -m pip install sounddevice")
    print("   python -m pip install numpy")

def create_audio_file_demo():
    """
    Create a demo that works with audio files instead of live mic.
    """
    demo_code = '''#!/usr/bin/env python3
"""
Audio File Speech-to-Text Demo
Works with pre-recorded audio files.
"""

import speech_recognition as sr
import os

def transcribe_audio_file(file_path):
    """
    Transcribe speech from an audio file.
    """
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return
    
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(file_path) as source:
            print(f"🎵 Loading audio file: {file_path}")
            audio = recognizer.record(source)
        
        print("🔄 Processing...")
        text = recognizer.recognize_google(audio)
        print(f"✅ Transcription: {text}")
        
    except sr.UnknownValueError:
        print("❌ Could not understand the audio file.")
    except sr.RequestError as e:
        print(f"❌ Speech recognition service error: {e}")

if __name__ == "__main__":
    # Example usage
    audio_file = input("Enter path to audio file (or press Enter to skip): ").strip()
    if audio_file:
        transcribe_audio_file(audio_file)
    else:
        print("No audio file provided.")
'''
    
    with open("audio_file_demo.py", "w") as f:
        f.write(demo_code)
    
    print("📁 Created 'audio_file_demo.py' - works with audio files instead of live mic")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Test speech recognition (try without PyAudio)")
    print("2. Show PyAudio installation alternatives")
    print("3. Create audio file demo")
    
    choice = input("\nEnter choice (1, 2, or 3): ").strip()
    
    if choice == "1":
        success = test_without_pyaudio()
        if not success:
            print("\n💡 If this didn't work, try the installation alternatives (option 2)")
    elif choice == "2":
        install_alternatives()
    elif choice == "3":
        create_audio_file_demo()
    else:
        print("Invalid choice. Exiting...")
