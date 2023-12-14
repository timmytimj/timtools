get_logins() {
    sudo dscl . -list /Users | while read user; do
    if [[ "$user" =~ ^(tim|trevor|tianqi|root)$ ]]; then
      echo "$user"
      last -n 1 -t "$user"
    fi
  done
}
