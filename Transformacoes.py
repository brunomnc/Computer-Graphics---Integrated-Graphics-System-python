import numpy as np
from numpy.matlib import identity
from math import sin, cos, pi


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
        theta = 10 * pi / 180
    if direcao == 'r':
        theta = - 10 * pi / 180

    matriz_rotacao = np.array([[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]])
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


def translacao3d(pontos3d, tx, ty, tz):
    matriz_transformacao = np.array([[1, 0, 0, 0],
                                     [0, 1, 0, 0],
                                     [0, 0, 1, 0],
                                     [tx, ty, tz, 1]])

    transformacao3d(pontos3d, matriz_transformacao)


def escalonamento3d(pontos, mult, tx, ty, tz):
    matriz_escala = np.array([[mult, 0, 0, 0], [0, mult, 0, 0], [0, 0, mult, 0], [0, 0, 0, 1]])
    matriz_centro = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-tx, -ty, -tz, 1]])
    matriz_centro_objeto = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [tx, ty, tz, 1]])
    matriz_transformacao = np.dot(np.dot(matriz_centro, matriz_escala), matriz_centro_objeto)

    transformacao3d(pontos, matriz_transformacao)


def rotacao3d(pontos, direcao, tx, ty, tz):
    if direcao == 'l':
        theta = 10 * pi / 180
        eixo = 'y'
    if direcao == 'r':
        theta = - 10 * pi / 180
        eixo = 'y'
    if direcao == 'u':
        theta = 10 * pi / 180
        eixo = 'x'
    if direcao == 'd':
        theta = - 10 * pi / 180
        eixo = 'x'

    identidade = identity(4, dtype=int)
    matriz_rotacao_x = identidade
    matriz_rotacao_y = identidade
    matriz_rotacao_z = identidade

    matriz_centro = np.array([[1, 0, 0, 0],
                              [0, 1, 0, 0],
                              [0, 0, 1, 0],
                              [-tx, -ty, -tz, 1]])

    matriz_centro_objeto = np.array([[1, 0, 0, 0],
                                     [0, 1, 0, 0],
                                     [0, 0, 1, 0],
                                     [tx, ty, tz, 1]])

    if eixo == 'y':
        matriz_rotacao_x = np.array([[1, 0,  0, 0],
                                   [0, cos(0), sin(0), 0],
                                   [0, sin(0), cos(0), 0],
                                   [0, 0, 0, 1]])

        matriz_rotacao_y = np.array([[cos(theta), 0, -sin(theta), 0],
                                     [0, 1, 0, 0],
                                     [sin(theta), 0, cos(theta), 0],
                                     [0, 0, 0, 1]])

        matriz_rotacao_z = np.array([[cos(0),-sin(0), 0, 0],
                                     [sin(0), cos(0), 0, 0],
                                     [0, 0, 1, 0],
                                     [0, 0, 0, 1]])


    if eixo == 'x':

        matriz_rotacao_z = np.array([[cos(theta),-sin(theta), 0, 0],
                                     [sin(theta), cos(theta), 0, 0],
                                     [0, 0, 1, 0],
                                     [0, 0, 0, 1]])

    matriz_transformacao = matriz_centro @ matriz_rotacao_x @ matriz_rotacao_y @ matriz_rotacao_z @ matriz_centro_objeto

    transformacao3d(pontos, matriz_transformacao)


def transformacao3d(pontos3d, matriz_transformacao):
    for ponto in pontos3d:
        m = np.array([ponto.x, ponto.y, ponto.z, 1])
        new_point = np.dot(m, matriz_transformacao)
        ponto.x = new_point.flat[0]
        ponto.y = new_point.flat[1]
        ponto.z = new_point.flat[2]


def perspectiva(pontos3d, d):
    M = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 0],
                 [0, 0, d, 1]])

    for ponto in pontos3d:
        m = np.array([ponto.x, ponto.y, ponto.z, 1])
        p = m @ M

        ponto.x = p.flat[0] * d / p.flat[2]
        ponto.y = p.flat[1] * d / p.flat[2]
        ponto.z = d


