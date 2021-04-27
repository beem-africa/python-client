from setuptools import setup

setup(
    name="beem-africa",
    version="0.1.0",
    description="A Python library to easy the integration with the Beem Africa SMS Gateway",
    url="https://github.com/beem-africa/python-client",
    download_url="https://github.com/beem-africa/python-client/releases/tag/0.1",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["BeemAfrica"],
    keywords=[
        "beem-africa",
        "beem-sms-api",
        "python-beem",
        "beem africa  package",
        "beem-africa-python",
        "python-tanzania",
    ],
    install_requires=[
        'requests',
    ],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
