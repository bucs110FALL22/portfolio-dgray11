import random 
import DisneyAPI #Proxy Class

def main():
    #Proxy Class
    dapi = DisneyAPI.DisneyAPI()
    print(f"{dapi['imageUrl']} this is the image url")
  
main()





    # Capi = CoffeeAPI.CoffeeAPI()
    # results = Capi.get()
  
    # for dadjoke in results:
    #   #print
    #   answers = dadjoke['text']
        
    #     print(f"{dadjoke['text']} \n-- Please select the correct answer:\n===")
        
    #     choice = int(input(":"))
    #     if answers[choice] == dadjoke['correct_answer']:
    #         print("correct, I guess.")
    #     else:
    #         print(f"Actually, {dadjoke['correct_answer']}")
