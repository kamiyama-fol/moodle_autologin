#/usr/bin/python

"""
京都産業大学のmoodleに自動でログインするスクリプト
"""
__version__ = "3.10.8"
__author__ = "UEYAMA Koki"


 # .env ファイルを読み込む

def main():
    #webdriverの下準備
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    


    #moodleのログインURLを取得
    from dotenv import load_dotenv
    import os
    load_dotenv()
    moodle_url=os.getenv("MOODLE_URL")
    driver.get(moodle_url)

    #学認システムへ移動&認証方式を選択
    from selenium.webdriver.common.by import By
    auth_select = driver.find_element(By.NAME,'auth')
    auth_select.send_keys("login")
    auth_select.submit()

    #ユーザidを入力してログイン
    user_id_form = driver.find_element(By.NAME, 'username')
    login_user_id = os.getenv("LOGIN_USER_ID")
    user_id_form.send_keys(login_user_id)
    password_form = driver.find_element(By.NAME, 'password')
    login_password = os.getenv("LOGIN_PASSWORD")
    password_form.send_keys(login_password)
    user_id_form.submit()

    if driver.current_url != "https://cclms.kyoto-su.ac.jp/my/":
        #ワンタイムパスワードを選択
        onetime_select = driver.find_element(By.NAME, "auth")
        onetime_select.send_keys("allotplogin")
        onetime_select.submit()

        #ワンタイムパスワードの入力
        onetime_form = driver.find_element(By.NAME, 'password')
        login_totp_key = os.getenv("LOGIN_TOTP_KEY")
        import pyotp
        one_time_password = pyotp.TOTP(login_totp_key).now()
        onetime_form.send_keys(one_time_password)
        print(one_time_password)
        onetime_form.submit()
        # ブラウザが自動で閉じないようにする
    input("テストが完了したら Enter を押してください...")
    return 0

def 

if __name__ == '__main__':
    import doctest
    doctest.testmod

    import sys
    sys.exit(main())