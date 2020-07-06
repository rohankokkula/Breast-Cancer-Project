mkdir -p ~/.streamlit/


echo “\
[general]\n\
email = \”dannylee1020@gmail.com\”\n\
“ > ~/.streamlit/credentials.toml


echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml






# echo “\
# [server]\n\
# headless = true\n\
# enableCORS=false\n\
# port = $PORT\n\
# “ > ~/.streamlit/config.toml