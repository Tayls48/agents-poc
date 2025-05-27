from agents import Agent, ModelSettings, function_tool, Runner
from dotenv import load_dotenv
from users import users  # Import our users data
from prompts.initial_prompt import create_inheritance_prompt
from models.inheritance_risk_output import inheritance_risk_output
import os
from pathlib import Path

# Load environment variables
load_dotenv()

# ------------------------------------------------------------
# Prompt Utilities
# ------------------------------------------------------------
def load_prompt(prompt_name):
    """
    Load a prompt from the prompts directory.
    
    Args:
        prompt_name (str): Name of the prompt file (without extension)
        
    Returns:
        str: The contents of the prompt file
        
    Raises:
        FileNotFoundError: If the prompt file doesn't exist
        Exception: For other file reading errors
    """
    prompt_path = Path(__file__).parent / 'prompts' / f"{prompt_name}.md"
    try:
        with open(prompt_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
    except Exception as e:
        raise Exception(f"Error loading prompt file: {str(e)}")

# ------------------------------------------------------------
# Agent Setup
# ------------------------------------------------------------
# Load the prompts
education_prompt = load_prompt('teacher_prompt')
tax_prompt = load_prompt('tax_prompt')

# ------------------------------------------------------------
# Agent Definition
# ------------------------------------------------------------
education_agent = Agent(
    name="Kliro - Education Agent",
    instructions=education_prompt,
    model="gpt-4",  
)

tax_agent = Agent(
    name="Kliro - Tax Agent",
    instructions=tax_prompt,
    model="gpt-4",
    output_type=inheritance_risk_output
)

# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------
def analyze_inheritance(user_id):
    """Analyze inheritance situation for a specific user"""
    if user_id not in users:
        return "User not found"
    
    user_data = users[user_id]
    prompt = create_inheritance_prompt(user_data)
    
    result = Runner.run_sync(education_agent, prompt)
    return result.final_output

def analyze_tax(user_id):
    """Analyze tax implications for a specific user"""
    if user_id not in users:
        return "User not found"
    
    user_data = users[user_id]
    prompt = create_inheritance_prompt(user_data)
    
    result = Runner.run_sync(tax_agent, prompt)
    return result.final_output

def main():
    # Example: Analyze inheritance for user1 (Nick)
    user_id = "user1"  # You can change this to test different users
    print(f"\nAnalyzing inheritance situation for {users[user_id]['name']}...")
    print("\n" + "="*50 + "\n")
    
    # Get education analysis
    education_analysis = analyze_inheritance(user_id)
    print("Education Analysis:")
    print(education_analysis)
    
    print("\n" + "="*50 + "\n")
    
    # Get tax analysis
    tax_analysis = analyze_tax(user_id)
    print("Tax Analysis:")
    print(tax_analysis)

if __name__ == "__main__":
    main()
