import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(kit_name):
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json().get("authToken")

    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name


def negative_assert_code_400(kit_name):
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json().get("authToken")

    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_response.status_code == 400


def negative_assert_no_name():
    user_body = data.user_body
    user_response = sender_stand_request.post_new_user(user_body)
    auth_token = user_response.json().get("authToken")

    kit_body = {}
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400


#Bloque de pruebas

#Prueba1
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


#Prueba2
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


#Prueba4
def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert_code_400(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

#Prueba3
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400("")

#Prueba5
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert('"№%@",')

#Prueba6
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" A Aaa ")

#Prueba7
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")

# Prueba8
def test_create_kit_no_name_get_error_response():
    negative_assert_no_name()

#Prueba9
def test_create_kit_number_type_name_get_error_response():
    negative_assert_code_400(123)

