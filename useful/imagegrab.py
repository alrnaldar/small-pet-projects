
import tkinter as tk
import asyncio
import aiohttp

from io import BytesIO
from PIL import Image, ImageTk


class AsyncTk(tk.Tk):
    

    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.done = True

    async def updater(self):
        self.done = False
        while not self.done:
            self.update()
            await asyncio.sleep(0.05)

    def mainloop(self):
        asyncio.get_event_loop().run_until_complete(self.updater())


async def fetch_image(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        if response.status != 200:
            label.config(text=f'HTTP error {response.status}')
        else:
            content = await response.content.read()
            pil_image = Image.open(BytesIO(content))
            image = ImageTk.PhotoImage(pil_image)
            label.config(image=image, text='')
            label.image = image

    button.config(state=tk.NORMAL)


def load_image():
    url = url_entry.get()
    button.config(state=tk.DISABLED)
    # label.config(text='загрузка изоображения...')
    asyncio.ensure_future(fetch_image(url))

def on_entry_click(event):
    button = tk.Button(root, text='найти картинку', command=load_image)
    button.place(x=200,y=0)
    if url_entry.get() == "вводите url картинки":
        url_entry.delete(0, "end")

root = AsyncTk()

root.geometry("300x500")
root.title("dfasfafa")


label = tk.Label(root)
label.place(x=0,y=28)

url_entry = tk.Entry(root)
url_entry.place(x=0,y=0)
url_entry.insert(0, "вводите url картинки")
url_entry.bind('<FocusIn>', on_entry_click)
root.mainloop()
