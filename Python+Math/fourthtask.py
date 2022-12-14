
#[Q]: 4. Казино предлагает вам сыграть в игру: вы бросаете два 6-гранных игральных кубика,
#и получаете приз в зависимости от выпавшей на них суммы очков:
#12 очков: 100 рублей
#11 очков: 90 рублей
#10 очков: 80 рублей
#9 очков: 50 рублей
#от 2 до 8 очков: 0 рублей
#Какую максимальную сумму вы согласны заплатить за возможность один раз сыграть в такую игру?

#[A]: Решение:
#Всего имеем 36 различных вариантов выпадения двух кубиков. Денежное вознаграждение будет получено при следующих комбинациях:
#9 очков: (4, 5), (5, 4), (3, 6), (6, 3), то есть 4/36;
#10 очков: (5, 5), (4, 6), (6, 4), то есть 3/36;
#11 очков: (5, 6), (6, 5), то есть 2/36;
#12 очков: (6, 6), то есть 1/36.
#Домножив полученные вероятности на их соответствующие денежные призы и сложив результаты, получим максимальную сумму, которую я готов заплатить за такую игру:
#50 * 4 /36 + 80 * 3/36 + 90 * 2/36 + 100 * 1/36 = 20  рублей.
#Ответ: 20 рублей.
