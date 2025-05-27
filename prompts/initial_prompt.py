def create_inheritance_prompt(user_data):
    """Create a detailed prompt for inheritance analysis based on user data"""
    
    return f"""
    Please analyze the inheritance situation for the following person:
    
    Name: {user_data['name']}
    
    Current Location:
    - Country: {user_data['user_location']['country']}
    - State/Province: {user_data['user_location']['state_province']}
    - City: {user_data['user_location']['city']}
    
    Parents' Location:
    - Country: {user_data['parents_location']['country']}
    - State/Province: {user_data['parents_location']['state_province']}
    - City: {user_data['parents_location']['city']}
    
    Additional Information:
    - Parents have a will: {'Yes' if user_data['parents_have_will'] else 'No'}
    - User is executor: {'Yes' if user_data['is_executor'] else 'No'}
    
    Please provide detailed guidance on how their inheritance will work.
    """ 