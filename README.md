
📚 Text Summarizer to PowerPoint using OpenAI

This project uses the **OpenAI GPT API** to summarize long texts or documents and automatically generate a **PowerPoint presentation (PPT)** with the summary.

---
✨ Features

* 🔍 Summarizes large input texts using OpenAI's GPT models.
* 🖼️ Generates a PowerPoint file with:

  * Cover slide
  * Summary slide(s)
  * Bullet points per section
* 🧠 Uses `openai` API for high-quality NLP
* 📊 Built with `python-pptx`, `openai`, `dotenv`

---

### 📁 Project Structure

```
Student-Ai-task-Automator/
│
├── main.py                # Main Python script to summarize and create PPT
├── .env                   # API keys (OpenAI)
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

---

 ⚙️ Requirements

* Python 3.12
* `openai`
* `python-pptx`
* `python-dotenv`

---
 📦 Installation

1. Clone the repository:


git clone https://github.com/kjt14/Student-Ai-task-Automator.git
cd text-summarizer-to-ppt


2. Create and activate a virtual environment (optional but recommended):


python -m venv venv
venv\Scripts\activate  # On Windows


3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your OpenAI key:

```
OPENAI_API_KEY=your_api_key_here
```

---

 🚀 Usage

Run the script with your text:


python main.py


You will be prompted to:

* Paste your text or upload it via code
* The tool will generate `summary_presentation.pptx` in the project folder

---

 🧠 Example Output

**Input:**

> "The sun is a star that gives us light and heat. It is the center of our solar system..."

**Output PPT:**

* Slide 1: Title "AI Text Summary"
* Slide 2: "Summary" with 4–5 bullet points explaining the text.

---

 🛠 Tech Stack

* 🧠 OpenAI GPT-4 via API
* 📊 python-pptx for presentation generation
* 🧪 python-dotenv for secure API usage

---

 🧑‍💻 Author

**Khush Thakkar**
B.Tech CSE (4th Year) – Passionate about AI, automation, and building smart solutions.

---
📃 License

MIT License – Feel free to use and modify this project.

