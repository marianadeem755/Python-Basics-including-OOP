import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
while True:
    print("Tell me What do you want to do: ")
    l=["Maria", "Shazia", "Javeria", "Tuba", "Kinza", "Maliha", "Rukhsar", "Riba", "Sughra"]
    s=input()
    for name in l:
        speaker.Speak(f"{s} {name}")
    break