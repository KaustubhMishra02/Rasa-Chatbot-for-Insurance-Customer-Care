<p align="center"><img src="https://media.istockphoto.com/vectors/-vector-id1010001882?k=20&m=1010001882&s=612x612&w=0&h=6ZqzWlYBD3bT2EqJolzC3xbIKVVy350qMQmmS6B-Wd4=" width="10%"></p>
<h1 align="center">Customer Care Bot</h1>
<p align="center">Customer care bot for insurance company which can check claim status, file new claims and give users info about insurance policies.</p>

<p align="center">
  Python v3.8.13 ||
  Rasa v3.2.1
</p>

<p align="center">
  Repo size : 904 MB
</p>

## Setup
- Initialize a virtual environment via Conda:
```bash
conda create --name rasaenv 
```
- activate venv and install numpy and spaCy
```
conda activate rasaenv
conda config --rasaenv --add channels conda-forge
conda install numpy
conda install -c conda-forge spacy.
```
- Install spaCy model and navigate to directory
```bash
python -m spacy download en_core_web_md
cd /chatbot
```


##  Working
Chatbot model is already trained so we just need to run it
- Run rasa action server on separate terminal
```
rasa run actions
```
- Test bot on shell
```
rasa shell
```
OR
- start `rasa` server for GUI integration
```bash
rasa run --enable-api --cors="*"
```
Then open index.html and chat with bot in widget.

## Tutorial links:
- [Build customer care chatbot from scratch](https://youtu.be/u6xOgR3jEMU)
- [RASA Documentation](https://rasa.com/docs/rasa/)
