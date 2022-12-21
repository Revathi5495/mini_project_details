
'''import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
messagebox.askyesno("question","want to enable bluetooth",)#asks to enable bluetooth

root.mainloop()'''

import asyncio

#popup message code
#from tkinter import messagebox
#root = tk.Tk()
#root.wm_title("question")
#lable = tk.Label(root, text=msg)
#lable.pack(side="top", fill="x", pady=10)
#B1 = tk.Button(root,text ="yes", command = root.quit)
#B1.pack()
#B2 = tk.Button(root, test ="no", command = root.destroy)
#B2.pack























#.......main program to turn on bluetooth starting.........

from winrt.windows.devices import radios

async def bluetooth_power(turn_on):
    all_radios = await radios.Radio.get_radios_async()
    for this_radios in all_radios:
        if this_radios.kind == radios.RadioKind.BLUETOOTH:
            if turn_on:
                result = await this_radios.set_state_async(radios.RadioState.ON)
            else:
                result = await this_radios.set_state_async(radios.RadioState.OFF)

if __name__ == '__main__':
    asyncio.run(bluetooth_power(True))
'''..............main program to turn on bluetooth ending.............'''


