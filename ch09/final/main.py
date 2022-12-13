import digimonAPI #Proxy Class
import coffeeAPI #2nd Proxy Class

def main():
    #Proxy Class
  api = digimonAPI.digimonAPI() #()
  results = api.get()
  for i in results:
    print(i['img'] + "What digimon is this?")

    user_input = int(input(":"))
    answer = i['name']
    if answer[user_input] == i['name']:
        print("correct!")
      
  
        capi = coffeeAPI.coffeeAPI()
        results = capi.get()
        for i in results:
            print(['file'] + "this is the FILE")
      
    else:
        print(f"The correct answer is: {i['name']}")



# for i in results:
#     answer = i['name']
#     print(i['name'] + "this is the NAME")

#     user_input = int(input(":"))
#     if answer[user_input] == i['name']:
#         print("correct!")

  
  



  
  
    # results = gomi.get()
    # for trivia in results:
    #   answers = trivia['name']
    #   print(f"{trivia['name']} \n-- Please select the correct answer:\n===")
     
    # # for i, a in enumerate(answers):
    # #     print(f"{i}){a}")

    #     #ask the user for their choice
    # choice = int(input(":"))
    # if answers[choice] == trivia['name']:
    #         print("correct")
    # else:
    #         print(f"Actually, {trivia['name']}")

main()