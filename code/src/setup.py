from setuptools import setup, find_packages
setup(
    name='iris-classifier',
    version='0.1',
    author='Ashish Pujari',
    author_email='apujari@northwestern.edu',
    description='A simple Iris classifier using Keras',
    long_description='A simple Iris classifier using Keras',
    long_description_content_type='text/markdown',
    url='https://github.com/linda-liang/iris-classifier',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'numpy',
        'scikit-learn',
        'tensorflow',
        'keras',
    ],
)






