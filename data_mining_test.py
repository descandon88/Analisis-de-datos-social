{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "data_mining_test.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPGbsZxutAX8dIpkHGxQ9IG",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/descandon88/Analisis-de-datos-social/blob/main/data_mining_test.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ylgy0ECAQQYW",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b170ab15-bc79-41bf-f766-d9b24d9d735d"
      },
      "source": [
        "## INSTALACION DE LIBRERIAS NECESARIAS\n",
        "!pip install Tweepy\n",
        "!pip install vaderSentiment #(para después)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: Tweepy in /usr/local/lib/python3.7/dist-packages (3.10.0)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.7/dist-packages (from Tweepy) (1.3.0)\n",
            "Requirement already satisfied: requests[socks]>=2.11.1 in /usr/local/lib/python3.7/dist-packages (from Tweepy) (2.23.0)\n",
            "Requirement already satisfied: six>=1.10.0 in /usr/local/lib/python3.7/dist-packages (from Tweepy) (1.15.0)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.7/dist-packages (from requests-oauthlib>=0.7.0->Tweepy) (3.1.0)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests[socks]>=2.11.1->Tweepy) (1.24.3)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests[socks]>=2.11.1->Tweepy) (2.10)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests[socks]>=2.11.1->Tweepy) (2020.12.5)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests[socks]>=2.11.1->Tweepy) (3.0.4)\n",
            "Requirement already satisfied: PySocks!=1.5.7,>=1.5.6; extra == \"socks\" in /usr/local/lib/python3.7/dist-packages (from requests[socks]>=2.11.1->Tweepy) (1.7.1)\n",
            "Collecting vaderSentiment\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/76/fc/310e16254683c1ed35eeb97386986d6c00bc29df17ce280aed64d55537e9/vaderSentiment-3.3.2-py2.py3-none-any.whl (125kB)\n",
            "\u001b[K     |████████████████████████████████| 133kB 5.5MB/s \n",
            "\u001b[?25hRequirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from vaderSentiment) (2.23.0)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->vaderSentiment) (2.10)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->vaderSentiment) (1.24.3)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->vaderSentiment) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->vaderSentiment) (2020.12.5)\n",
            "Installing collected packages: vaderSentiment\n",
            "Successfully installed vaderSentiment-3.3.2\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "T9RMA42vQQ7r"
      },
      "source": [
        "## LIBRERIAS A UTILIZAR\n",
        "import pandas as pd\n",
        "import tweepy\n",
        "import tweepy # Python wrapper around Twitter API\n",
        "import json\n",
        "from datetime import date\n",
        "from datetime import datetime\n",
        "import time\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6FyXBHT5tRzv"
      },
      "source": [
        "## VALIDACION DE TOKENS\n",
        "\n",
        "CONSUMER_KEY = 'neJIIPK2CIii74UVmgIqscov8'\n",
        "CONSUMER_SECRET = 'sqMCQ296xYQuA1XT0vSchc0pwu0ToogJQ9fz7fXW5bS0UDB7Rx'\n",
        "ACCESS_TOKEN = '1384513082815352832-9m0677EJslnroFrpE0BhsDwszqr6Gc'\n",
        "ACCESS_TOKEN_SECRET = 'WPrBsb116p72YclhdD5aY7XzKRDIYQDCaWeHm64POsfPd'\n",
        "\n",
        "auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)\n",
        "auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)\n",
        "api = tweepy.API(auth)\n",
        "\n",
        "#status = \"Testing!\"\n",
        "#api.update_status(status=status)"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CwC1v6lZubBp",
        "outputId": "fcbe3fa1-5c40-4371-b0cc-77c11c59389c"
      },
      "source": [
        "user = api.get_user(\"GabrielBurdin\")\n",
        "\n",
        "print(\"Detalles del Usuario:\")\n",
        "print(user.name)\n",
        "print(user.description)\n",
        "print(user.location)\n",
        "\n",
        "print(\"Los últimos 20 seguidores:\")\n",
        "for follower in user.followers():\n",
        "    print(follower.name)"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Detalles del Usuario:\n",
            "Gabriel Burdin\n",
            "Associate Professor in Economics @LeedsUniBSchool | @iza_bonn Research Fellow | @FCEA_UdelaR Affiliated Researcher | Views are my own: https://t.co/Ra8NW4qTZH\n",
            "\n",
            "Los últimos 20 seguidores:\n",
            "Agos\n",
            "Carlos Siculi\n",
            "SaraM.\n",
            "Jorge L. Achard\n",
            "Francisco Medina\n",
            "Micaela\n",
            "Sunghun Lim\n",
            "GigiRiots\n",
            "Hugo Barretto Ghione\n",
            "Eduardo Santos\n",
            "by George, it’s land taxing time!\n",
            "Francisco Sánchez\n",
            "Dirk Ehnts\n",
            "andrés ignacio torres\n",
            "+Rossy\n",
            "José Luis Colombia\n",
            "Leeds University Business School\n",
            "Federico\n",
            "Ariel Stefanoli\n",
            "Justin Graside\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zXlMp0QjxQ-y",
        "outputId": "519a41fc-0268-4407-8b26-f30b0223a0d2"
      },
      "source": [
        "user = api.get_user(\"vaillant_marcel\")\n",
        "\n",
        "print(\"Detalles del Usuario:\")\n",
        "print(user.name)\n",
        "print(user.description)\n",
        "print(user.location)\n",
        "\n",
        "print(\"Los últimos 20 seguidores:\")\n",
        "for follower in user.followers():\n",
        "    print(follower.name)"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Detalles del Usuario:\n",
            "marcel vaillant\n",
            "Mandarina criolla\n",
            "Montevideo, Uruguay\n",
            "Los últimos 20 seguidores:\n",
            "MACARENA\n",
            "Eugenia Zas\n",
            "Mariana\n",
            "Matías Fellay\n",
            "Ariel Stefanoli\n",
            "Nicolás\n",
            "José Carro\n",
            "Néstor Saldain\n",
            "Santiago Aristoy\n",
            "Socrates2\n",
            "A. López\n",
            "Pz. trading investment\n",
            "Mauro Navarrine\n",
            "Mauricio Suárez\n",
            "Nicole\n",
            "Santiago Pereira Campos\n",
            "Gabriela Casullo\n",
            "Martin Sprechmann\n",
            "María Inés mailhos\n",
            "Daniel Giménez\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CXdq3zQUxxWf",
        "outputId": "02c5b2e2-ebdd-4784-906a-fbe603718ed8"
      },
      "source": [
        "#Extraccion de tweets\n",
        "# We create an extractor object:\n",
        "#extractor = twitter_setup()\n",
        "\n",
        "# We create a tweet list as follows:\n",
        "tweets = api.user_timeline(screen_name=\"vaillant_marcel\", count=10)\n",
        "print(\"Número de los tweets extridos: {}.\\n\".format(len(tweets)))\n",
        "\n",
        "# Se imprime los 5 tweets recientes:\n",
        "print(\"Los 5 tweets recientes:\\n\")\n",
        "for tweet in tweets[:5]:\n",
        "    print(tweet.text)\n",
        "    print()"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Número de los tweets extridos: 10.\n",
            "\n",
            "Los 5 tweets recientes:\n",
            "\n",
            "@luismardones Ejemplo errores no forzados. Dificil de entender esta carta. Que la firme algún sector sería natural… https://t.co/xaHmr5iqtk\n",
            "\n",
            "Hechos recientes ilustran que el gobierno trabaja para la oposición. Y la oposición para el gobierno. Tema de la ev… https://t.co/F0kh485oaL\n",
            "\n",
            "@juancahallak Importar para exportar. Lema de las CGV, importás una parte para ponerle un fragmento de producción y… https://t.co/cWBYc97ac0\n",
            "\n",
            "@juancahallak Sirve de contraejemplo. Para import to export!!!!!\n",
            "\n",
            "@conradoh47 China Zorrilla\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "udzopPR9cUgI",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 331
        },
        "outputId": "15891169-8a79-46de-f15c-a49f22f4cd69"
      },
      "source": [
        "# Creando dataframe de los tweets de las cuentas\n",
        "data_tweets = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])\n",
        "\n",
        "# print de los 10 tweets\n",
        "display(data_tweets.head(10))"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "display_data",
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
              "      <th>Tweets</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>@luismardones Ejemplo errores no forzados. Dif...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Hechos recientes ilustran que el gobierno trab...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>@juancahallak Importar para exportar. Lema de ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>@juancahallak Sirve de contraejemplo. Para imp...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>@conradoh47 China Zorrilla</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>RT @_AnabelG: Al llegar a su 30 aniversario, e...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>RT @RazonesPersonas: \"¿Precisamos un GACH econ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>Un factor no obvio de este bloqueo proteccioni...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Luego de tanta retórica información útil para ...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>@nicotrajtenberg @heber_freiria Feynman</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                              Tweets\n",
              "0  @luismardones Ejemplo errores no forzados. Dif...\n",
              "1  Hechos recientes ilustran que el gobierno trab...\n",
              "2  @juancahallak Importar para exportar. Lema de ...\n",
              "3  @juancahallak Sirve de contraejemplo. Para imp...\n",
              "4                         @conradoh47 China Zorrilla\n",
              "5  RT @_AnabelG: Al llegar a su 30 aniversario, e...\n",
              "6  RT @RazonesPersonas: \"¿Precisamos un GACH econ...\n",
              "7  Un factor no obvio de este bloqueo proteccioni...\n",
              "8  Luego de tanta retórica información útil para ...\n",
              "9            @nicotrajtenberg @heber_freiria Feynman"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 331
        },
        "id": "qgGMGxLnywO3",
        "outputId": "f69600f7-e290-4f3c-ea25-ac3ca9264c0f"
      },
      "source": [
        "## PRIMER EJERCICIO DE DATAFRAME DE UNA CUENTA\n",
        "\n",
        "data_tweets['len']  = np.array([len(tweet.text) for tweet in tweets])\n",
        "data_tweets['ID']   = np.array([tweet.id for tweet in tweets])\n",
        "data_tweets['Date'] = np.array([tweet.created_at for tweet in tweets])\n",
        "data_tweets['Source'] = np.array([tweet.source for tweet in tweets])\n",
        "data_tweets['Likes']  = np.array([tweet.favorite_count for tweet in tweets])\n",
        "data_tweets['RTs']    = np.array([tweet.retweet_count for tweet in tweets])\n",
        "data_tweets.head(10)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
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
              "      <th>Tweets</th>\n",
              "      <th>len</th>\n",
              "      <th>ID</th>\n",
              "      <th>Date</th>\n",
              "      <th>Source</th>\n",
              "      <th>Likes</th>\n",
              "      <th>RTs</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>@luismardones Ejemplo errores no forzados. Dif...</td>\n",
              "      <td>139</td>\n",
              "      <td>1384201423525613577</td>\n",
              "      <td>2021-04-19 17:45:11</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Hechos recientes ilustran que el gobierno trab...</td>\n",
              "      <td>140</td>\n",
              "      <td>1384191021681037317</td>\n",
              "      <td>2021-04-19 17:03:51</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>17</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>@juancahallak Importar para exportar. Lema de ...</td>\n",
              "      <td>140</td>\n",
              "      <td>1383587990455291906</td>\n",
              "      <td>2021-04-18 01:07:37</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>@juancahallak Sirve de contraejemplo. Para imp...</td>\n",
              "      <td>64</td>\n",
              "      <td>1383531585367015429</td>\n",
              "      <td>2021-04-17 21:23:29</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>@conradoh47 China Zorrilla</td>\n",
              "      <td>26</td>\n",
              "      <td>1383112897337954310</td>\n",
              "      <td>2021-04-16 17:39:46</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>RT @_AnabelG: Al llegar a su 30 aniversario, e...</td>\n",
              "      <td>139</td>\n",
              "      <td>1382877539601907715</td>\n",
              "      <td>2021-04-16 02:04:32</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>0</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>RT @RazonesPersonas: \"¿Precisamos un GACH econ...</td>\n",
              "      <td>140</td>\n",
              "      <td>1382745834299740170</td>\n",
              "      <td>2021-04-15 17:21:11</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>0</td>\n",
              "      <td>19</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>Un factor no obvio de este bloqueo proteccioni...</td>\n",
              "      <td>140</td>\n",
              "      <td>1382711921468657666</td>\n",
              "      <td>2021-04-15 15:06:26</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Luego de tanta retórica información útil para ...</td>\n",
              "      <td>137</td>\n",
              "      <td>1382711919140868104</td>\n",
              "      <td>2021-04-15 15:06:25</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>@nicotrajtenberg @heber_freiria Feynman</td>\n",
              "      <td>39</td>\n",
              "      <td>1382664104054304768</td>\n",
              "      <td>2021-04-15 11:56:25</td>\n",
              "      <td>Twitter Web App</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                              Tweets  len  ...  Likes RTs\n",
              "0  @luismardones Ejemplo errores no forzados. Dif...  139  ...      2   0\n",
              "1  Hechos recientes ilustran que el gobierno trab...  140  ...     17   3\n",
              "2  @juancahallak Importar para exportar. Lema de ...  140  ...      0   0\n",
              "3  @juancahallak Sirve de contraejemplo. Para imp...   64  ...      0   0\n",
              "4                         @conradoh47 China Zorrilla   26  ...      1   0\n",
              "5  RT @_AnabelG: Al llegar a su 30 aniversario, e...  139  ...      0   5\n",
              "6  RT @RazonesPersonas: \"¿Precisamos un GACH econ...  140  ...      0  19\n",
              "7  Un factor no obvio de este bloqueo proteccioni...  140  ...      1   0\n",
              "8  Luego de tanta retórica información útil para ...  137  ...      2   0\n",
              "9            @nicotrajtenberg @heber_freiria Feynman   39  ...      1   0\n",
              "\n",
              "[10 rows x 7 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 15
        }
      ]
    }
  ]
}