
#[Q]: 3. Один поезд выехал из пункта А в пункт Б, одновременно с ним другой поезд выехал из пункта Б в пункт А.
#Поезда двигаются с постоянными скоростями. Они встретились в 15 часов, машинисты на ходу помахали друг другу из
#окон, и продолжили двигаться к своим конечным пунктам.
#Первый поезд доехал до своего пункта назначения через 9 часов после встречи, а второй до своего - через 16 часов после встречи.
#Во сколько они стартовали?

#[A]: Решение:
#Пусть расстояние между пунктами А и Б равно S;
#Скорость поездов равна V1 и V2 соответственно;
#x -  время от выезда до встречи поездов (в часах).
#Тогда имеет место система 3 уравнений:
#S = V1x + V2x;        (1) - расстояние, выраженное через время до встречи поездов
#S = (x+9)V1;            (2) - расстояние, выраженное через общее время поездки 1-го поезда
#S = (x+16)V2           (3) - расстояние, выраженное через общее время поездки 2-го поезда
#Далее выразим V1 и V2 из уравнений (2) и (3) соответственно и подставим их в уравнение (1):
#(2): V1 = S/(x+9);
#(3): V2 = S/(x+16).
#Тогда уравнение (1) примет вид:
#S = Sx/(x+9) + Sx/(x+16);        | разделим обе части на S != 0
#x/(x+9) + x/(x+16) = 1;
#(x^2 + 16x + x^2 + 9x)/(x^2 + 25x + 144) = 1;
#2x^2 + 25x = x^2 + 25x + 144;
#x^2  - 144 = 0 => x = +- 12, но так как x - положительная величина, то рассматриваем только x = 12
#Таким образом, время выезда поездов будет равно 15 - x = 3.
#Ответ: Поезда стартовали в 3 часа.