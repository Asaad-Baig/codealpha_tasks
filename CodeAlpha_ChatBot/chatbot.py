def get_chatbot_response(user_input):
    """
    Analyzes the user's input using if-elif logic and returns a predefined reply.
    Converts input to lowercase to handle variations in casing.
    """
    # Clean the input by stripping whitespace and converting to lowercase
    processed_input = user_input.strip().lower()
    
    # Rule-based conditional responses
    if "hello" in processed_input or "hi" in processed_input:
        return "Hi! How can I help you today?"
        
    elif "how are you" in processed_input:
        return "I'm fine, thanks! How are things on your end?"
        
    elif "what is your name" in processed_input:
        return "I'm an automated rule-based chatbot."
        
    elif "bye" in processed_input or "quit" in processed_input:
        return "Goodbye! Have a great day!"
        
    else:
        return "I'm sorry, I don't understand that command. Try saying 'hello', 'how are you', or 'bye'."


def run_chatbot():
    """
    Main execution function that handles the loop and basic input/output interaction.
    """
    print("==================================================")
    print("  Chatbot Initialized. Type 'bye' to exit.        ")
    print("==================================================")
    
    # Infinite loop to keep the conversation going until an exit keyword is parsed
    while True:
        # Standard input from the user
        user_message = input("You: ")
        
        # Fetch the predefined reply from the response function
        bot_reply = get_chatbot_response(user_message)
        
        # Standard output showing the chatbot's response
        print(f"Chatbot: {bot_reply}\n")
        
        # Terminate the loop if the user says goodbye
        if "bye" in user_message.lower() or "quit" in user_message.lower():
            print("--- Session Ended ---")
            break


if __name__ == "__main__":
    # Start the chatbot application
    run_chatbot()