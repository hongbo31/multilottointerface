from MultilottoServiceInterface.BaseService import BaseService


class GetCountryIdByIp(BaseService):

    def getcountryidbyip_service(self, result_type_is_str=False):
        result = self.request_service(result_type_is_str)
        return result


if __name__ == '__main__':
    getidbyip = GetCountryIdByIp("getvalidcountries")
    print(getidbyip.getcountryidbyip_service())
