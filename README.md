# Project Overview  

The WhatsApp Chat Analyzer is a Streamlit-based web application designed to help users analyze their exported WhatsApp chat data.


### Usefulness & Impact  
- The WhatsApp Chat Analyzer empowers users to gain a deeper understanding of their communication habits, helping identify trends, busiest users, and peak activity times.
-  It provides actionable insights that can be valuable for personal use, team collaboration, or organizational monitoring.
-  By visualizing chat data, users can optimize communication strategies, improve engagement, and make informed decisions based on historical chat behavior.
-  This tool is especially beneficial for group admins, community managers, and anyone looking to derive meaningful insights from their chat conversations.  


---
## Live Demo
[App Live At](https://whatsapp-chat-analyzer-nox54hxnakbbqteeoi8v6f.streamlit.app/)

### Key Instructions for Users:
- **Export Your WhatsApp Chat:** Export your (group / individual) chat from WhatsApp without media (ensure it's in .txt format).
- **Upload the File:** Use the "Browse Files" section to upload the exported .txt file.
- **Select Your Options:** Choose the desired analysis options(overall / specified user) from the dropdown menu.
- **Show Analysis:** Click on the "Show Analysis" button to generate insights and visualize your chat data.

## Installation  

Follow the steps below to set up the project on your local machine:  

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Aditi-Singh-15/whatsapp-chat-analyzer.git
   cd whatsapp-chat-analyzer
2. **Install the Required Dependencies:**
   ```bash
   pip install -r requirements.txt


## Run the Application

To run the application, use the following command:

```bash
streamlit run app.py 
```

---

## Features 
- **Group & Individual Chat Analysis**: Users can perform analysis for both group chats and one-on-one conversations. Insights can be obtained for overall chat activity as well as for specific members, providing a more granular understanding of communication patterns.  
- **Top Chat Statistics:** Gain valuable insights into your chat data by viewing total messages, words, and media shared, helping you understand the overall communication patterns.
- **Monthly and Daily Timeline:** Analyze message trends over time to identify patterns, peak activity periods, and understand how your communication evolves.
- **Activity Maps:** Visualize the busiest days and months, enabling you to pinpoint when and how often specific users interact, enhancing your understanding of chat engagement.
- **Heatmaps:** Dive deeper into activity distribution across days and time periods, offering a clear visual representation of communication trends, making it easier to spot patterns and busy periods.
- **Busiest Users Analysis:** Identify the most active users in group chats, helping you understand user engagement levels and focusing on key contributors to the conversation.
- **Common Words:** Discover the most frequently used words (excluding stop words), gaining deeper insights into the common themes and topics discussed in your chats.
---
## Technologies Used
- **Python:** The programming language used for developing the application.
- **Streamlit:** A framework for building interactive web applications with Python.
- **Pandas:** A powerful data manipulation library for handling and processing structured data.
- **Seaborn & Matplotlib:** Libraries for creating statistical graphics and visualizing data.
- **Regex:** A library used for string manipulation and pattern matching.
- **NumPy:** A library for numerical computations in Python.

---
