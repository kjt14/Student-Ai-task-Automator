import wikipedia

def search_and_extract_content(topic):
    try:
        summary = wikipedia.summary(topic, sentences=7)
        return summary
    except Exception as e:
        return "Failed_to_get_summary: " + str(e)
