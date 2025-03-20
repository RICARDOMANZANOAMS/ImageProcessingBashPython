
export PROJECT_PATH="/RICARDO/personal/ImageProcessingBashPython"  #Define project path
WSL_PROJECT_PATH=$(wslpath "$PROJECT_PATH")  #Transform path to wsl path 
echo $WSL_PROJECT_PATH

jsonFile=$WSL_PROJECT_PATH/config/config.json  #Path to config file

jq -c '.[]' $jsonFile | while read -r item; do
    echo $item | jq -c '.[]' | while read -r item2; do
        echo $item2
        keys=$(echo "$item2" | jq -r 'keys_unsorted[]')
        echo $keys
        for key in $keys; do
            enabled_value=$(echo "$item2" | jq -r --arg key "$key" '.[$key].enabled')
            
            if [ "$enabled_value" = "true" ]; then
                echo "true value"
                python3 /mnt/c/Ricardo/personal/ImageProcessingBashPython/src/test.py "$key"                
            else
                echo "false value"
            fi
        done
       
    done
done
