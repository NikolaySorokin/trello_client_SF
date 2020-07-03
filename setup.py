import setuptools


with open("README.md", "r") as fh:  
   long_description = fh.read()  
   setuptools.setup(  
   name="trello_client-basics-api-nikolaysorokin",
   version="0.0.1", author="Nikolay Sorokin",
   author_email="sorokinnikolay88@gmail.com",
   description="Простой клиент для Trello",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/NikolaySorokin/trello_client_SF",  # Адрес сайта вашего пакета, можно указать ссылку на репозиторий GitHub.
   packages=setuptools.find_packages(),
   classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
   python_requires='>=3.6',)  