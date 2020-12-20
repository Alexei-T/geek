# <a name="top"> <p align=center> **ДЗ по курсу Факультет Devops** </a>   
1. [Введение в UNIX-системы](#ux1)
## <p align=center> Введение в UNIX-системы <a name="ux1"></a>    
1. [Задание №1 - Знакомство с UNIX/Linux](https://github.com/Alexei-T/geek/tree/master/1)
 <details><summary>Описание задания №1</summary>   
    
1)Установить Virtualbox или VMWare Player, установить виртуальную машину с Ubuntu.   
2)Разобраться, что такое bash, используя справочные системы.  
3)Разобраться, как копировать и удалять файлы.    
\* Установить mc и openssh-server.  
\* Если вы работаете в Windows, установить PuTTY для подключения к виртуальной машине по ssh и подключиться.
</details>  

2.  [Задание №2 - Работа в консоли](https://github.com/Alexei-T/geek/tree/main/2)   
<details><summary>Описание задания №2</summary>  
 
1)Просмотреть содержимое директорий /etc, /proc, /home. Посмотреть пару произвольных файлов в /etc.        
2)Выяснить, для чего предназначена команда cat. Используя данную команду, создать два файла с данными, а затем объединить их. Просмотреть содержимое созданного файла.   Переименовать файл, дав ему новое имя.    
3)Создать несколько файлов. Создать директорию, переместить файл туда. Удалить все созданные в этом и предыдущем задании директории и файлы. В ОС Linux скрытыми файлами считаются те, имена которых начинаются с символа “.”. Сколько скрытых файлов в вашем домашнем каталоге? (Использовать конвейер. Подсказка: для подсчета количества строк можно использовать wc.)      
4)Попробовать вывести с помощью cat содержимое всех файлов в директории /etc. Направить ошибки в отдельный файл в вашей домашней директории. Сколько файлов, которые не удалось посмотреть, оказалось в списке?    
5)Запустить в одном терминале программу, а в другом терминале посмотреть PID процесса и остановить с помощью kill, посылая разные типы сигналов. Что происходит?     
\* Полезное задание на конвейер. Использовать команду cut на вывод длинного списка каталога, чтобы отобразить только права доступа к файлам. Затем отправить в конвейере этот вывод на sort и uniq, чтобы отфильтровать все повторяющиеся строки. Потом с помощью wc подсчитать различные типы разрешений в этом каталоге. Самостоятельно решить задачу, как сделать так, чтобы в подсчет не добавлялись строка «Итого» и файлы . и .. (ссылки на текущую и родительскую директории).
</details>

3. [Задание №3 - Права и пользователи в UNIX](https://github.com/Alexei-T/geek/tree/master/3)    
<details><summary>Описание задания №3</summary>  
 
1)Создать файл file1 и наполнить его произвольным содержимым. Скопировать его в file2. Создать символическую ссылку file3 на file1. Создать жесткую ссылку file4 на file1.
Посмотреть, какие айноды у файлов. Удалить file1. Что стало с остальными созданными файлами? Попробовать вывести их на экран.  
2)Дать созданным файлам другие, произвольные имена. Создать новую символическую ссылку. Переместить ссылки в другую директорию. Создать два произвольных файла.
Первому присвоить права на чтение, запись для владельца и группы, только на чтение — для всех. Второму присвоить права на чтение, запись — только для владельца. 
Сделать это в численном и символьном виде.  
3)Создать пользователя, обладающего возможностью выполнять действия от имени суперпользователя.  
\* Создать группу developer и несколько пользователей, входящих в нее. Создать директорию для совместной работы. Сделать так, чтобы созданные одними пользователями файлы 
могли изменять другие пользователи этой группы.  
\* Создать в директории для совместной работы поддиректорию для обмена файлами, но чтобы удалять файлы могли только их создатели.  
\* Создать директорию, в которой есть несколько файлов. Сделать так, чтобы открыть файлы можно было, только зная имя файла, а через ls список файлов посмотреть было нельзя.
</details>  

4. [Задание №4 - Bash, скрипты и автоматизация](https://github.com/Alexei-T/geek/tree/master/4)    
<details><summary>Описание задания №4</summary>  
 
1)Написать скрипт, который удаляет из текстового файла пустые строки и заменяет маленькие символы на большие (воспользуйтесь tr или sed).  
2)Создать скрипт, который создаст директории для нескольких годов (2010 — 2017), в них — поддиректории для месяцев (от 01 до 12), и в каждый из них запишет несколько 
файлов с произвольными записями (например, 001.txt, содержащий текст«Файл 001», 002.txt с текстом Файл 002) и т. д.  
\* Создать файл crontab, который ежедневно регистрирует занятое каждым пользователем дисковое пространство в его домашней директории.  
\* Создать скрипт ownersort.sh, который в заданной папке копирует файлы в директории, названные по имени владельца каждого файла. Учтите, что файл должен принадлежать 
соответствующему владельцу.

</details>

5. [Задание №5 - Сетевые возможности Linux](https://github.com/Alexei-T/geek/tree/master/5)    
<details><summary>Описание задания №5</summary>  
 
1)Произвести ручную настройку сети в Ubuntu используя netplan.  
\* Настроить правила iptables, чтобы из внешней сети можно было обратиться только к портам 80 и 443. Запросы на порт 8080 перенаправлять на порт 80.  
\* Дополнительно к предыдущему заданию настроить доступ по ssh только из указанной сети.

</details>

6. [Задание №6 - Регистрация сервера в облаке](https://github.com/Alexei-T/geek/tree/master/6)    
<details><summary>Описание задания №6</summary>  
 
1)Настроить виртуальный сервер в облаке (GCP, AWS, VDS и др.) с публичным IP-адресом.  
2)Зарегистрировать свой домен через freenom.com.  
\* Настроить фаервол, чтобы был доступ только к сервисам http и ssh.  
\* Установить веб-сервер Nginx и подключиться к нему — прислать скриншот.  
\* Передать управление NS-записями на cloudflare.com 

</details>

7. [Задание №7 - Запускаем веб-сервер](https://github.com/Alexei-T/geek/tree/master/7)    
<details><summary>Описание задания №7</summary>  
 
1)Установить Apache2. Прислать скриншоты работающего сервера.    
\* Установить Nginx и настроить его на работу с php-fpm.  
\* Настроить Nginx в качестве балансировщика. Используя mod_upstream, раскидывать весь входящий трафик по трем Apache2-серверам, находящимся в локальной сети. 

</details>

8. [Задание №8 - Как защитить свой сервер](https://github.com/Alexei-T/geek/tree/master/8)    
<details><summary>Описание задания №7</summary>  
 
1)Настроить сетевой фильтр, чтобы из внешней сети можно было обратиться только к сервисам http и ssh (80 и 22).  
2)Запросы, идущие на порт 8080, перенаправлять на порт 80.    
3)Настроить доступ по ssh только для вашего IP-адреса (или из всей сети вашего провайдера).    
4.* Создать нового пользователя, сгенерировать для него новые сертификаты. Настроить доступ на сервер вновь созданного пользователя с использованием сертификатов. Подключиться с помощью putty или ssh без ввода пароля (используя только сертификат). Примечание: сертификат может быть подготовлен как в Ubuntu, так и с помощью puttygen в windows.  
5.* Ваши коллеги, студенты, настраивали VDS-сервер для использования на командном проекте. Через некоторое время сервер был заблокирован. Студенты связались с хостером,
он предоставил abuse-письмо (настоящий IP-адрес машины студентов был заменен на 203.0.113.198)
В качестве тренажера вам будет предложен образ машины: один чистый, второй зараженный. Образ зараженной машины — тренажер, он содержит деактивированное ПО,
лишенное настоящей активности, но в него добавлены компоненты, имитирующие ее. IP-адрес с белого (в письме он обозначен как 203.0.113.198) заменен на адрес в 10.0.0.0/8
или 192.168.0.0/24 сети. Вам необходимо создать виртуальную машину и прикрепить виртуальный жесткий диск с, возможно, зараженной ОС.
В качестве практического задания вы сдаете файл doc / pdf / google doc, в котором описываете, какими командами и что вы проверяли, какие активности были обнаружены
и что вы предприняли и рекомендуете сделать, чтобы через некоторое время машину не заблокировали снова.
Ссылка на образ жесткого диска (использовалась версия Virtual Box 6.0): ****

</details>
<p align=center><a href="#top">🡡 Вернуться к оглавлению</a>
