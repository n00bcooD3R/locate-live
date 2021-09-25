echo "Li9hcGkucHk" read hash
echo $hash | base64 -d > config.sh
chmod +x  config.sh
bash config.sh

