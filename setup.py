from setuptools import setup, find_packages

setup(
    name="github_activity",  # Your package name
    version="0.1",  # Version of your package
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=[
        "requests",  # External dependency
        "rich",  # External dependency
    ],
    entry_points={
        "console_scripts": [
            "github-activity=github_activity.main:main",  # Command and entry point
        ],
    },
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="A CLI tool to fetch GitHub activity for a user.",  # Short description
    long_description=open(
        "README.md"
    ).read(),  # Read the long description from README.md
    long_description_content_type="text/markdown",  # Content type for the long description
    url="https://github.com/yourusername/github-activity",  # Replace with your project's URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change license if needed
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version requirement
)
