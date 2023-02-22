def upload_article(path):
    file = open(path, "r", encoding="utf-8", errors="ignore")
    f = file.read()
    return f