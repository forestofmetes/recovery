poetry add openai streamlit

pip freeze > requirements.txt

mkdir .streamlit
echo 'API_KEY=""' > .streamlit/secrets.toml
