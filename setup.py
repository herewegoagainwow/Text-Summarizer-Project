import setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USERNAME = "herewegoagain"
SRC_REPO = "textSummarizer"
AUTHOR_EMIAL = "prakasharunav12@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMIAL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/herewegoagain/Text-Summarizer-Project",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)



