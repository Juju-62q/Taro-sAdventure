for port in 23 25 53 70 80 110 119 143
do
  echo "$port port"
  telnet $1 $port
done
