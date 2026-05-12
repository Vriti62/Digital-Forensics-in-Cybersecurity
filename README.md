# Project Title - Digital Forensics in Cybersecurity: Techniques for Effective Evidence Investigation

## Type
Research Project / Industry Oriented Hands On Experience (IOHE)

---

# Authors

- Anushka - 2210991322
- Drishti Bhardwaj - 2210990306 
- Geetanshu Mantro - 2210990324    
- Vriti Jaitley - 2210994862  

---

# Co-Author

## Dr. Shikha Tuteja  
Associate Professor  
Department of Computer Science and Engineering  
Chitkara University, Punjab

---

# Description

This project focuses on the role of Digital Forensics in modern Cybersecurity and how forensic techniques can be used to investigate cybercrimes effectively. With the rapid increase in cyberattacks such as phishing, malware infections, unauthorized access, and data breaches, organizations require efficient methods to identify, preserve, and analyze digital evidence.

The research combines practical forensic investigation methodologies with automation techniques to improve the efficiency and accuracy of cybercrime investigations. The project uses industry-standard tools such as Wireshark and Autopsy along with Python scripting to automate packet analysis and log processing.

A virtual environment was created using VMware to safely simulate attacks and generate realistic forensic evidence. The study demonstrates how automated workflows can significantly reduce manual effort while maintaining the integrity and authenticity of evidence.

---

# Features

## Digital Forensic Investigation Process

- Evidence Identification and Collection
- Evidence Preservation using Hashing
- Examination and Artifact Analysis
- Structured Reporting and Documentation

---

## Tools Used

### Network Forensics
- Wireshark
- Nmap
- Scapy (Python)

### Disk Forensics
- Autopsy

### Virtualization
- VMware Workstation

### Automation
- Python Scripts for:
  - Packet Analysis
  - Log Processing
  - Automated Summarization

---

## Key Functionalities

- Detection of suspicious SYN packet patterns
- Automated network traffic analysis
- Recovery of deleted files
- Extraction of browser history and system artifacts
- Shell Bag analysis
- Identification of encrypted/suspicious files
- Chronological reconstruction of user activities

---

# Methodology

The research follows a four-stage forensic investigation framework:

## 1. Experimental Environment
- VMware virtual lab setup
- Kali Linux used as attacker/forensic system
- Windows machine used as target system

## 2. Identification & Collection
- Capturing:
  - System logs
  - Network traffic (.pcapng)
  - Disk images

## 3. Preservation
- Use of cryptographic hashing
- Ensuring evidence remains unchanged and authentic

## 4. Examination & Analysis
- Artifact extraction
- Timeline reconstruction
- Network behavior analysis

## 5. Reporting
- Exporting findings into structured reports
- Documentation in HTML/Excel formats

---

# Project Structure

```bash
├── Documentation/
│   ├── AI_Plagiarism_Report.pdf.pdf/
│   ├── Abstract Digital Forensics in Cybersecurity.docx/
│   └── DigitalForensicsInCyberecurity_Report.docx/
│
├── Sourc-Code/
│   ├── Autopsy_Output.docx
│   ├── WIRESHARK_OUTPUT.docx
|   ├── analyze.py
│   └── wireshark.pcapng
│
└── README.md
```

---

# Installation

Make sure Python 3.8+ is installed.

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

# How to Run the Project

## Step 1 - Setup Virtual Environment
- Install VMware Workstation
- Configure:
  - Kali Linux VM
  - Windows VM

---

## Step 2 - Capture Network Traffic

Run Nmap scan:

```bash
nmap -sS <target-ip>
```

Capture packets using Wireshark.

---

## Step 3 - Analyze Network Packets

Run the Python automation script:

```bash
python analyze.py
```

The script:
- Reads `.pcapng` files
- Detects SYN packets
- Counts unique ports scanned
- Generates summaries automatically

---

## Step 4 - Perform Disk Forensics

Open disk image in Autopsy and enable ingest modules for:
- Deleted file recovery
- Web history extraction
- Shell Bag analysis
- Artifact categorization

---

# Recommended Platforms

- Jupyter Notebook
- Google Colab
- VS Code
- VMware Workstation

---

# Major Findings / Results

## Key Results

### Attack Detection
- Automated scripts detected:
  - 1000 SYN packets
  - 1000 unique targeted ports
- Confirmed reconnaissance/scanning attack behavior

---

### Artifact Recovery

Autopsy successfully extracted:
- Deleted files
- 4008 web history entries
- User activity traces
- Suspected encrypted files

---

### Investigation Integrity
- Cryptographic hashing maintained evidence authenticity throughout the investigation lifecycle.

---

# Comparative Tool Analysis

| Tool | Disk Analysis | Network Monitoring | Log Processing | Data Recovery |
|------|------|------|------|------|
| Autopsy | ✔ | ✖ | ✔ | ✔ |
| Wireshark | ✖ | ✔ | ✔ | ✖ |
| Python | ✔ | ✔ | ✔ | ✖ |

---

# Conclusion

This research demonstrates that combining structured forensic methodologies with automation significantly improves cybersecurity investigations. The integration of tools such as Autopsy, Wireshark, and Python enables investigators to process large datasets efficiently while preserving evidence integrity.

The project highlights the growing importance of digital forensics in incident response, cybercrime analysis, and legal investigations.

---

# Future Scope

## AI & Machine Learning Integration
- Intelligent threat prediction
- Automated anomaly detection
- Real-time attack classification

---

## Cloud & IoT Forensics
- Investigation of cloud infrastructures
- Smart device and IoT artifact analysis

---

## Scalable Digital Forensics
- Handling enterprise-scale forensic investigations
- Petabyte-scale evidence processing

---

# References

1. Casey, E. (2011). *Digital Evidence and Computer Crime*  
2. Al-Dhaqm, A. et al. (2020). *Digital Forensics: Challenges and Future Directions*  
3. Raghavan, S. (2013). *Digital Forensic Research: Current State of the Art*  
4. Taylor, M. et al. (2010). *Digital Evidence in Cloud Computing Systems*  
5. Adelstein, F. (2006). *Live Forensics: Diagnosing Your System Without Killing It First*

---

# Documents

The complete project report and research documentation are included in:

```bash
documents/
```

This includes:
- Methodology
- Experimental setup
- Tool implementation
- Findings and conclusions
- References and supporting material
