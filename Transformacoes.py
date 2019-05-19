import numpy as np
import math as math


def translacao(pontos, dx, dy):
    matriz_transformacao = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])

    transformacao(pontos, matriz_transformacao)


def escalonamento(pontos, mult, dx, dy):
    matriz_escala = np.array([[mult, 0, 0], [0, mult, 0], [0, 0, 1]])
    matriz_centro = np.array([[1, 0, 0], [0, 1, 0], [-dx, -dy, 1]])
    matriz_centro_objeto = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])
    matriz_transformacao = np.dot(np.dot(matriz_centro, matriz_escala), matriz_centro_objeto)

    transformacao(pontos, matriz_transformacao)


def rotacao(pontos, direcao, dx, dy):
    if direcao == 'l':
        theta = 10 * math.pi / 180
    if direcao == 'r':
        theta = - 10 * math.pi / 180

    matriz_rotacao = np.array([[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]])
    matriz_centro = np.array([[1, 0, 0], [0, 1, 0], [-dx, -dy, 1]])
    matriz_centro_objeto = np.array([[1, 0, 0], [0, 1, 0], [dx, dy, 1]])
    matriz_transformacao = np.dot(np.dot(matriz_centro, matriz_rotacao), matriz_centro_objeto)

    transformacao(pontos, matriz_transformacao)


def transformacao(pontos, matriz_transformacao):
    for ponto in pontos:
        m = np.array([ponto.x, ponto.y, 1])
        new_point = np.dot(m, matriz_transformacao)
        ponto.x = new_point.flat[0]
        ponto.y = new_point.flat[1]