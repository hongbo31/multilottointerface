from MultilottoServiceInterface.userService.login import Login


class Deposit(Login):

    lg = Login("login_by_account")

    def deposit_service(self):
        return self.lg.login_cookie_service("getdeposit")


if __name__ == '__main__':
    dp = Deposit("getdeposit")
    print(dp.deposit_service())
