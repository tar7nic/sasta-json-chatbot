import json
from difflib import get_close_matches
 
def load_kb(file_path:str) -> dict: # string file path jo dictionary return karegi
    with open(file_path,'r') as file:  
        data: dict = json.load(file)
    return data

def save_kb(file_path: str, data : dict): 
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
def find_best_match(user_ques:str, questions:list[str]) -> str | None: 
    matches : list = get_close_matches(user_ques, questions, n=1, cutoff=0.6)    # n=1 is for the best answer possible, we can use n=2 or 3 for multiple best answers, and cutoff is for 0.6 = 60% accurate answers       
    return matches[0] if matches else None

def get_ans_for_ques(question: str, kb : dict) -> str | None:
    for q in kb["questions"]:
        if q["question"] == question:
            return q["answer"]
      
def cb():
    knowledge_base : dict = load_kb('C:\\Users\\Asus\\OneDrive\\Documents\\VSC\\output\\.vscode\\Jupyter\\knowledegbase.json')
    
    while True:   # it will continue iterating indefinitely until a break condition is encountered or until the program is interrupted
        user_ip : str = input('You: ')
        
        if user_ip.lower() == 'quit':
            break
        
        best_match : str | None = find_best_match(user_ip, [q["question"] for q in knowledge_base["questions"]])
        if best_match:
            answer: str = get_ans_for_ques(best_match, knowledge_base)
            print(f'bot: {answer}')
        else:
            print(f'bot: I don\'t know the answer. Can you teach me?-' )
            new_answer : str = input('You: Type the answer or "skip" to skip- ')
            
            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question":user_ip, "answer":new_answer})
                save_kb('C:\\Users\\Asus\\OneDrive\\Documents\\VSC\\output\\.vscode\\Jupyter\\knowledegbase.json', knowledge_base)
                print('bot: Thankyou! I learned a new response!')
                
if __name__ == '__main__':
    cb()