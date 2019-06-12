from MultilottoServiceInterface.BaseService import BaseService


class GetVaildCountries(BaseService):

    def getvaildcountries_service(self, reslut_type_is_str=False):
        result = self.request_service(reslut_type_is_str)
        return result


if __name__ == '__main__':
    vaildcountrt = GetVaildCountries("getvalidcountries")
    print(vaildcountrt.getvaildcountries_service())
    print(vaildcountrt.case_name)