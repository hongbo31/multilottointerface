from MultilottoServiceInterface.userService.login import Login

class GetPaymentMethods(Login):

    lg = Login('login_by_account')

    def getpaymentmethods_service(self):
        return self.lg.login_cookie_service("getpaymentmethods")

if __name__ == '__main__':

    gp = GetPaymentMethods('getpaymentmethods')
    print(gp.getpaymentmethods_service())