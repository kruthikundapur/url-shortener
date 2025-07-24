from setuptools import setup, find_packages

with open("CHANGES.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="url-shortener",
    version="0.1.0",
    author="Kruthi Kundapur D",  # Replace with your actual name
    author_email="kruthikundapur@gmail.com",  # Replace with your actual email
    description="A Python URL shortener service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kruthikundapur/url-shortener",
    packages=find_packages(include=["app", "app.*"]),
    install_requires=[
        "flask>=2.0.0",
        "validators>=0.18.0",
        "shortuuid>=1.0.0"
    ],
    extras_require={
        "mongodb": ["pymongo>=4.0.0"]
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "url-shortener=app.api:main"
        ]
    }
)