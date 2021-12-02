# multi: cpu-bound-task

Генерация монет при 1 задействованном воркере <br>
![1proc](https://github.com/grigoryblack/multi/blob/main/results/1processor.png)

Генерация монет при 5 воркерах <br>
![5proc](https://github.com/grigoryblack/multi/blob/main/results/5processors.png)

При повышении числа воркеров увеличивается шанс нахождения монеты, поскольку проверку совершает не 1 процессор, а несколько.

Ресурсы

1 процессор <br>
![result1](https://github.com/grigoryblack/multi/blob/main/results/1processor_result.png)

3 воркер <br>
![result3](https://github.com/grigoryblack/multi/blob/main/results/3processors_result.png)

7 воркер <br>
![result7](https://github.com/grigoryblack/multi/blob/main/results/7processors_result.png)

# multi: io-bound-task

Время синхронной проверки достигла 20 минут для очень маленького объема данных. <br>
В случае с распараллеливанием, время всех проверок сократилось до 2-3 минут. <br>
При увеличении числа потоков растут ресурсы сети (ethernet) и центрального процессора (cpu).
