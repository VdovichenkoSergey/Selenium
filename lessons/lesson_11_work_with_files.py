import json

# reg_data = {
#             'first_name': 'Sergey14',
#             'last_name': 'Anatolich14',
#             'email': 'test@test.com14',
#             'phone': '+380981234580',
#             'password': '1234'
#         }
#
# with open('reg_data.txt', 'w', encoding="utf-8") as file:
#     json.dump(reg_data, file)


with open('../../Docker_test/data/reg_data.txt', 'r', encoding="utf-8") as file:
    reg_data = json.load(file)

    print(reg_data)