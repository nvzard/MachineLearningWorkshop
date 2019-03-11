{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import Libraries\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load Text For Training\n",
    "def load_text(filename):\n",
    "    with open(filename, encoding='utf-8') as f:\n",
    "        return f.read().lower()\n",
    "        \n",
    "data = load_text('data.txt')\n",
    "# data = load_text('english_speech_2.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Prepare Markov chain transition table\n",
    "def createTransitionTable(data, weight=4):\n",
    "    T = {}\n",
    "    for i in range(0, len(data)-weight):\n",
    "        substr = data[i : i+weight]\n",
    "        next_char = data[i+weight]\n",
    "        if T.get(substr) is None:\n",
    "            T[substr] = {}\n",
    "            T[substr][next_char] = 1\n",
    "        elif T[substr].get(next_char) is None:\n",
    "            T[substr][next_char] = 1\n",
    "        else:\n",
    "            T[substr][next_char] += 1\n",
    "    \n",
    "    return T\n",
    "        \n",
    "\n",
    "T = createTransitionTable(data)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [],
   "source": [
    "def changeTransitionTableToProb(T):\n",
    "    for kx in T.keys():\n",
    "        factor = (sum(T[kx].values()))\n",
    "        for val in T[kx].keys():\n",
    "            T[kx][val] = T[kx][val]/factor\n",
    "    return T\n",
    "        \n",
    "T = changeTransitionTableToProb(T)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write prediction function\n",
    "def predict(ctx, T):\n",
    "    if T.get(ctx) is None:\n",
    "        return \" \"\n",
    "    sample_array = list(T[ctx].keys())\n",
    "    sample_probab = list(T[ctx].values())\n",
    "    \n",
    "    return np.random.choice(sample_array, p=sample_probab)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sampling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 174,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "कौन बोला, कौन बोला\n",
      "अपना time आएगा ना\n",
      "तू नंगा ही तो आया है\n",
      "क्यूंकि हैरत नहीं है चाहत की\n",
      "अदालत ये है सीने \n"
     ]
    }
   ],
   "source": [
    "# Generate \n",
    "sentence = \"कौन \"\n",
    "# sentence = \"time\"\n",
    "# sentence = 'my d'\n",
    "for i in range(100):\n",
    "    char_returned = predict(sentence[-4:], T)\n",
    "    sentence += char_returned\n",
    "\n",
    "print(sentence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "32512"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Text To Speech\n",
    "from gtts import gTTS\n",
    "import os\n",
    "language = \"hi\"\n",
    "myobj = gTTS(text=sentence, lang=language, slow=False)\n",
    "myobj.save(\"ML_RAP.mp3\") \n",
    "\n",
    "os.system(\"mpg321 ML_RAP.mp3\") \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
