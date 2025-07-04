import streamlit_authenticator as stauth

print(stauth.Hasher(['cvd123']).generate())
