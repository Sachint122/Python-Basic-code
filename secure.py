import os
import ctypes
import tkinter as tk
from tkinter import messagebox, filedialog
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

class FolderLockerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Locker")
        self.root.geometry("400x200")

        self.folder_path = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(root, text="Folder Path:").pack(pady=5)
        self.path_entry = tk.Entry(root, textvariable=self.folder_path, width=50)
        self.path_entry.pack(pady=5)

        tk.Button(root, text="Browse", command=self.browse_folder).pack(pady=5)

        tk.Label(root, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(root, textvariable=self.password, show="*", width=50)
        self.password_entry.pack(pady=5)

        tk.Button(root, text="Lock Folder", command=self.lock_folder).pack(pady=5)
        tk.Button(root, text="Unlock Folder", command=self.unlock_folder).pack(pady=5)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def lock_folder(self):
        folder_path = self.folder_path.get()
        password = self.password.get()

        if not folder_path or not password:
            messagebox.showerror("Error", "Please provide a folder path and password")
            return

        # Encrypt the password
        encrypted_password = self.encrypt_password(password)

        # Save the encrypted password in a hidden file
        password_file = os.path.join(folder_path, ".lock")
        with open(password_file, "wb") as f:
            f.write(encrypted_password)

        # Hide the folder
        self.set_folder_attributes(folder_path, hide=True)

        messagebox.showinfo("Success", f"Folder '{folder_path}' is now locked")

    def unlock_folder(self):
        folder_path = self.folder_path.get()
        password = self.password.get()

        if not folder_path or not password:
            messagebox.showerror("Error", "Please provide a folder path and password")
            return

        # Check the encrypted password
        password_file = os.path.join(folder_path, ".lock")
        if not os.path.exists(password_file):
            messagebox.showerror("Error", "Folder is not locked")
            return

        with open(password_file, "rb") as f:
            encrypted_password = f.read()

        if not self.verify_password(password, encrypted_password):
            messagebox.showerror("Error", "Incorrect password")
            return

        # Unhide the folder
        self.set_folder_attributes(folder_path, hide=False)

        # Remove the password file
        os.remove(password_file)

        messagebox.showinfo("Success", f"Folder '{folder_path}' is now unlocked")

    def set_folder_attributes(self, folder_path, hide):
        FILE_ATTRIBUTE_HIDDEN = 0x02
        FILE_ATTRIBUTE_SYSTEM = 0x04

        attrs = ctypes.windll.kernel32.GetFileAttributesW(folder_path)
        if attrs == -1:
            messagebox.showerror("Error", "Failed to get folder attributes")
            return

        if hide:
            attrs |= FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM
        else:
            attrs &= ~FILE_ATTRIBUTE_HIDDEN
            attrs &= ~FILE_ATTRIBUTE_SYSTEM

        result = ctypes.windll.kernel32.SetFileAttributesW(folder_path, attrs)
        if not result:
            messagebox.showerror("Error", "Failed to change folder attributes")

    def encrypt_password(self, password):
        salt = get_random_bytes(16)
        key = PBKDF2(password, salt, dkLen=32, count=1000000)
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(b"password")
        return salt + cipher.nonce + tag + ciphertext

    def verify_password(self, password, encrypted_password):
        salt = encrypted_password[:16]
        nonce = encrypted_password[16:32]
        tag = encrypted_password[32:48]
        ciphertext = encrypted_password[48:]
        key = PBKDF2(password, salt, dkLen=32, count=1000000)
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        try:
            cipher.decrypt_and_verify(ciphertext, tag)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = FolderLockerApp(root)
    root.mainloop()
