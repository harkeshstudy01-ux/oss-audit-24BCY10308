\# CyberSafe Toolkit (Command Line Application)



\##  Project Description



CyberSafe Toolkit is a command-line based cybersecurity application developed using Python that combines multiple security tools into a single system.



The application allows users to:

\- Generate secure passwords

\- Check password strength

\- Store file hashes

\- Verify file integrity

\- Detect suspicious URLs (phishing detection)



This project demonstrates basic cybersecurity concepts such as password security, hashing, and threat detection using a simple CLI interface.



\---



\##  Objective



The objective of this project is to help users understand basic cybersecurity practices and improve awareness about digital security.



\---



\##  Technologies Used



\- Python 3

\- JSON (for storing file hashes)

\- Command Line Interface (CLI)

\- SHA-256 Hashing Algorithm



\---



\##  Project Structure



cybersafe-toolkit/



main.py → Main program (user interface)



password\_tool.py → Password generator and strength checker



integrity\_checker.py → File hashing and verification logic



url\_detector.py → Phishing URL detection



hashes.json → Stores file hashes



README.md → Project documentation



requirements.txt → Dependencies (empty)



\---



\##  Installation \& Setup



Follow the steps below to run this project on your system.



\### Step 1: Install Python



Download Python from:

https://www.python.org/downloads/



Install Python and make sure to check:

"Add Python to PATH"



\---



\### Step 2: Clone the Repository



Open Command Prompt and run:



git clone https://github.com/YOURUSERNAME/cybersafe-toolkit.git



\---



\### Step 3: Navigate to Project Folder



cd cybersafe-toolkit



\---



\### Step 4: Run the Program



python main.py



\---



\##  How to Use the Application



After running the program, you will see a menu:



CyberSafe Toolkit



1 Generate Password  

2 Check Password Strength  

3 Store File Hash  

4 Verify File  

5 Check URL  

6 Exit  



\---



\### ➤ Option 1: Generate Password



\- Enter desired password length

\- System generates a strong password



Example:

Length: 10  

Output: A9@kLp3#Qz  



\---



\### ➤ Option 2: Check Password Strength



\- Enter a password

\- Output will be:

&#x20; - Weak

&#x20; - Medium

&#x20; - Strong



Example:

Input: weak123  

Output: Weak  



\---



\### ➤ Option 3: Store File Hash



\- Enter file path (example: test.txt)

\- System stores original file hash



\---



\### ➤ Option 4: Verify File Integrity



\- Enter file path

\- System checks whether file is modified



Output:

SAFE → File unchanged  

MODIFIED → File changed  



\---



\### ➤ Option 5: Check URL



\- Enter a website URL

\- System checks if it is safe or suspicious



Example:

Input: http://login-bank.com  

Output: Suspicious  



\---



\### ➤ Option 6: Exit



Closes the program



\---



\## 💾 Data Storage



File hashes are stored in:



hashes.json



This file automatically updates when you store file hashes.



\---



\##  Example Run



Generate password:



Length: 8  

Output: Xy7@pQ2!  



Check URL:



Input: http://verify-account.com  

Output: Suspicious  



\---



\##  Features Summary



✔ Password generation  

✔ Password strength checking  

✔ File integrity verification  

✔ Phishing URL detection  

✔ JSON-based data storage  

✔ CLI-based application  



\---



\##  Ethical Note



This project is created for educational purposes only and should not be used for any malicious activities.



\---



\##  Author



HARKESH



\---



\##  Conclusion



This project demonstrates how basic cybersecurity techniques can be implemented using Python. It helps users understand important security concepts like password strength, file integrity, and phishing detection in a simple and practical way.

