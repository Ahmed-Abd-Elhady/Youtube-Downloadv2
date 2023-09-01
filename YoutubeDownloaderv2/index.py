from tkinter import *  # the gui moduel
import tkinter as tk  # import tikner moduel as tk to easy use it in the code
from PIL import Image, ImageTk  # moduel help me in foramtes
from pytube import YouTube  # imoport youtube downloader
from tkinter import ttk  # import something from tk
from tkinter import filedialog  # file select
import time  # time library
import pyperclip  #
import tkinter.messagebox
import clipboard  # clipboard
import threading  # unfreez
from ttkthemes import ThemedStyle  # thmes color change
import sys  # exit the sys tremnial


# make the tk to root the easy press codes
root = Tk()  # root as Tk()
# basics for the app
root.title("Youtube App Dowload App @konafa")  # title
root.iconbitmap(
    "C:/Users/abelh\OneDrive/Desktop/YoutubeDownloaderv2/app assets/title.ico"
)  # The app icon
root.geometry("800x500")  # make the with and high 800x600 make the app better
root.resizable(width=False, height=False)  # make the wiindow unresized
# background img


image = Image.open(
    "C:/Users/abelh\OneDrive/Desktop/YoutubeDownloaderv2/app assets/backgroundImg.jpg"  # img path
)  # open the img from the app
background_image = ImageTk.PhotoImage(image)  # the can me app
# select the  path
background_label = tk.Label(
    root, image=background_image
)  # here to choose the background make it lable in the root
background_label.place(
    x=0, y=0, relheight=1, relwidth=1
)  # potiion of the background to make it 0 and 0 to make it on all the screen


myLable1 = Label(
    root, text="Welcome to Youtube App Dowload App @konafa"
)  # welcome message in the first of the app to weclome the clients
myLable1.pack(side="top", pady=10)  # potion of this text

myLable1.configure(fg="white")  # background of the text


# youtube things

entry = tk.Entry(
    root,
    width=80,
)  # create the entry and witdh/high
entry.pack()  # potion of the entry
entry.place(x=160, y=200, height=30)


# buttom


# Create a menu
menu = tk.Menu(root, tearoff=0)  # tearoff=0 removes the dashed line


# The Funuion To Downolad the video
def on_button_click():
    url = entry.get()  # convert url from string to youtube object
    if "www.youtube.com" not in url:  # break the funion if not a youtube link
        button["text"] = "Try Again"  # saying try again
        on_button_click()  # req the def again
    button["text"] = "Loading..."  # loading things
    button["state"] = "disabled"  # disable it don't spam
    entry["state"] = "disabled"  # disable it don't spam

    # def geturl():
    # url = entry.get()
    # root.after(0)
    # Get the user input URL
    print(url)  # print the url
    youtube = YouTube(url)  # youtube things
    # video = YouTube(user_input)
    video_stream_1080p = (
        youtube.streams.get_highest_resolution()
    )  # get the high video res
    audio_streams = youtube.streams.filter(
        only_audio=True
    )  # get the audio at the high quilty

    # def to download 1080 when press the buttom
    def downloada():
        save_path = filedialog.askdirectory()  # path to save
        # video_stream_1080p = video_streams.first()
        if video_stream_1080p:  # to save it with file name
            video_filename = f"{youtube.title}.mp4"  # get youtube video name
            video_stream_1080p.download(
                output_path=save_path, filename=video_filename
            )  # save it with the name and path
            print("Video download complete!")  # terminal things
        else:  # if something going wrong
            print("1080p video stream not available.")

    # download audio
    def mp3():
        save_path = filedialog.askdirectory()  # save the folder again if audio
        audio_stream = audio_streams.first()  # make it with sound
        if audio_stream:
            audio_filename = f"{youtube.title}.mp3"  # get youtube video name
            audio_stream.download(
                output_path=save_path, filename=audio_filename
            )  # save it with name and path
            print("Audio download complete!")  # if done therminal things
        else:  #
            print("Audio stream not available.")

    def mp3andone():
        mp3()
        oneclickmp3()

    mp3_button = tk.Button(
        root, text="Audio Only", command=mp3andone, font=15, fg="white"
    )

    # Grid the new button next to the existing button
    mp3_button.place(x=460, y=300)

    def oneclickmp3():
        mp3_button["text"] = "Done✅"
        mp3_button["state"] = "disable"

    def mp4da():
        oneclickmp3()
        downloada()

    mp4_button = tk.Button(
        root, text="Highest Quilty", command=mp4da, font=15, fg="white"
    )

    # Grid the new button next to the existing button
    mp4_button.place(x=300, y=300)
    button["text"] = "Convert Again?"
    button["state"] = "normal"
    button.place(x=360, y=240)
    entry["state"] = "normal"


# menu.add_command(label="720p Mp3", command=downloada)


button = tk.Button(root, text="Convert", command=on_button_click, font=15, fg="white")
button.pack()
button.place(x=370, y=240)
# youtube things


# clipboard buttom
def paste_from_clipboard():
    try:
        clipboard_text = pyperclip.paste()  # Get text from clipboard
        entry.delete(0, tk.END)  # Clear the current entry text
        entry.insert(0, clipboard_text)  # Insert clipboard text into the entry
    except:
        tk.messagebox.showerror("Error", "Could not retrieve text from clipboard")


def execute_both_commands():
    paste_from_clipboard()
    on_button_click()


paste_button = tk.Button(
    root,
    text="Paste from Clipboard",
    command=execute_both_commands,
    font=14,
    fg="white",
)
paste_button.pack()

last_clipboard_content = ""


def get_clipboard_link():
    global last_clipboard_content
    clipboard_content = clipboard.paste()
    if (
        "www.youtube.com" in clipboard_content
        and clipboard_content != last_clipboard_content
    ):
        entry.delete(0, tk.END)
        entry.insert(0, clipboard_content)
        on_button_click()
        last_clipboard_content = clipboard_content


def auto_paste():
    while True:
        get_clipboard_link()
        time.sleep(2)  # Adjust the interval as needed


auto_paste_thread = threading.Thread(target=auto_paste)
auto_paste_thread.start()


def on_closing():
    # Add any cleanup or confirmation logic here
    root.destroy()  # Close the window
    sys.exit()  # Exit the script


root.protocol("WM_DELETE_WINDOW", on_closing)  # Bind the event
button13 = tk.Button(root, text="Exit", command=on_closing, font=12, fg="white")
button13.place(x=12, y=13)
# selection


root.mainloop()  # main loop to make the app dosen't close for ever :)
