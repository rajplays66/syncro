# ============================================
# SIMPLE AI CHATBOT FOR ACODE APP
# ============================================
# Copy ALL this code into ACode and run

import random
import datetime
import json
import os

class ACodeChatbot:
    def __init__(self, name="Neuro"):
        self.name = name
        self.user_name = ""
        self.memory_file = "chatbot_memory.json"
        self.load_memory()
        
        print("🤖" * 20)
        print(f"      {self.name} AI CHATBOT")
        print("🤖" * 20)
        print("\nType 'bye' to exit, 'help' for commands")
        print("=" * 40)
    
    def load_memory(self):
        """Load previous conversations"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    data = json.load(f)
                    self.user_name = data.get("user_name", "")
                    print(f"Welcome back, {self.user_name}!" if self.user_name else "")
            except:
                self.user_name = ""
        else:
            self.user_name = ""
    
    def save_memory(self):
        """Save user info"""
        data = {"user_name": self.user_name}
        with open(self.memory_file, 'w') as f:
            json.dump(data, f)
    
    def respond(self, user_input):
        """Generate response to user input"""
        user_input = user_input.lower().strip()
        
        # Exit command
        if user_input in ['bye', 'exit', 'quit', 'goodbye']:
            self.save_memory()
            return "Goodbye! 👋 Thanks for chatting!"
        
        # Help command
        if user_input == 'help':
            return """📋 **AVAILABLE COMMANDS:**
• help - Show this help
• joke - Tell a joke
• time - Current time
• date - Today's date
• clear - Clear screen
• facts - Show interesting facts
• game - Play a game
• about - About this bot
• bye - Exit chatbot"""
        
        # Clear screen
        if user_input == 'clear':
            print("\n" * 50)
            return "Screen cleared! 🧹"
        
        # Tell joke
        if 'joke' in user_input:
            jokes = [
                "🤖 Why do programmers prefer dark mode? Because light attracts bugs!",
                "💻 Why was the computer cold? It left its Windows open!",
                "🐍 Why do Python programmers prefer snakes? Because they love Python!",
                "📱 Why did the smartphone go to therapy? It had too many issues!",
                "🌮 What do you call a fake noodle? An impasta!"
            ]
            return random.choice(jokes)
        
        # Time
        if 'time' in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"🕐 Current time: {current_time}"
        
        # Date
        if 'date' in user_input:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            return f"📅 Today is: {current_date}"
        
        # User name
        if 'my name is' in user_input:
            name = user_input.replace('my name is', '').strip().title()
            if name:
                self.user_name = name
                self.save_memory()
                return f"👋 Nice to meet you, {self.user_name}! I'll remember that."
        
        # Ask for name
        if 'your name' in user_input:
            return f"I'm {self.name}, your AI assistant! 🤖"
        
        # Greetings
        if any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
            if self.user_name:
                return f"Hello {self.user_name}! 😊 How can I help you today?"
            return "Hello! 👋 What's your name?"
        
        # How are you
        if 'how are you' in user_input:
            feelings = ["I'm great! Powered by Python! 🐍", 
                       "Awesome! Ready to help!", 
                       "Doing well! Learning from you!"]
            return random.choice(feelings)
        
        # Thank you
        if 'thank' in user_input:
            return "You're welcome! 😊 Happy to help!"
        
        # About
        if 'about' in user_input:
            return f"""ℹ️ **ABOUT {self.name}:**
• Created with Python 🐍
• Running on ACode App 📱
• Version 1.0
• Developer: You! 🎉"""
        
        # Game
        if 'game' in user_input:
            return "🎮 Let's play! Try guessing:\nI'm thinking of a number 1-10. Guess it!"
        
        # Facts
        if 'fact' in user_input:
            facts = [
                "💡 Honey never spoils. Archaeologists have found 3000-year-old honey!",
                "🐙 Octopuses have three hearts!",
                "🌌 A day on Venus is longer than a year on Venus!",
                "📱 Your smartphone has more computing power than Apollo 11!",
                "🐜 Ants never sleep!"
            ]
            return random.choice(facts)
        
        # Weather (simulated)
        if 'weather' in user_input:
            weather_types = ["sunny ☀️", "rainy 🌧️", "cloudy ☁️", "snowy ❄️", "windy 💨"]
            temp = random.randint(15, 35)
            return f"🌤️ Today's weather: {random.choice(weather_types)}, {temp}°C"
        
        # Math
        if 'calculate' in user_input or '+' in user_input or '-' in user_input or '*' in user_input:
            try:
                # Simple calculation
                if '+' in user_input:
                    nums = user_input.split('+')
                    if len(nums) == 2:
                        result = float(nums[0].strip()) + float(nums[1].strip())
                        return f"🧮 Result: {result}"
                elif '-' in user_input:
                    nums = user_input.split('-')
                    if len(nums) == 2:
                        result = float(nums[0].strip()) - float(nums[1].strip())
                        return f"🧮 Result: {result}"
                elif '*' in user_input or 'x' in user_input:
                    nums = user_input.replace('x', '*').split('*')
                    if len(nums) == 2:
                        result = float(nums[0].strip()) * float(nums[1].strip())
                        return f"🧮 Result: {result}"
            except:
                pass
        
        # Love/relationship
        if any(word in user_input for word in ['love', 'like you', 'crush']):
            return "💖 I'm an AI, but I appreciate your friendship!"
        
        # Default responses
        responses = [
            "🤔 That's interesting! Tell me more.",
            "😊 I see! What else would you like to know?",
            "🎯 Cool! Want to play a game? Type 'game'",
            "📚 Need help? Type 'help' for commands",
            "💭 Hmm... can you explain that differently?",
            "🌟 Interesting thought!",
            f"🔍 {self.user_name}, could you elaborate?" if self.user_name else "🔍 Could you elaborate?"
        ]
        
        return random.choice(responses)

# ============================================
# MAIN CHAT LOOP
# ============================================
def main():
    # Create chatbot
    bot = ACodeChatbot("NeuroAI")
    
    # Chat history
    history = []
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
            
            # Add to history
            history.append(f"You: {user_input}")
            
            # Get response
            response = bot.respond(user_input)
            
            # Add bot response to history
            history.append(f"{bot.name}: {response}")
            
            # Print response
            print(f"\n🤖 {bot.name}: {response}")
            
            # Check if user wants to exit
            if user_input.lower() in ['bye', 'exit', 'quit']:
                print("\n" + "=" * 40)
                print("📝 CHAT HISTORY (last 5 messages):")
                print("-" * 40)
                for msg in history[-10:]:  # Show last 10 messages
                    print(msg)
                print("=" * 40)
                print("Thanks for using ACode Chatbot! 🎉")
                break
            
        except KeyboardInterrupt:
            print(f"\n\n{bot.name}: Oops! Interrupted. Goodbye! 👋")
            break
        except Exception as e:
            print(f"\n{bot.name}: Error: {str(e)}")
            print("Let's continue chatting!")

# ============================================
# RUN THE CHATBOT
# ============================================
if __name__ == "__main__":
    # Clear screen
    print("\n" * 3)
    
    # Welcome message
    print("🚀 Starting ACode AI Chatbot...")
    print("📱 Running on Android with Python")
    
    # Run main function
    main()