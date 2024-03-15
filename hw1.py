{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "05585bf0-5436-4242-85ae-db2e4a831abc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "시작\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "넓이를 구하고자 하는 원의 반지름은?  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "원의 넓이는: 12.56\n",
      "끝\n"
     ]
    }
   ],
   "source": [
    "def get_radius(prompt):\n",
    "    r = int(input(prompt))\n",
    "    return r\n",
    "\n",
    "def get_circle_area(radius):\n",
    "    area = 3.14 * radius * radius\n",
    "    return area\n",
    "\n",
    "print('시작')\n",
    "radius = get_radius('넓이를 구하고자 하는 원의 반지름은? ')\n",
    "result = get_circle_area(radius)\n",
    "print(\"원의 넓이는:\", result)\n",
    "print(\"끝\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83395efa-4753-4c41-ba71-f6a86eac520f",
   "metadata": {},
   "outputs": [],
   "source": []
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
