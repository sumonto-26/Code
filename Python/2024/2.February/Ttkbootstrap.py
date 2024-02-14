'''import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

b1 = ttk.Button(root, text='primary', bootstyle=PRIMARY)
b1.pack(side=LEFT, padx=5, pady=5)

b2 = ttk.Button(root, text='secondary', bootstyle=SECONDARY)
b2.pack(side=LEFT, padx=5, pady=5)

b3 = ttk.Button(root, text='success', bootstyle=SUCCESS)
b3.pack(side=LEFT, padx=5, pady=5)

b4 = ttk.Button(root, text='info', bootstyle=INFO)
b4.pack(side=LEFT, padx=5, pady=5)

b5 = ttk.Button(root, text='warning', bootstyle=WARNING)
b5.pack(side=LEFT, padx=5, pady=5)

b6 = ttk.Button(root, text='danger', bootstyle=DANGER)
b6.pack(side=LEFT, padx=5, pady=5)

b7 = ttk.Button(root, text='light', bootstyle=LIGHT)
b7.pack(side=LEFT, padx=5, pady=5)

b8 = ttk.Button(root, text='dark', bootstyle=DARK)
b8.pack(side=LEFT, padx=5, pady=5)

root.mainloop()
'''

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

b1 = ttk.Button(root, text="Solid Button", style=SUCCESS)
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Outline Button", style=(SUCCESS, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

# Default toolbutton style
toolbutton1 = ttk.Checkbutton(root, text="Default Toolbutton", style="toolbutton")
toolbutton1.pack(side=LEFT, padx=5, pady=10)

# Success toolbutton style
toolbutton2 = ttk.Checkbutton(root, text="Success Toolbutton", style="success-toolbutton")
toolbutton2.pack(side=LEFT, padx=5, pady=10)

# Default outline toolbutton style
toolbutton3 = ttk.Checkbutton(root, text="Default Outline Toolbutton", style="outline-toolbutton")
toolbutton3.pack(side=LEFT, padx=5, pady=10)

# Success outline toolbutton style
toolbutton4 = ttk.Checkbutton(root, text="Success Outline Toolbutton", style="success-outline-toolbutton")
toolbutton4.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
