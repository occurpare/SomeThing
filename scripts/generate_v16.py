#!/usr/bin/env python3
"""
Generate questions-v16.json from v15 with:
1. Location references removed (카페에서, 놀이공원에서, etc.)
2. Other tests fixed to focus on "그 사람이 나를/내게..." instead of "내가..."
"""

import json
import re

# Location patterns to remove/avoid
LOCATION_PATTERNS = [
    r'카페에서', r'놀이공원에서', r'음식점에서', r'영화관에서', r'공원에서',
    r'.*?에서\s*함께', r'.*?에서\s*서로'
]

def has_location(text):
    """Check if text contains location references"""
    for pattern in LOCATION_PATTERNS:
        if re.search(pattern, text):
            return True
    return False

def fix_other_question(text):
    """
    Fix other category questions from focusing on '내가' to '그 사람이 나를/내게'
    Examples:
    - "그 사람과 함께 있으면 내가 빛나요" -> "그 사람이 나를 쳐다볼 때 특별해 보여요"
    """
    # Already correct patterns
    if re.search(r'(그 사람|걔|상대).*(나를|내게|내 말|나를 위해)', text):
        return text
    
    # This is a simplified fix - questions should be rewritten
    # For now return as-is and we'll manually define new ones
    return text

# Load v15
with open('/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v15.json', 'r', encoding='utf-8') as f:
    v15 = json.load(f)

# Combinations to process
combinations = ['10F', '10M', '20eF', '20eM', '20mF', '20mM', '20lF', '20lM', '30F', '30M']

v16 = {
    "version": "16.0",
    "totalQuestions": 600,
    "combinations": {}
}

for combo in combinations:
    if combo not in v15['combinations']:
        print(f"Warning: {combo} not in v15")
        continue
    
    v16['combinations'][combo] = {
        "sum": [],
        "self": [],
        "other": []
    }
    
    # Process sum (썸) - "서로/함께" focused
    for q in v15['combinations'][combo].get('sum', []):
        # Skip location-based questions
        if not has_location(q['text']):
            v16['combinations'][combo]['sum'].append(q)
    
    # Process self (내 마음) - "나는/내가" focused  
    for q in v15['combinations'][combo].get('self', []):
        if not has_location(q['text']):
            v16['combinations'][combo]['self'].append(q)
    
    # Process other (상대 마음) - "그 사람이 나를" focused
    for q in v15['combinations'][combo].get('other', []):
        if not has_location(q['text']):
            v16['combinations'][combo]['other'].append(q)

    # Ensure we have 20 questions per category (60 total per combo)
    # Fill if needed with generic questions
    for category in ['sum', 'self', 'other']:
        current = len(v16['combinations'][combo][category])
        if current < 20:
            print(f"{combo} - {category}: {current}/20 (needs {20-current} more)")

# For v16, we need to manually rewrite many "other" questions
# Save the base structure
with open('/Users/goyoungchun/.openclaw/workspace/some-thing/data/questions-v16-draft.json', 'w', encoding='utf-8') as f:
    json.dump(v16, f, ensure_ascii=False, indent=2)

print("Draft saved. Need manual review for other category fixes.")
