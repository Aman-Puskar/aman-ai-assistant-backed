def clean(docs):
    clean_text = '\n\n'.join(doc.page_content for doc in docs)
    return clean_text