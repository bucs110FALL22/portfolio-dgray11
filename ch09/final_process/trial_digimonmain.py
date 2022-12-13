import random 
import trial_digimonAPI

def main():
    
    tapi = trial_digimonAPI.trial_digimonAPI()
    results = tapi.get()
    # picture = [f'img']
    #print(f'img')
    print(results)
    # print(f"{['img']} \n-- Please select the correct answer:\n===")
  
    # for trivia in results:
    #     #combine the incorrect and corrects into a single array
    #     answers = trivia['incorrect_answers'] + [trivia['correct_answer']]
        
    #     print(f"{trivia['question']} \n-- Please select the correct answer:\n===")
        
    #     #enumerate(): returns a tuple of the index and the value for each list item
    #     #display all possible answers
    #     for i, a in enumerate(answers):
    #         print(f"{i}){a}")

main()