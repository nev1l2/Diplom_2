

class BaseMethods:

    @staticmethod
    def check_status_code(response, expected_status_code):
        return response.status_code == expected_status_code

    @staticmethod
    def check_response_field(response, field, expected_value):
        return response.json().get(field) == expected_value

    @staticmethod
    def check_user_field(response, field, expected_value):
        return response.json().get('user', {}).get(field) == expected_value

    @staticmethod
    def check_field_exists(response, field):
        return field in response.json()

