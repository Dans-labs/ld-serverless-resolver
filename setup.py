from setuptools import setup

packages = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="ld_proxy",
    version="0.1.0",
    description="example api to be deployed to aws lambda",
    url="https://github.com/Dans-labs/ld-serverless-proxy",
    author="Slava Tykhonov",
    author_email="4tikhonov@gmail.com",
    license="MIT",
    include_package_data=True,
    install_requires=requirements,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
