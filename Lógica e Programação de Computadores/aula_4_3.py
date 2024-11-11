{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNp8Fuz0fguW22HE74aJ9oC",
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
        "<a href=\"https://colab.research.google.com/github/brendhaed/Faculdade-ADS/blob/main/L%C3%B3gica%20e%20Programa%C3%A7%C3%A3o%20de%20Computadores/aula_4_3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "EE2RYFXQO4i2"
      },
      "outputs": [],
      "source": [
        "#Exemplo 7: Variação do exemplo 5 (versão encadeada)\n",
        "nota = int(input(\"Nota: \"))\n",
        "\n",
        "if nota >=90:\n",
        "  print(\"Conceito A\")\n",
        "elif nota >=80:\n",
        "  print(\"Conceito B\")\n",
        "elif nota >=70:\n",
        "  print(\"Conceito C\")\n",
        "elif nota >=60:\n",
        "  print(\"Conceito D\")\n",
        "else:\n",
        "  print(\"Conceito F\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Exemplo 8: total de dias em mes qualquer de 1-12 (sem bissextos)\n",
        "mes = int(input(\"Mês: \"))\n",
        "if mes == 2:\n",
        "  dias = 28\n",
        "elif mes == 4 or mes == 6 or mes == 9 or mes == 11:\n",
        "  dias = 30\n",
        "else:\n",
        "  dias = 31\n",
        "print(f\"Total de dias: {dias}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wJdQBiXSPmzq",
        "outputId": "393904c4-8d9f-4a2b-e681-585404ccb5f6"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mês: 6\n",
            "Total de dias: 30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Exemplo 9: classificação a partir do cálculo do IMC:\n",
        "altura = float(input(\"Altura (m):\"))\n",
        "peso = float(input(\"Peso (kg):\"))\n",
        "imc = peso/altura**2\n",
        "print(f\"Seu IMC é: {imc}\")\n",
        "\n",
        "if imc < 18.6:\n",
        "  print(\"Abaixo do peso\")\n",
        "elif imc < 25:\n",
        "  print(\"Peso normal\")\n",
        "elif imc < 30:\n",
        "  print(\"Sobrepeso\")\n",
        "elif imc < 35:\n",
        "  print(\"Obesidade grau 1\")\n",
        "elif imc < 40:\n",
        "  print(\"Obesidade grau 2\")\n",
        "else:\n",
        "  print(\"Obesidade grau 3 (severa)\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "69i_MYulT8GK",
        "outputId": "3af6bdb4-f33c-4c43-c5f8-a40c10fc561c"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Altura (m):1.55\n",
            "Peso (kg):50\n",
            "Seu IMC é: 20.811654526534856\n",
            "Peso normal\n"
          ]
        }
      ]
    }
  ]
}