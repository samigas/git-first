{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a533e4b-342e-42c7-8851-3c2e64bbc37a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_integer(prompt):\n",
    "    res = int(input(prompt))\n",
    "    return res\n",
    "\n",
    "def exchange(price):\n",
    "    n500 = price//500\n",
    "    n100 = (price%500)//100\n",
    "    n50 = ((price%500)%100)//50\n",
    "    n10 = (((price%500)%100)%50)//10\n",
    "    print('500원 짜리는:', n500, '개', '100원 짜리는:', n100, '개', '50원 짜리는:', n50, '개', '10원짜리는:', n10, '개')\n",
    "\n",
    "pri = int(get_integer('동전으로 바꾸고 싶은 금액은?'))\n",
    "result= exchange(pri)\n",
    "print(result)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
