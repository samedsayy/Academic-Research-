# File Encryption & Decryption Tool

This project implements a simple file encryption/decryption system using the
[Fernet](https://cryptography.io/en/latest/fernet/) symmetric key encryption
module from the `cryptography` Python library.

The program allows you to:

- Generate a new encryption key  
- Load an existing encryption key  
- Encrypt any file (text, images, PDFs, etc.)  
- Decrypt previously encrypted files  

---

## Requirements

This project uses Python 3.8+ and the `cryptography` library.

Install all dependencies with:

```bash
pip install -r requirements.txt

Run the main program:
python main.py
You will see this menu:
FILE ENCRYPTION TOOL
1. Generate a new key
2. Encrypt a file
3. Decrypt a file
4. Exit

Step-by-Step Instructions
1) Generate a Key (Run Once)
Before encrypting files, generate a key:
python main.py
# Choose option 1
This creates a file called:
key.key
This file must stay in the same folder as main.py for encryption and decryption.
2️) Encrypt a File
Make sure the file you want to encrypt (e.g., example.txt) is in the same folder or
provide a full path.
Run:
python main.py
# Choose option 2
Enter the file name to encrypt: example.txt
Your file will now be replaced with an encrypted version.
3️) Decrypt a File
To restore an encrypted file:
python main.py
# Choose option 3
Enter the encrypted filename:
Enter the file name to decrypt: example.txt
The file will be restored to its original contents.

Important Notes
Losing key.key means losing access to all encrypted files.
Do NOT upload your key publicly.
Encryption overwrites the original file — make backups if needed.
Only decrypt files that were encrypted using the same key.

Authors
Deniz Baran Coban, Abdulsamed Say, Leon Katava
