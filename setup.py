from setuptools import setup

setup(
    name="eet",
    version="0.1",
    py_modules=["eet"],
    install_requires=["Click"],
    entry_points="""
        [console_scripts]
        eet=eet:eet
    """,
)
