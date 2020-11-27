# <p align=center> **ДЗ по курсу Факультет Devops**
1. [Введение в UNIX-системы](#ux1)

## <p align=center> Введение в UNIX-системы <a name="ux1"></a>
1. [Задание №1 - Знакомство с UNIX/Linux](https://github.com/Alexei-T/geek/tree/master/1)
<details><summary>Описание задания</summary>  
1)Установить Virtualbox или VMWare Player, установить виртуальную машину с Ubuntu.      
2)Разобраться, что такое bash, используя справочные системы.      
3)Разобраться, как копировать и удалять файлы.      
\* Установить mc и openssh-server.      
\* Если вы работаете в Windows, установить PuTTY для подключения к виртуальной машине по ssh и подключиться.    
</details>    
2. [Задание №2 - Работа в консоли](https://github.com/Alexei-T/geek/tree/master/2)    
  
<details><summary>Описание задания</summary>  
1)Просмотреть содержимое директорий /etc, /proc, /home. Посмотреть пару произвольных файлов в /etc.        
2)Выяснить, для чего предназначена команда cat. Используя данную команду, создать два файла с данными, а затем объединить их. Просмотреть содержимое созданного файла.   Переименовать файл, дав ему новое имя.    
3)Создать несколько файлов. Создать директорию, переместить файл туда. Удалить все созданные в этом и предыдущем задании директории и файлы. В ОС Linux скрытыми файлами считаются те, имена которых начинаются с символа “.”. Сколько скрытых файлов в вашем домашнем каталоге? (Использовать конвейер. Подсказка: для подсчета количества строк можно использовать wc.)      
4)Попробовать вывести с помощью cat содержимое всех файлов в директории /etc. Направить ошибки в отдельный файл в вашей домашней директории. Сколько файлов, которые не удалось посмотреть, оказалось в списке?    
5)Запустить в одном терминале программу, а в другом терминале посмотреть PID процесса и остановить с помощью kill, посылая разные типы сигналов. Что происходит?     
\* Полезное задание на конвейер. Использовать команду cut на вывод длинного списка каталога, чтобы отобразить только права доступа к файлам. Затем отправить в конвейере этот вывод на sort и uniq, чтобы отфильтровать все повторяющиеся строки. Потом с помощью wc подсчитать различные типы разрешений в этом каталоге. Самостоятельно решить задачу, как сделать так, чтобы в подсчет не добавлялись строка «Итого» и файлы . и .. (ссылки на текущую и родительскую директории).
  </details>    
3. [Задание №3 - Права и пользователи в UNIX](https://github.com/Alexei-T/geek/tree/master/3)  
<details><summary>Описание задания</summary>  
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
