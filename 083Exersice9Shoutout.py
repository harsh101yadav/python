import win32com.client

# print(help(win32api))

# # Get the current username
# username = win32api.GetUserName()
# print("Current username:", username)

# # Get the system directory
# system_directory = win32api.GetSystemDirectory()
# print("System directory:", system_directory)
# print((win32com.client.__dict__))
speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["Harsh Yadav","Ayush Taunk","Shubham Bankar","Suraj Srinath","Yash Sisodiya","Jaaaaaaaaaaaaaaay"]
for name in l:
    speaker.Speak(f"Hello to {name}")

# k = """Hmmmmmmmmmmm..
# Kiska hai yeh tumko intezar main hoon nah
# Dekh lo idhar to ek baar main hoon nah
# Kiska hai yeh tumko intezar main hoon nah
# Dekh lo idhar to ek baar main hoon nah
# Khamosh kyun ho jo bhi kehna hai kaho
# Dil chaahe jitna pyaar utna maang lo ho..
# Tumko milega utna pyaar main hoon nah
# Kiska hai yeh tumko intezar main hoon nah
# Dekh lo idhar to ek baar main hoon nah"""

# speaker.Speak(k)