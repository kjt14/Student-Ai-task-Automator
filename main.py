import gradio as gr
from search import search_and_extract_content
from summarizer import summarize_text
from presenter import generate_ppt

def automate_task(topic):
    try:
        raw_content = search_and_extract_content(topic)
        if not raw_content:
            return "❌ Failed to get content."

        summarized = summarize_text(raw_content)

        # Ensure at least 10 slides
        slides = summarized.split('\n')
        slides = [s.strip() for s in slides if s.strip()]
        while len(slides) < 10:
            slides.append("More details coming soon...")

        slides = slides[:10]  # Limit to 10

        generate_ppt(topic, slides)
        return f"✅ PPT created: {topic}.pptx"
    except Exception as e:
        return f"❌ Error: {e}"

gr.Interface(
    fn=automate_task,
    inputs="text",
    outputs="text",
    title="AI Task Automator - Generate PPT from Topic"
).launch()
