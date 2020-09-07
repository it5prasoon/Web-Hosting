{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "\n",
    "<a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>\n",
    "___\n",
    "# Logistic Regression with Python\n",
    "\n",
    "For this lecture we will be working with the [Titanic Data Set from Kaggle](https://www.kaggle.com/c/titanic). This is a very famous data set and very often is a student's first step in machine learning! \n",
    "\n",
    "We'll be trying to predict a classification- survival or deceased.\n",
    "Let's begin our understanding of implementing Logistic Regression in Python for classification.\n",
    "\n",
    "We'll use a \"semi-cleaned\" version of the titanic data set, if you use the data set hosted directly on Kaggle, you may need to do some additional cleaning not shown in this lecture notebook.\n",
    "\n",
    "## Import Libraries\n",
    "Let's import some libraries to get started!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline\n",
    "import warnings\n",
    "import pickle\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## The Data\n",
    "\n",
    "Let's start by reading in the titanic_train.csv file into a pandas dataframe."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "train = pd.read_csv('titanic_train.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>886</td>\n",
       "      <td>887</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Montvila, Rev. Juozas</td>\n",
       "      <td>male</td>\n",
       "      <td>27.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>211536</td>\n",
       "      <td>13.0000</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>887</td>\n",
       "      <td>888</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Graham, Miss. Margaret Edith</td>\n",
       "      <td>female</td>\n",
       "      <td>19.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>112053</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>B42</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>888</td>\n",
       "      <td>889</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Johnston, Miss. Catherine Helen \"Carrie\"</td>\n",
       "      <td>female</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>W./C. 6607</td>\n",
       "      <td>23.4500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>889</td>\n",
       "      <td>890</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Behr, Mr. Karl Howell</td>\n",
       "      <td>male</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>111369</td>\n",
       "      <td>30.0000</td>\n",
       "      <td>C148</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>890</td>\n",
       "      <td>891</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Dooley, Mr. Patrick</td>\n",
       "      <td>male</td>\n",
       "      <td>32.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>370376</td>\n",
       "      <td>7.7500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Q</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>891 rows × 12 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     PassengerId  Survived  Pclass  \\\n",
       "0              1         0       3   \n",
       "1              2         1       1   \n",
       "2              3         1       3   \n",
       "3              4         1       1   \n",
       "4              5         0       3   \n",
       "..           ...       ...     ...   \n",
       "886          887         0       2   \n",
       "887          888         1       1   \n",
       "888          889         0       3   \n",
       "889          890         1       1   \n",
       "890          891         0       3   \n",
       "\n",
       "                                                  Name     Sex   Age  SibSp  \\\n",
       "0                              Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1    Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                               Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                             Allen, Mr. William Henry    male  35.0      0   \n",
       "..                                                 ...     ...   ...    ...   \n",
       "886                              Montvila, Rev. Juozas    male  27.0      0   \n",
       "887                       Graham, Miss. Margaret Edith  female  19.0      0   \n",
       "888           Johnston, Miss. Catherine Helen \"Carrie\"  female   NaN      1   \n",
       "889                              Behr, Mr. Karl Howell    male  26.0      0   \n",
       "890                                Dooley, Mr. Patrick    male  32.0      0   \n",
       "\n",
       "     Parch            Ticket     Fare Cabin Embarked  \n",
       "0        0         A/5 21171   7.2500   NaN        S  \n",
       "1        0          PC 17599  71.2833   C85        C  \n",
       "2        0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3        0            113803  53.1000  C123        S  \n",
       "4        0            373450   8.0500   NaN        S  \n",
       "..     ...               ...      ...   ...      ...  \n",
       "886      0            211536  13.0000   NaN        S  \n",
       "887      0            112053  30.0000   B42        S  \n",
       "888      2        W./C. 6607  23.4500   NaN        S  \n",
       "889      0            111369  30.0000  C148        C  \n",
       "890      0            370376   7.7500   NaN        Q  \n",
       "\n",
       "[891 rows x 12 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Exploratory Data Analysis\n",
    "\n",
    "Let's begin some exploratory data analysis! We'll start by checking out missing data!\n",
    "\n",
    "## Missing Data\n",
    "\n",
    "We can use seaborn to create a simple heatmap to see where we are missing data!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929ef6ee08>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Roughly 20 percent of the Age data is missing. The proportion of Age missing is likely small enough for reasonable replacement with some form of imputation. Looking at the Cabin column, it looks like we are just missing too much of that data to do something useful with at a basic level. We'll probably drop this later, or change it to another feature like \"Cabin Known: 1 or 0\"\n",
    "\n",
    "Let's continue on by visualizing some more of the data! Check out the video for full explanations over these plots, this code is just to serve as reference."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929f306f88>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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9uzRmjVr1N/fryeeeEK1tbWqra3ViRMnJEmvvPKK5syZoyVLlnBbbww7IgCj+f1+bdq0SUePHlUwGNT999+v/fv3J31+X1+f/vrXv2rJkiW69dZb9cEHH2hgYEAdHR26++67E8+rrq7Wrl27JEk7d+7UvHnztHnzZt11111qaWnRH/7wB61atUr9/f166aWX9MYbb2jjxo26ePGi668ZuBKng2C0kydPyufzqbGxUZL0t7/9TY899pjGjx+feM6VF9VPnDhRY8aMkSTNmzdPO3fuVF9fn372s59ddRO+X/ziF5o/f77mzp2rSCSiqVOn6pNPPtH777+vPXv2SJLOnTunf/zjH5oyZUpim9OmTXP9NQNX4kgARjtx4oRWrVqlWCwmSSouLlZubq7y8/PV19cnSfroo48Sz8/K+u+3zI9//GOFw2Ft375d1dXVV23X5/PpjjvuUGNjox588EFJUklJiRYuXKiWlhb96U9/0qxZszRp0iR9+umnunDhguLxuMLhsNsvGbgKRwIw2n333afu7m7NnTtX48aNk+M4euqpp/S9731Pv//97/WDH/xAEyZMuOa6lmWpqqpKhw8fVlFR0Te+PnfuXD366KOJG/Q9/vjjWr58ud544w1FIhEtXbpUfr9fv/71r1VTUyO/389f08Kw4wZyAGAwTgcBgMGIAAAYjAgAgMGIAAAYjAgAgMGIAAAYjAgAgMH+HyzUXR1Gpq8rAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set_style('whitegrid')\n",
    "sns.countplot(x='Survived',data=train,palette='RdBu_r')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929f383f88>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set_style('whitegrid')\n",
    "sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929f417208>"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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AICJUQIAYGKUAACYGCUAACZGCcD0Xn75ZU2fPl1FRUWaOXNmj26j8cwzz6ixsfGKP//zn/9ctbW1V/x5oLu4TgCm9umnn+rtt9/W66+/LsMw5HQ6tWDBAu3YseOKlrdw4cIgJwRCi5EATC0xMVGNjY3avHmzjh8/royMDG3evFl2u12fffaZJOn1119XZWWlGhoalJeXJ7vdrnXr1ulHP/qRvr7MZunSpdq5c6f/cw8++KAaGhokSW+++aaWLVum5uZmzZkzR3a7XXa7XR9//LEk6dVXX9X999+vRx55hNt6I+woAZhaYmKi1qxZo/fff1+FhYXKzc3V7t27O5z/xIkT+vWvf61HHnlEN998s/7+97+rtbVVdXV1uvvuu/3z5efna/v27ZKkbdu2adKkSVq7dq1uv/12rV+/XqWlpVqyZImam5v1yiuvaNOmTaqqqlJbW1vIf2fgm9gdBFM7evSo4uPjVVZWJkn65z//qUcffVRJSUn+eb55UX1KSor69esnSZo0aZK2bdumEydO6J577rnoJnw/+clPNGXKFBUUFKilpUU33XSTPvnkE+3fv19vvvmmJOncuXP6/PPPdcMNN/iXOWrUqJD/zsA3MRKAqX388cdasmSJ3G63JCk9PV02m00JCQk6ceKEJOnDDz/0zx8V9b//Ze644w45nU5t2bJF+fn5Fy03Pj5eI0eOVFlZmR588EFJ0rBhwzR9+nStX79ev/rVr5SXl6ehQ4fq008/1YULF+TxeOR0OkP9KwMXYSQAU5swYYI+++wzFRQUaMCAAfL5fJo/f75iYmL0y1/+Utddd50GDx582c8ahqGcnBy99957SktLu+T9goICPfzww/4b9D322GNauHChNm3apJaWFs2ePVuJiYn62c9+psmTJysxMZGnaSHsuIEcAJgYu4MAwMQoAQAwMUoAAEyMEgAAE6MEAMDEKAEAMDFKAABM7P8A4+wUgz56OVYAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.set_style('whitegrid')\n",
    "sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929f417b48>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(train['Age'].dropna(),kde=False,color='darkred',bins=30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929f56a7c8>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "train['Age'].hist(bins=30,color='darkred',alpha=0.7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929f577c08>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='SibSp',data=train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929f67cf48>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "train['Fare'].hist(color='green',bins=40,figsize=(8,4))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "____\n",
    "### Cufflinks for plots\n",
    "___\n",
    " Let's take a quick moment to show an example of cufflinks!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-latest.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import cufflinks as cf\n",
    "cf.go_offline()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "linkText": "Export to plot.ly",
        "plotlyServerURL": "https://plot.ly",
        "showLink": true
       },
       "data": [
        {
         "histfunc": "count",
         "histnorm": "",
         "marker": {
          "color": "rgba(0, 128, 0, 1.0)",
          "line": {
           "color": "#4D5663",
           "width": 1.3
          }
         },
         "name": "Fare",
         "nbinsx": 30,
         "opacity": 0.8,
         "orientation": "v",
         "type": "histogram",
         "x": [
          7.25,
          71.2833,
          7.925,
          53.1,
          8.05,
          8.4583,
          51.8625,
          21.075,
          11.1333,
          30.0708,
          16.7,
          26.55,
          8.05,
          31.275,
          7.8542,
          16,
          29.125,
          13,
          18,
          7.225,
          26,
          13,
          8.0292,
          35.5,
          21.075,
          31.3875,
          7.225,
          263,
          7.8792,
          7.8958,
          27.7208,
          146.5208,
          7.75,
          10.5,
          82.1708,
          52,
          7.2292,
          8.05,
          18,
          11.2417,
          9.475,
          21,
          7.8958,
          41.5792,
          7.8792,
          8.05,
          15.5,
          7.75,
          21.6792,
          17.8,
          39.6875,
          7.8,
          76.7292,
          26,
          61.9792,
          35.5,
          10.5,
          7.2292,
          27.75,
          46.9,
          7.2292,
          80,
          83.475,
          27.9,
          27.7208,
          15.2458,
          10.5,
          8.1583,
          7.925,
          8.6625,
          10.5,
          46.9,
          73.5,
          14.4542,
          56.4958,
          7.65,
          7.8958,
          8.05,
          29,
          12.475,
          9,
          9.5,
          7.7875,
          47.1,
          10.5,
          15.85,
          34.375,
          8.05,
          263,
          8.05,
          8.05,
          7.8542,
          61.175,
          20.575,
          7.25,
          8.05,
          34.6542,
          63.3583,
          23,
          26,
          7.8958,
          7.8958,
          77.2875,
          8.6542,
          7.925,
          7.8958,
          7.65,
          7.775,
          7.8958,
          24.15,
          52,
          14.4542,
          8.05,
          9.825,
          14.4583,
          7.925,
          7.75,
          21,
          247.5208,
          31.275,
          73.5,
          8.05,
          30.0708,
          13,
          77.2875,
          11.2417,
          7.75,
          7.1417,
          22.3583,
          6.975,
          7.8958,
          7.05,
          14.5,
          26,
          13,
          15.0458,
          26.2833,
          53.1,
          9.2167,
          79.2,
          15.2458,
          7.75,
          15.85,
          6.75,
          11.5,
          36.75,
          7.7958,
          34.375,
          26,
          13,
          12.525,
          66.6,
          8.05,
          14.5,
          7.3125,
          61.3792,
          7.7333,
          8.05,
          8.6625,
          69.55,
          16.1,
          15.75,
          7.775,
          8.6625,
          39.6875,
          20.525,
          55,
          27.9,
          25.925,
          56.4958,
          33.5,
          29.125,
          11.1333,
          7.925,
          30.6958,
          7.8542,
          25.4667,
          28.7125,
          13,
          0,
          69.55,
          15.05,
          31.3875,
          39,
          22.025,
          50,
          15.5,
          26.55,
          15.5,
          7.8958,
          13,
          13,
          7.8542,
          26,
          27.7208,
          146.5208,
          7.75,
          8.4042,
          7.75,
          13,
          9.5,
          69.55,
          6.4958,
          7.225,
          8.05,
          10.4625,
          15.85,
          18.7875,
          7.75,
          31,
          7.05,
          21,
          7.25,
          13,
          7.75,
          113.275,
          7.925,
          27,
          76.2917,
          10.5,
          8.05,
          13,
          8.05,
          7.8958,
          90,
          9.35,
          10.5,
          7.25,
          13,
          25.4667,
          83.475,
          7.775,
          13.5,
          31.3875,
          10.5,
          7.55,
          26,
          26.25,
          10.5,
          12.275,
          14.4542,
          15.5,
          10.5,
          7.125,
          7.225,
          90,
          7.775,
          14.5,
          52.5542,
          26,
          7.25,
          10.4625,
          26.55,
          16.1,
          20.2125,
          15.2458,
          79.2,
          86.5,
          512.3292,
          26,
          7.75,
          31.3875,
          79.65,
          0,
          7.75,
          10.5,
          39.6875,
          7.775,
          153.4625,
          135.6333,
          31,
          0,
          19.5,
          29.7,
          7.75,
          77.9583,
          7.75,
          0,
          29.125,
          20.25,
          7.75,
          7.8542,
          9.5,
          8.05,
          26,
          8.6625,
          9.5,
          7.8958,
          13,
          7.75,
          78.85,
          91.0792,
          12.875,
          8.85,
          7.8958,
          27.7208,
          7.2292,
          151.55,
          30.5,
          247.5208,
          7.75,
          23.25,
          0,
          12.35,
          8.05,
          151.55,
          110.8833,
          108.9,
          24,
          56.9292,
          83.1583,
          262.375,
          26,
          7.8958,
          26.25,
          7.8542,
          26,
          14,
          164.8667,
          134.5,
          7.25,
          7.8958,
          12.35,
          29,
          69.55,
          135.6333,
          6.2375,
          13,
          20.525,
          57.9792,
          23.25,
          28.5,
          153.4625,
          18,
          133.65,
          7.8958,
          66.6,
          134.5,
          8.05,
          35.5,
          26,
          263,
          13,
          13,
          13,
          13,
          13,
          16.1,
          15.9,
          8.6625,
          9.225,
          35,
          7.2292,
          17.8,
          7.225,
          9.5,
          55,
          13,
          7.8792,
          7.8792,
          27.9,
          27.7208,
          14.4542,
          7.05,
          15.5,
          7.25,
          75.25,
          7.2292,
          7.75,
          69.3,
          55.4417,
          6.4958,
          8.05,
          135.6333,
          21.075,
          82.1708,
          7.25,
          211.5,
          4.0125,
          7.775,
          227.525,
          15.7417,
          7.925,
          52,
          7.8958,
          73.5,
          46.9,
          13,
          7.7292,
          12,
          120,
          7.7958,
          7.925,
          113.275,
          16.7,
          7.7958,
          7.8542,
          26,
          10.5,
          12.65,
          7.925,
          8.05,
          9.825,
          15.85,
          8.6625,
          21,
          7.75,
          18.75,
          7.775,
          25.4667,
          7.8958,
          6.8583,
          90,
          0,
          7.925,
          8.05,
          32.5,
          13,
          13,
          24.15,
          7.8958,
          7.7333,
          7.875,
          14.4,
          20.2125,
          7.25,
          26,
          26,
          7.75,
          8.05,
          26.55,
          16.1,
          26,
          7.125,
          55.9,
          120,
          34.375,
          18.75,
          263,
          10.5,
          26.25,
          9.5,
          7.775,
          13,
          8.1125,
          81.8583,
          19.5,
          26.55,
          19.2583,
          30.5,
          27.75,
          19.9667,
          27.75,
          89.1042,
          8.05,
          7.8958,
          26.55,
          51.8625,
          10.5,
          7.75,
          26.55,
          8.05,
          38.5,
          13,
          8.05,
          7.05,
          0,
          26.55,
          7.725,
          19.2583,
          7.25,
          8.6625,
          27.75,
          13.7917,
          9.8375,
          52,
          21,
          7.0458,
          7.5208,
          12.2875,
          46.9,
          0,
          8.05,
          9.5875,
          91.0792,
          25.4667,
          90,
          29.7,
          8.05,
          15.9,
          19.9667,
          7.25,
          30.5,
          49.5042,
          8.05,
          14.4583,
          78.2667,
          15.1,
          151.55,
          7.7958,
          8.6625,
          7.75,
          7.6292,
          9.5875,
          86.5,
          108.9,
          26,
          26.55,
          22.525,
          56.4958,
          7.75,
          8.05,
          26.2875,
          59.4,
          7.4958,
          34.0208,
          10.5,
          24.15,
          26,
          7.8958,
          93.5,
          7.8958,
          7.225,
          57.9792,
          7.2292,
          7.75,
          10.5,
          221.7792,
          7.925,
          11.5,
          26,
          7.2292,
          7.2292,
          22.3583,
          8.6625,
          26.25,
          26.55,
          106.425,
          14.5,
          49.5,
          71,
          31.275,
          31.275,
          26,
          106.425,
          26,
          26,
          13.8625,
          20.525,
          36.75,
          110.8833,
          26,
          7.8292,
          7.225,
          7.775,
          26.55,
          39.6,
          227.525,
          79.65,
          17.4,
          7.75,
          7.8958,
          13.5,
          8.05,
          8.05,
          24.15,
          7.8958,
          21.075,
          7.2292,
          7.8542,
          10.5,
          51.4792,
          26.3875,
          7.75,
          8.05,
          14.5,
          13,
          55.9,
          14.4583,
          7.925,
          30,
          110.8833,
          26,
          40.125,
          8.7125,
          79.65,
          15,
          79.2,
          8.05,
          8.05,
          7.125,
          78.2667,
          7.25,
          7.75,
          26,
          24.15,
          33,
          0,
          7.225,
          56.9292,
          27,
          7.8958,
          42.4,
          8.05,
          26.55,
          15.55,
          7.8958,
          30.5,
          41.5792,
          153.4625,
          31.275,
          7.05,
          15.5,
          7.75,
          8.05,
          65,
          14.4,
          16.1,
          39,
          10.5,
          14.4542,
          52.5542,
          15.7417,
          7.8542,
          16.1,
          32.3208,
          12.35,
          77.9583,
          7.8958,
          7.7333,
          30,
          7.0542,
          30.5,
          0,
          27.9,
          13,
          7.925,
          26.25,
          39.6875,
          16.1,
          7.8542,
          69.3,
          27.9,
          56.4958,
          19.2583,
          76.7292,
          7.8958,
          35.5,
          7.55,
          7.55,
          7.8958,
          23,
          8.4333,
          7.8292,
          6.75,
          73.5,
          7.8958,
          15.5,
          13,
          113.275,
          133.65,
          7.225,
          25.5875,
          7.4958,
          7.925,
          73.5,
          13,
          7.775,
          8.05,
          52,
          39,
          52,
          10.5,
          13,
          0,
          7.775,
          8.05,
          9.8417,
          46.9,
          512.3292,
          8.1375,
          76.7292,
          9.225,
          46.9,
          39,
          41.5792,
          39.6875,
          10.1708,
          7.7958,
          211.3375,
          57,
          13.4167,
          56.4958,
          7.225,
          26.55,
          13.5,
          8.05,
          7.7333,
          110.8833,
          7.65,
          227.525,
          26.2875,
          14.4542,
          7.7417,
          7.8542,
          26,
          13.5,
          26.2875,
          151.55,
          15.2458,
          49.5042,
          26.55,
          52,
          9.4833,
          13,
          7.65,
          227.525,
          10.5,
          15.5,
          7.775,
          33,
          7.0542,
          13,
          13,
          53.1,
          8.6625,
          21,
          7.7375,
          26,
          7.925,
          211.3375,
          18.7875,
          0,
          13,
          13,
          16.1,
          34.375,
          512.3292,
          7.8958,
          7.8958,
          30,
          78.85,
          262.375,
          16.1,
          7.925,
          71,
          20.25,
          13,
          53.1,
          7.75,
          23,
          12.475,
          9.5,
          7.8958,
          65,
          14.5,
          7.7958,
          11.5,
          8.05,
          86.5,
          14.5,
          7.125,
          7.2292,
          120,
          7.775,
          77.9583,
          39.6,
          7.75,
          24.15,
          8.3625,
          9.5,
          7.8542,
          10.5,
          7.225,
          23,
          7.75,
          7.75,
          12.475,
          7.7375,
          211.3375,
          7.2292,
          57,
          30,
          23.45,
          7.05,
          7.25,
          7.4958,
          29.125,
          20.575,
          79.2,
          7.75,
          26,
          69.55,
          30.6958,
          7.8958,
          13,
          25.9292,
          8.6833,
          7.2292,
          24.15,
          13,
          26.25,
          120,
          8.5167,
          6.975,
          7.775,
          0,
          7.775,
          13,
          53.1,
          7.8875,
          24.15,
          10.5,
          31.275,
          8.05,
          0,
          7.925,
          37.0042,
          6.45,
          27.9,
          93.5,
          8.6625,
          0,
          12.475,
          39.6875,
          6.95,
          56.4958,
          37.0042,
          7.75,
          80,
          14.4542,
          18.75,
          7.2292,
          7.8542,
          8.3,
          83.1583,
          8.6625,
          8.05,
          56.4958,
          29.7,
          7.925,
          10.5,
          31,
          6.4375,
          8.6625,
          7.55,
          69.55,
          7.8958,
          33,
          89.1042,
          31.275,
          7.775,
          15.2458,
          39.4,
          26,
          9.35,
          164.8667,
          26.55,
          19.2583,
          7.2292,
          14.1083,
          11.5,
          25.9292,
          69.55,
          13,
          13,
          13.8583,
          50.4958,
          9.5,
          11.1333,
          7.8958,
          52.5542,
          5,
          9,
          24,
          7.225,
          9.8458,
          7.8958,
          7.8958,
          83.1583,
          26,
          7.8958,
          10.5167,
          10.5,
          7.05,
          29.125,
          13,
          30,
          23.45,
          30,
          7.75
         ]
        }
       ],
       "layout": {
        "barmode": "overlay",
        "legend": {
         "bgcolor": "#F5F6F9",
         "font": {
          "color": "#4D5663"
         }
        },
        "paper_bgcolor": "#F5F6F9",
        "plot_bgcolor": "#F5F6F9",
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "font": {
          "color": "#4D5663"
         }
        },
        "xaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": ""
         },
         "zerolinecolor": "#E1E5ED"
        },
        "yaxis": {
         "gridcolor": "#E1E5ED",
         "showgrid": true,
         "tickfont": {
          "color": "#4D5663"
         },
         "title": {
          "font": {
           "color": "#4D5663"
          },
          "text": ""
         },
         "zerolinecolor": "#E1E5ED"
        }
       }
      },
      "text/html": [
       "<div>\n",
       "        \n",
       "        \n",
       "            <div id=\"86154ff0-7674-423a-82ef-9ffa8e9a84fc\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>\n",
       "            <script type=\"text/javascript\">\n",
       "                require([\"plotly\"], function(Plotly) {\n",
       "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    window.PLOTLYENV.BASE_URL='https://plot.ly';\n",
       "                    \n",
       "                if (document.getElementById(\"86154ff0-7674-423a-82ef-9ffa8e9a84fc\")) {\n",
       "                    Plotly.newPlot(\n",
       "                        '86154ff0-7674-423a-82ef-9ffa8e9a84fc',\n",
       "                        [{\"histfunc\": \"count\", \"histnorm\": \"\", \"marker\": {\"color\": \"rgba(0, 128, 0, 1.0)\", \"line\": {\"color\": \"#4D5663\", \"width\": 1.3}}, \"name\": \"Fare\", \"nbinsx\": 30, \"opacity\": 0.8, \"orientation\": \"v\", \"type\": \"histogram\", \"x\": [7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51.8625, 21.075, 11.1333, 30.0708, 16.7, 26.55, 8.05, 31.275, 7.8542, 16.0, 29.125, 13.0, 18.0, 7.225, 26.0, 13.0, 8.0292, 35.5, 21.075, 31.3875, 7.225, 263.0, 7.8792, 7.8958, 27.7208, 146.5208, 7.75, 10.5, 82.1708, 52.0, 7.2292, 8.05, 18.0, 11.2417, 9.475, 21.0, 7.8958, 41.5792, 7.8792, 8.05, 15.5, 7.75, 21.6792, 17.8, 39.6875, 7.8, 76.7292, 26.0, 61.9792, 35.5, 10.5, 7.2292, 27.75, 46.9, 7.2292, 80.0, 83.475, 27.9, 27.7208, 15.2458, 10.5, 8.1583, 7.925, 8.6625, 10.5, 46.9, 73.5, 14.4542, 56.4958, 7.65, 7.8958, 8.05, 29.0, 12.475, 9.0, 9.5, 7.7875, 47.1, 10.5, 15.85, 34.375, 8.05, 263.0, 8.05, 8.05, 7.8542, 61.175, 20.575, 7.25, 8.05, 34.6542, 63.3583, 23.0, 26.0, 7.8958, 7.8958, 77.2875, 8.6542, 7.925, 7.8958, 7.65, 7.775, 7.8958, 24.15, 52.0, 14.4542, 8.05, 9.825, 14.4583, 7.925, 7.75, 21.0, 247.5208, 31.275, 73.5, 8.05, 30.0708, 13.0, 77.2875, 11.2417, 7.75, 7.1417, 22.3583, 6.975, 7.8958, 7.05, 14.5, 26.0, 13.0, 15.0458, 26.2833, 53.1, 9.2167, 79.2, 15.2458, 7.75, 15.85, 6.75, 11.5, 36.75, 7.7958, 34.375, 26.0, 13.0, 12.525, 66.6, 8.05, 14.5, 7.3125, 61.3792, 7.7333, 8.05, 8.6625, 69.55, 16.1, 15.75, 7.775, 8.6625, 39.6875, 20.525, 55.0, 27.9, 25.925, 56.4958, 33.5, 29.125, 11.1333, 7.925, 30.6958, 7.8542, 25.4667, 28.7125, 13.0, 0.0, 69.55, 15.05, 31.3875, 39.0, 22.025, 50.0, 15.5, 26.55, 15.5, 7.8958, 13.0, 13.0, 7.8542, 26.0, 27.7208, 146.5208, 7.75, 8.4042, 7.75, 13.0, 9.5, 69.55, 6.4958, 7.225, 8.05, 10.4625, 15.85, 18.7875, 7.75, 31.0, 7.05, 21.0, 7.25, 13.0, 7.75, 113.275, 7.925, 27.0, 76.2917, 10.5, 8.05, 13.0, 8.05, 7.8958, 90.0, 9.35, 10.5, 7.25, 13.0, 25.4667, 83.475, 7.775, 13.5, 31.3875, 10.5, 7.55, 26.0, 26.25, 10.5, 12.275, 14.4542, 15.5, 10.5, 7.125, 7.225, 90.0, 7.775, 14.5, 52.5542, 26.0, 7.25, 10.4625, 26.55, 16.1, 20.2125, 15.2458, 79.2, 86.5, 512.3292, 26.0, 7.75, 31.3875, 79.65, 0.0, 7.75, 10.5, 39.6875, 7.775, 153.4625, 135.6333, 31.0, 0.0, 19.5, 29.7, 7.75, 77.9583, 7.75, 0.0, 29.125, 20.25, 7.75, 7.8542, 9.5, 8.05, 26.0, 8.6625, 9.5, 7.8958, 13.0, 7.75, 78.85, 91.0792, 12.875, 8.85, 7.8958, 27.7208, 7.2292, 151.55, 30.5, 247.5208, 7.75, 23.25, 0.0, 12.35, 8.05, 151.55, 110.8833, 108.9, 24.0, 56.9292, 83.1583, 262.375, 26.0, 7.8958, 26.25, 7.8542, 26.0, 14.0, 164.8667, 134.5, 7.25, 7.8958, 12.35, 29.0, 69.55, 135.6333, 6.2375, 13.0, 20.525, 57.9792, 23.25, 28.5, 153.4625, 18.0, 133.65, 7.8958, 66.6, 134.5, 8.05, 35.5, 26.0, 263.0, 13.0, 13.0, 13.0, 13.0, 13.0, 16.1, 15.9, 8.6625, 9.225, 35.0, 7.2292, 17.8, 7.225, 9.5, 55.0, 13.0, 7.8792, 7.8792, 27.9, 27.7208, 14.4542, 7.05, 15.5, 7.25, 75.25, 7.2292, 7.75, 69.3, 55.4417, 6.4958, 8.05, 135.6333, 21.075, 82.1708, 7.25, 211.5, 4.0125, 7.775, 227.525, 15.7417, 7.925, 52.0, 7.8958, 73.5, 46.9, 13.0, 7.7292, 12.0, 120.0, 7.7958, 7.925, 113.275, 16.7, 7.7958, 7.8542, 26.0, 10.5, 12.65, 7.925, 8.05, 9.825, 15.85, 8.6625, 21.0, 7.75, 18.75, 7.775, 25.4667, 7.8958, 6.8583, 90.0, 0.0, 7.925, 8.05, 32.5, 13.0, 13.0, 24.15, 7.8958, 7.7333, 7.875, 14.4, 20.2125, 7.25, 26.0, 26.0, 7.75, 8.05, 26.55, 16.1, 26.0, 7.125, 55.9, 120.0, 34.375, 18.75, 263.0, 10.5, 26.25, 9.5, 7.775, 13.0, 8.1125, 81.8583, 19.5, 26.55, 19.2583, 30.5, 27.75, 19.9667, 27.75, 89.1042, 8.05, 7.8958, 26.55, 51.8625, 10.5, 7.75, 26.55, 8.05, 38.5, 13.0, 8.05, 7.05, 0.0, 26.55, 7.725, 19.2583, 7.25, 8.6625, 27.75, 13.7917, 9.8375, 52.0, 21.0, 7.0458, 7.5208, 12.2875, 46.9, 0.0, 8.05, 9.5875, 91.0792, 25.4667, 90.0, 29.7, 8.05, 15.9, 19.9667, 7.25, 30.5, 49.5042, 8.05, 14.4583, 78.2667, 15.1, 151.55, 7.7958, 8.6625, 7.75, 7.6292, 9.5875, 86.5, 108.9, 26.0, 26.55, 22.525, 56.4958, 7.75, 8.05, 26.2875, 59.4, 7.4958, 34.0208, 10.5, 24.15, 26.0, 7.8958, 93.5, 7.8958, 7.225, 57.9792, 7.2292, 7.75, 10.5, 221.7792, 7.925, 11.5, 26.0, 7.2292, 7.2292, 22.3583, 8.6625, 26.25, 26.55, 106.425, 14.5, 49.5, 71.0, 31.275, 31.275, 26.0, 106.425, 26.0, 26.0, 13.8625, 20.525, 36.75, 110.8833, 26.0, 7.8292, 7.225, 7.775, 26.55, 39.6, 227.525, 79.65, 17.4, 7.75, 7.8958, 13.5, 8.05, 8.05, 24.15, 7.8958, 21.075, 7.2292, 7.8542, 10.5, 51.4792, 26.3875, 7.75, 8.05, 14.5, 13.0, 55.9, 14.4583, 7.925, 30.0, 110.8833, 26.0, 40.125, 8.7125, 79.65, 15.0, 79.2, 8.05, 8.05, 7.125, 78.2667, 7.25, 7.75, 26.0, 24.15, 33.0, 0.0, 7.225, 56.9292, 27.0, 7.8958, 42.4, 8.05, 26.55, 15.55, 7.8958, 30.5, 41.5792, 153.4625, 31.275, 7.05, 15.5, 7.75, 8.05, 65.0, 14.4, 16.1, 39.0, 10.5, 14.4542, 52.5542, 15.7417, 7.8542, 16.1, 32.3208, 12.35, 77.9583, 7.8958, 7.7333, 30.0, 7.0542, 30.5, 0.0, 27.9, 13.0, 7.925, 26.25, 39.6875, 16.1, 7.8542, 69.3, 27.9, 56.4958, 19.2583, 76.7292, 7.8958, 35.5, 7.55, 7.55, 7.8958, 23.0, 8.4333, 7.8292, 6.75, 73.5, 7.8958, 15.5, 13.0, 113.275, 133.65, 7.225, 25.5875, 7.4958, 7.925, 73.5, 13.0, 7.775, 8.05, 52.0, 39.0, 52.0, 10.5, 13.0, 0.0, 7.775, 8.05, 9.8417, 46.9, 512.3292, 8.1375, 76.7292, 9.225, 46.9, 39.0, 41.5792, 39.6875, 10.1708, 7.7958, 211.3375, 57.0, 13.4167, 56.4958, 7.225, 26.55, 13.5, 8.05, 7.7333, 110.8833, 7.65, 227.525, 26.2875, 14.4542, 7.7417, 7.8542, 26.0, 13.5, 26.2875, 151.55, 15.2458, 49.5042, 26.55, 52.0, 9.4833, 13.0, 7.65, 227.525, 10.5, 15.5, 7.775, 33.0, 7.0542, 13.0, 13.0, 53.1, 8.6625, 21.0, 7.7375, 26.0, 7.925, 211.3375, 18.7875, 0.0, 13.0, 13.0, 16.1, 34.375, 512.3292, 7.8958, 7.8958, 30.0, 78.85, 262.375, 16.1, 7.925, 71.0, 20.25, 13.0, 53.1, 7.75, 23.0, 12.475, 9.5, 7.8958, 65.0, 14.5, 7.7958, 11.5, 8.05, 86.5, 14.5, 7.125, 7.2292, 120.0, 7.775, 77.9583, 39.6, 7.75, 24.15, 8.3625, 9.5, 7.8542, 10.5, 7.225, 23.0, 7.75, 7.75, 12.475, 7.7375, 211.3375, 7.2292, 57.0, 30.0, 23.45, 7.05, 7.25, 7.4958, 29.125, 20.575, 79.2, 7.75, 26.0, 69.55, 30.6958, 7.8958, 13.0, 25.9292, 8.6833, 7.2292, 24.15, 13.0, 26.25, 120.0, 8.5167, 6.975, 7.775, 0.0, 7.775, 13.0, 53.1, 7.8875, 24.15, 10.5, 31.275, 8.05, 0.0, 7.925, 37.0042, 6.45, 27.9, 93.5, 8.6625, 0.0, 12.475, 39.6875, 6.95, 56.4958, 37.0042, 7.75, 80.0, 14.4542, 18.75, 7.2292, 7.8542, 8.3, 83.1583, 8.6625, 8.05, 56.4958, 29.7, 7.925, 10.5, 31.0, 6.4375, 8.6625, 7.55, 69.55, 7.8958, 33.0, 89.1042, 31.275, 7.775, 15.2458, 39.4, 26.0, 9.35, 164.8667, 26.55, 19.2583, 7.2292, 14.1083, 11.5, 25.9292, 69.55, 13.0, 13.0, 13.8583, 50.4958, 9.5, 11.1333, 7.8958, 52.5542, 5.0, 9.0, 24.0, 7.225, 9.8458, 7.8958, 7.8958, 83.1583, 26.0, 7.8958, 10.5167, 10.5, 7.05, 29.125, 13.0, 30.0, 23.45, 30.0, 7.75]}],\n",
       "                        {\"barmode\": \"overlay\", \"legend\": {\"bgcolor\": \"#F5F6F9\", \"font\": {\"color\": \"#4D5663\"}}, \"paper_bgcolor\": \"#F5F6F9\", \"plot_bgcolor\": \"#F5F6F9\", \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"title\": {\"font\": {\"color\": \"#4D5663\"}}, \"xaxis\": {\"gridcolor\": \"#E1E5ED\", \"showgrid\": true, \"tickfont\": {\"color\": \"#4D5663\"}, \"title\": {\"font\": {\"color\": \"#4D5663\"}, \"text\": \"\"}, \"zerolinecolor\": \"#E1E5ED\"}, \"yaxis\": {\"gridcolor\": \"#E1E5ED\", \"showgrid\": true, \"tickfont\": {\"color\": \"#4D5663\"}, \"title\": {\"font\": {\"color\": \"#4D5663\"}, \"text\": \"\"}, \"zerolinecolor\": \"#E1E5ED\"}},\n",
       "                        {\"showLink\": true, \"linkText\": \"Export to plot.ly\", \"plotlyServerURL\": \"https://plot.ly\", \"responsive\": true}\n",
       "                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('86154ff0-7674-423a-82ef-9ffa8e9a84fc');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })\n",
       "                };\n",
       "                });\n",
       "            </script>\n",
       "        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "train['Fare'].iplot(kind='hist',bins=30,color='green')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "___\n",
    "## Data Cleaning\n",
    "We want to fill in missing age data instead of just dropping the missing age data rows. One way to do this is by filling in the mean age of all the passengers (imputation).\n",
    "However we can be smarter about this and check the average age by passenger class. For example:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x292a4301b48>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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2bMnc+fOLfyawcHBzJ8/P0cddVSSZOHChenu7s4dd9yRarWadevWDd93AAAANXLQmeXt27dn8eLFSZJzzjknl19+ebq7uzNnzpzCr7npppty8cUX50tf+lKSZNOmTZkyZUqSZNq0aXnwwQdz3nnnHXDcgYGB9Pb2/tbfyG+rv79/2J8TytDf31+Tc4Qj1wvvb34uoL6ce43toGV5165d+clPfpLTTz89P/nJT9Lf358dO3YUls677747J5xwQs4555z9Zblare6/mkZra2t27tx50GDNzc1pa2t7Od/Lb6WlpSXJs8P+vFBvLS0tNTlHOHL9+v0tfi6gzpx7R74D/aJz0LI8f/78XH311Xnqqady1FFH5V3vele+9a1v5UMf+tBLfv43vvGNVCqVPPzww+nt7c3cuXOzffv2/Y/v3r0748aNO4RvAwAA6uuga5b/6I/+KB//+Mfztre9Lc8//3y2bduWOXPmZPr06S/5+bfffntWrFiR5cuXp62tLTfddFOmTZuWDRs2JPn1JsHJkycP73cBAAA1UDizvGfPnqxevTq33357xo4dm127dmXdunX7N+29HHPnzs28efOyePHinHbaaYVFGwAADieFZfntb397Zs6cmZtvvjmvfe1r8/73v/9lF+Xly5fv/+8VK1YcekoAAChBYVm+9NJLs2rVqjz++OOZPXv2/tteAwDASFG4ZvmDH/xg7rnnnnR0dGTVqlX5wQ9+kEWLFuXRRx+tZz4AACjNQTf4TZkyJYsWLcratWtz8skn52/+5m/qkQsAAEr3W99zety4ceno6MjKlStrmQcAAA4bv3VZBgCAkUZZBgCAAge9g1+j2bZtW8bufSonPntr2VHgkI3duyXbtu0tOwYANDwzywAAUGDEzSyPHz8+j24ZnaeP+1DZUeCQnfjsrRk//riyYwBAwzOzDAAABZRlAAAoMOKWYQDluOWWW9LX11d2jIb2wr9vV1dXyUka26RJk9Ld3V12DKBOlGWgLvr6+vK9/7spe445sewoDWvUvjFJkod++lTJSRrX2F1Plx0BqDNlGaibPcecmCfO+j9lx4BDdvIj3yg7AlBn1iwDAEABZRkAAAooywAAUEBZBgCAAsoyAAAUUJYBAKCAsgwAAAWUZQAAKKAsAwBAAWUZAAAKKMsAAFBAWQYAgALKMgAAFFCWAQCgwOiyAwAA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7BgADaVua5bf/OY3Z/369UmSRx55JGeccUa9hgYAgENSt6nd8847Lw8++GAuvvjiVKvV39iMAgAAh5u6leWmpqb83d/9Xb2GAwCAV6xuyzAAAOBIoywDAEABZRkAAAooywAAUEBZBgCAAsoyAAAUUJYBAKCAsgwAAAWUZQAAKKAsAwBAgbrd7vrlGhgYSG9vb9kxAABocAMDA4WPVarVarWOWQAA4IhhGQYAABRQlgEAoICyDAAABZRlAAAooCwDAEABZRkAAAooywy7jRs3pqOjo+wYMKIMDg7m6quvziWXXJLZs2dn3bp1ZUeCEbGQwrcAAAQLSURBVGHfvn259tprc/HFF2fOnDl57LHHyo7EMDtsb0rCkenLX/5y7rnnnhx99NFlR4ER5Z577snxxx+fRYsWZceOHXnXu96VP//zPy87FjS8+++/P0ny9a9/PRs2bMjChQvzxS9+seRUDCczywyrU089NUuWLCk7Bow4F1xwQf7yL/9y//GoUaNKTAMjx7nnnpsbb7wxSbJly5ZMmDCh5EQMNzPLDKvp06fnl7/8ZdkxYMRpbW1NkuzatSsf/ehH093dXXIiGDlGjx6duXPnZu3atfn85z9fdhyGmZllgAbxq1/9KpdeemlmzZqVd77znWXHgRHlpptuyr333pt58+alv7+/7DgMI2UZoAFs3bo1l19+ea6++urMnj277DgwYqxcuTK33XZbkuToo49OpVKxDKrBKMsADeDWW2/Nc889l2XLlqWjoyMdHR35n//5n7JjQcM7//zz89///d+ZM2dOrrjiilx33XVpbm4uOxbDqFKtVqtlhwAAgMORmWUAACigLAMAQAFlGQAACijLAABQQFkGAIACyjLAYWjDhg1561vfuv8ycO9973uzfPnyl/zcjo6O/OQnP6lzQoCRwe2uAQ5Tb3nLW/LZz342SbJnz55ccMEFmTVrVsaNG1dyMoCRQ1kGOALs2rUrTU1N+eEPf5ibb7451Wo1r3rVq3LzzTfv/5wnnngiH//4xzMwMJBnnnkmXV1dOffcc/PZz3423/nOdzI0NJT29vZcdtlluf3227Ny5co0NTXlzW9+c+bOnVvidwdw+FKWAQ5T3/nOd9LR0ZFKpZIxY8Zk3rx5+cQnPpHPfvazOf3003P77be/aPnFT3/603R2dubss8/Of/7nf2bJkiU599xzs3LlyqxYsSKvetWrcvfddydJ7r777sybNy9nnXVW7rjjjuzduzejR/tfAsD/5p0R4DD1/y7DeMF1112X008/PUkyZ86cFz124okn5otf/GLuuuuuVCqV7N27N0myePHiLF68OFu3bs0555yTJFm4cGG+8pWv5Oabb85ZZ50VN3MFeGk2+AEcQU466aT87Gc/S5J86Utfytq1a/c/9rnPfS6zZs3KokWLcvbZZ6darWbPnj35l3/5lyxevDh///d/n3/+53/O448/njvvvDM33HBDVqxYkd7e3nz/+98v6TsCOLyZWQY4gtxwww257rrr0tTUlBNPPDGXXXZZ/uEf/iFJcsEFF+STn/xkbrvttvzu7/5uduzYkbFjx+a4447LrFmzctxxx+VP/uRP8upXvzqvf/3rM3v27PzO7/xOXvWqV+XMM88s+TsDODxVqv72BgAAL8kyDAAAKKAsAwBAAWUZAAAKKMsAAFBAWQYAgALKMgAAFFCWAQCgwP8HzBfOAzDcgaQAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 864x504 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12, 7))\n",
    "sns.boxplot(x='Pclass',y='Age',data=train,palette='winter')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can see the wealthier passengers in the higher classes tend to be older, which makes sense. We'll use these average age values to impute based on Pclass for Age."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def impute_age(cols):\n",
    "    Age = cols[0]\n",
    "    Pclass = cols[1]\n",
    "    \n",
    "    if pd.isnull(Age):\n",
    "\n",
    "        if Pclass == 1:\n",
    "            return 37\n",
    "\n",
    "        elif Pclass == 2:\n",
    "            return 29\n",
    "\n",
    "        else:\n",
    "            return 24\n",
    "\n",
    "    else:\n",
    "        return Age"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now apply that function!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now let's check that heat map again!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x2929ef9ee48>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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4khNZvvwR3Z2tiZMmOBf3a86XeT2319ISIjRC0R/axMnTlR0dLTCw8MVFhamgwcPavPmzZo1a5bRusOGDdOyZct0880365ZbblGXLl1cfb5ruxfuvPNOLVy48Iy7w0yeShsxYoSWLl1qvGHziBEj/KvcDz74oPEOR+dbOfWpqXN3puXk5Jxx+OO7774zdvjD5t/frFmzXN8RUd0UFhZq48aNys/P11VXXaXevXsbP9ji89NPPykgIMD1eq6NdMPCwvxNWmyw0VDkbDZO4BCs7rN5+MPm319ND1yp8mbe/v37W625adMmzZgxQ40aNVJJSYlmzJih7t27u/Z810a6MTExKioq0o033uifczE5mX++/YImtrP06NFD4eHhchxHW7Zs8c8LSrzuAzXR4MGD9eqrryo4OFgFBQV69NFHXe174tpI1/QJrbOd70ptE9fZzJs3z/9zm/shAfw26tev7z/V17Rp0+q7Zezuu+/W2rVrdejQIXXv3l2tW7d269Hn5Wtk7DiOvvnmG2P7ZnndBy4Nvu135eXlGjt2rLp06aIdO3a4vjblWuhOmzbN6LXFZzt71GljJwOAmsu3/a7qNjwTB2hcC13T1xafrWoDk/z8fB06dMhoPQA1m2/7XWFhobZu3XrG9lc3uRa6pq8tPltCQoK/gUmTJk0uiZVcAOY9/PDDuv7669WwYUNJlacX3dzX7Vronn1tsaleAb7ba6s2MDl16pTxI5cALg0NGzZUUlKSsee7tmXM59ixY2rUqJHq1HEtz88QFRWliRMn6oYbblDfvn2VnJzsb2Biep8ugJpvyZIlqlev3hk3jXft2tW157uWjO+//74qKipUVlam5ORkjRo1SqNGjXLr8X4XamBiq68ugJrt888/V1lZmbZt2yapcnqhWobukiVLtGjRIsXGxuqjjz7Sww8/bCR0L9TApLi42PVaAC49JSUlRtvEuha6devWlVS5sdh3n5EJv8XttQAuHa1bt9a6devUrl07/+laN7u5uTan+9RTT2nr1q16+umntWvXLhUUFBi7tdNmAxMAlxbf1U6+aCwrK/PfKu0GVxfSiouLVb9+fR05csR/YgwA/hPExMT4j/2//vrr/unR4cOH+y+odYNrq0/btm3TF198oU2bNikyMlLvvvuuW48GAOOOHj3q//mmTZv8P3e7abproZucnKyWLVsqJSVFq1atYvsWgP9YJtu4uha6devW1eWXX646deqoadOmKisrc+vRAGBc1RGtySuBXNu90KBBAz300EO6//77tWLFijNukACA6u58Vy05jqOcnBxX67i2kFZWVqbc3Fxdf/31+v7779WyZUuj1/UAgJtsXbXkWuju27dPGRkZ/h4I+fn5xq8pB4D/NK7N6fq6fG3fvl0HDhzQ8ePH3Xo0ANQYroVuYGCgxo4dqyuuuELPP/+8jhw54tajAaDGcC10HcdRQUGBSkpKVFJSohMnTrj1aACoMVwJ3aKiIj322GPasGGD+vXrpz59+qhXr15uPBoAapSLXkhbvny5lixZojp16mjq1KmELQD8iose6a5bt04ZGRlKTU1VSkqKG18TANRYFx26Xq9XXq9XwcHBXJkDAP8LV69bMHleGQBqgoue0+3Ro4fCw8PlOI62bNniv81BkubMmXPRXyAA1CQXHbq2js4BQE3g+m3AAIAL4wpdALCI0AUAiwhdALCI0AUAiwhdALDovwEuOkC/DosI+gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Let's go ahead and drop the Cabin column and the row in Embarked that is NaN."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "train.drop('Cabin',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Embarked  \n",
       "0      0         A/5 21171   7.2500        S  \n",
       "1      0          PC 17599  71.2833        C  \n",
       "2      0  STON/O2. 3101282   7.9250        S  \n",
       "3      0            113803  53.1000        S  \n",
       "4      0            373450   8.0500        S  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.head(5)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "train.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Converting Categorical Features \n",
    "\n",
    "We'll need to convert categorical features to dummy variables using pandas! Otherwise our machine learning algorithm won't be able to directly take in those features as inputs."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 889 entries, 0 to 890\n",
      "Data columns (total 11 columns):\n",
      "PassengerId    889 non-null int64\n",
      "Survived       889 non-null int64\n",
      "Pclass         889 non-null int64\n",
      "Name           889 non-null object\n",
      "Sex            889 non-null object\n",
      "Age            889 non-null float64\n",
      "SibSp          889 non-null int64\n",
      "Parch          889 non-null int64\n",
      "Ticket         889 non-null object\n",
      "Fare           889 non-null float64\n",
      "Embarked       889 non-null object\n",
      "dtypes: float64(2), int64(5), object(4)\n",
      "memory usage: 83.3+ KB\n"
     ]
    }
   ],
   "source": [
    "train.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "sex = pd.get_dummies(train['Sex'],drop_first=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "train.drop(['Sex','Embarked','Name','Ticket','Pclass','PassengerId','SibSp','Parch'],axis=1,inplace=True)"
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
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "train = pd.concat([train,sex],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Survived</th>\n",
       "      <th>Age</th>\n",
       "      <th>Fare</th>\n",
       "      <th>male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>22.0</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>38.0</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>26.0</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>35.0</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>35.0</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Survived   Age     Fare  male\n",
       "0         0  22.0   7.2500     1\n",
       "1         1  38.0  71.2833     0\n",
       "2         1  26.0   7.9250     0\n",
       "3         1  35.0  53.1000     0\n",
       "4         0  35.0   8.0500     1"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "train.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Great! Our data is ready for our model!\n",
    "\n",
    "# Building a Logistic Regression model\n",
    "\n",
    "Let's start by splitting our data into a training set and test set (there is another test.csv file that you can play around with in case you want to use all this data for training).\n",
    "\n",
    "## Train Test Split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(train.drop('Survived',axis=1), \n",
    "                                                    train['Survived'], test_size=0.30, \n",
    "                                                    random_state=101)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Training and Predicting"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "                   intercept_scaling=1, l1_ratio=None, max_iter=100,\n",
       "                   multi_class='warn', n_jobs=None, penalty='l2',\n",
       "                   random_state=None, solver='warn', tol=0.0001, verbose=0,\n",
       "                   warm_start=False)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "logmodel = LogisticRegression()\n",
    "logmodel.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "inputt=[int(x) for x in \"45 32 60\".split(' ')]\n",
    "final=[np.array(inputt)]\n",
    "\n",
    "b = logmodel.predict_proba(final)\n",
    "\n",
    "\n",
    "pickle.dump(logmodel,open('model.pkl','wb'))\n",
    "model=pickle.load(open('model.pkl','rb'))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's move on to evaluate our model!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Evaluation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can check precision,recall,f1-score using classification report!"
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
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Not so bad! You might want to explore other feature engineering and the other titanic_text.csv file, some suggestions for feature engineering:\n",
    "\n",
    "* Try grabbing the Title (Dr.,Mr.,Mrs,etc..) from the name as a feature\n",
    "* Maybe the Cabin letter could be a feature\n",
    "* Is there any info you can get from the ticket?\n",
    "\n",
    "## Great Job!"
   ]
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
