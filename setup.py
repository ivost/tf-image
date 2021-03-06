from setuptools import setup, find_packages
import os

setup(
    name="tf_image",
    version="0.1.0",
    description="Image augmentation operations for TensorFlow 2+.",
    url="https://github.com/Ximilar-com/tf-image",
    author="Ximilar.com Team, Michal Lukac, Libor Vanek, ...",
    author_email="tech@ximilar.com",
    license="MIT",
    packages=find_packages(),
    keywords="machine learning, multimedia, image",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
    zip_safe=False,
    namespace_packages=["tf_image"],
)
