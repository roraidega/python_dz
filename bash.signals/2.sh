# напишите скрипт который раз в 5 секунд выводит надпись "я все еще тут"
# если нажать ctrl+c выводится надпись "ты меня не остановишь"
# спустя 10 если нажать ctrl+c выводится надпись "так уж и быть"
# запустите скрипт в фоновом режиме

# запуск в фоновом режиме ./1.sh &


#!/bin/bash

trap "echo 'Ты меня не остановишь'" SIGINT

echo "Скрипт запущен. Чтобы остановить, нажмите Ctrl+C."

count=0

while true; do
  sleep 5
  echo "Я все еще тут"
  count=$((count + 5))

  if [ $count -ge 10 ]; then
    trap "echo 'Так уж и быть'; exit 0" SIGINT
  fi
done

