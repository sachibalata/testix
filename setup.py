from distutils.core import setup
setup(
    name = "testix",
    packages = ["testix", "examples", "examples.tests"],
    version = "0.3",
    description = "Mocking framework Python with *exact* Scenarios",
    author = "Yoav Kleinberger",
    author_email = "haarcuba@gmail.com",
    url = "https://github.com/haarcuba/testix",
    keywords = ["mock", "mocking", "unittest", "python", "unit testing"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        ]
)
