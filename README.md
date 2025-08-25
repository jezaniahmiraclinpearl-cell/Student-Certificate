Student-Certificate-Blockchain

A beginner-friendly blockchain implementation in Python for securely storing and verifying student certificates.
This project demonstrates how blockchain concepts can be applied in education, ensuring tamper-proof certificates, authenticity, and traceability.

🚀 Features

✅ Genesis block creation – the first block starts the certificate chain.

✅ Add certificates – store student name, course, and grade as secure records.

✅ Student-wise blockchain – each student’s certificates are linked in their chain.

✅ Verify authenticity – ensures certificates cannot be modified or faked.

✅ Trace education history – fetch all certificates of a student step by step.

✅ Interactive CLI menu – add new certificates and view student records easily.

✅ Beginner-friendly Python code – simple and clear blockchain example.

⚙ How It Works

A new blockchain starts with a Genesis block (first certificate entry).

Each new certificate (student + course + grade) is stored as a new block.

Blocks are linked using SHA-256 hashing, making them tamper-proof.

When a student earns a new certificate, it is added as another block.

Student’s full academic history can be securely traced and verified.

Blockchain integrity check ensures no certificate has been altered.

🔑 Concepts Used

🧱 Blockchain basics – blocks linked with previous hashes

🔒 SHA-256 hashing – protects data against tampering

✨ Immutability – certificates cannot be changed once stored

📜 Traceability – complete student record in chronological order

✅ Data validation – ensures certificate authenticity

▶️ Running the Project
# Clone the repository
git clone https://github.com/YourUsername/Student-Certificate-Blockchain.git

# Navigate into the project folder
cd Student-Certificate-Blockchain

# Run the blockchain program
python certificate_blockchain.py

📌 Example Demo
Enter University Name: ABC University  

1. Add Certificate  
2. Show Student Certificates  
3. Exit  

Student Name: Alice  
Course Name: B.Sc Computer Science  
Grade: A  
✅ Certificate added successfully!  

🎓 Certificates of Alice:  
{'University': 'ABC University', 'Student': 'Alice', 'Course': 'B.Sc Computer Science', 'Grade': 'A'}
