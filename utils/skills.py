skills = [
    "python",
    "java",
    "kotlin",
    "android",
    "flutter",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "sql",
    "mysql",
    "aws",
    "docker",
    "git",
    "react",
    "spring boot"
]
def extract_skills(text):

    found = []

    lower_text = text.lower()

    for skill in skills:

        if skill in lower_text:
            found.append(skill)

    return found