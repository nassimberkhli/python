from hash import my_hash
from choose_login import choose_login

login_chosen = choose_login()

while my_hash(login_chosen) != 'q':

    login_chosen = choose_login()
