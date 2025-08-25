import hashlib, json, time

# Utility: hashing
def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Block class
class Block:
    def __init__(self, index, prev_hash, record, timestamp=None):
        self.index = index
        self.prev_hash = prev_hash
        self.record = record
        self.timestamp = timestamp or time.time()
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "prev_hash": self.prev_hash,
            "record": self.record,
            "timestamp": self.timestamp
        }, sort_keys=True)
        return sha256(block_string)

# Blockchain for Student Certificates
class CertificateBlockchain:
    def __init__(self, university_name):
        self.university_name = university_name
        self.chain = []
        self.create_genesis()

    def create_genesis(self):
        genesis = Block(0, "0", {"msg": f"Genesis Block - {self.university_name} Certificates"})
        self.chain.append(genesis)

    def add_certificate(self, student, course, grade):
        record = {
            "University": self.university_name,
            "Student": student,
            "Course": course,
            "Grade": grade
        }
        prev = self.chain[-1]
        new_block = Block(len(self.chain), prev.hash, record)
        self.chain.append(new_block)

    def get_certificates(self, student_name):
        certs = []
        for b in self.chain:
            if isinstance(b.record, dict) and b.record.get("Student") == student_name:
                certs.append(b.record)
        return certs


# ------------------------------
# DEMO with User Input
# ------------------------------
uni = input("Enter University Name: ")
cb = CertificateBlockchain(uni)

while True:
    print("\n1. Add Certificate")
    print("2. Show Student Certificates")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student = input("Student Name: ")
        course = input("Course Name: ")
        grade = input("Grade: ")
        cb.add_certificate(student, course, grade)
        print("✅ Certificate added successfully!")

    elif choice == "2":
        student = input("Enter Student Name to view certificates: ")
        certs = cb.get_certificates(student)
        print(f"\n🎓 Certificates of {student}:")
        for c in certs:
            print(c)

    elif choice == "3":
        print("Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice, try again.")
