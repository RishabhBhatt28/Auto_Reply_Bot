import pyautogui
import time
import pyperclip
import re
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

def is_last_message_from_sender(chat_text, sender_name="Pradeep Kumar"):
    """
    Function to get the sender of the last message in the chat history.
    """
    messages = chat_text.strip().split("/2025]")[-1]
    if sender_name in messages:
        return True
    return False


# Wait for a moment to switch to the required screen
time.sleep(0)

# Click on the icon at 
pyautogui.click(990, 735)
time.sleep(1)  # Wait for the application to open

# Drag to select the text
pyautogui.moveTo(543, 245)
pyautogui.mouseDown()
pyautogui.moveTo(923, 651, duration=1)
pyautogui.mouseUp()

# Copy the selected text to clipboard
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)  # Allow some time for copying

# Click in the input field (optional)
pyautogui.click(1162, 202)

# Retrieve copied text from clipboard
copied_text = pyperclip.paste()
print("Copied Text:", copied_text)

# Generate response using OpenAI API
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": "You are a person named Rishabh who speaks Hindi,English. You are from India and you are a college student. You analyze chat history and respond like Rishabh. **Output should be only the next chat response as Rishabh, without timestamps, your name, or metadata. Only reply with the actual message**."},
        {"role": "user", "content": copied_text}
    ]
)

# Extract only the message content
response_text = completion.choices[0].message.content

# **Remove timestamps like [11:05 pm, 03/03/2025]**
clean_response = re.sub(r"\[\d{1,2}:\d{1,2} (?:am|pm), \d{2}/\d{2}/\d{4}\]", "", response_text).strip()

# **Remove "Rishabh Bhatt:" or similar name references**
clean_response = re.sub(r"\bRishabh Bhatt\b[:,]*", "", clean_response).strip()
clean_response = re.sub(r"\bRishabh\b[:,]*", "", clean_response).strip()  # Handles cases where only "Rishabh" appears

print("Generated Response:", clean_response)  # For debugging

# Copy the cleaned response to clipboard
pyperclip.copy(clean_response)

# Click at (594, 687) (Chatbox)
pyautogui.click(594, 687)
time.sleep(1)

# Paste the copied response
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# Press Enter to send the message
pyautogui.press('enter')

print("Message sent successfully!")


























