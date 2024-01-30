import datetime
import asyncio
from telegram import Bot
from telegram.error import TelegramError
import os

async def send_photo_and_text():
    # Get the current time
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")


    # Telegram Bot settings
    telegram_bot_token = "6217190311:AAEXlWT8dokgVHXS9L9rUTWhyouXACEMkyM"
    telegram_group_chat_id = -4180046777  # Replace with your actual group chat ID

    # Initialize the Telegram bot
    bot = Bot(token=telegram_bot_token)

    
    
    try:
            message_text = f"Last updated on {formatted_time}"
            
            captions = {
                "Daily_Trend.jpg": "Blood Donation Daily Trend",
                "Age_Generations_Donors_2023.jpg": "2023 New Donors Based on Age Range",
                "Age_Generations_Donors_2024.jpg": "2024 New Donors Based on Age Range",
                "Blood_Donor_Generation.jpg": "Blood Donors Based on Generation",
                "Blood_Type_And_Social_Group.jpg": "Highest Blood Group and Highest Social Group",
                "Regularity_Voluntary_Donors.jpg": "Donation Regularity in 2023",
            }

            figure_folder_path = "./Figures/"
            
            # Upload photo for all figures in folder
            if not os.path.exists(figure_folder_path):
                print(f"The folder '{figure_folder_path}' does not exist.")
            else:
                # List all files in the folder
                image_list = [f for f in os.listdir(figure_folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

            
            for filename in image_list:
                caption = captions.get(filename, "No caption available")
                photo_path = os.path.join(figure_folder_path, filename)# Replace with the path to your photo
                photo_response = await bot.send_photo(chat_id=telegram_group_chat_id, photo=open(photo_path, "rb"), caption=caption)

            # Check the response for sending the photo
            if photo_response and photo_response.message_id:
                print("Photo sent to Telegram group")
            else:
                print("Failed to send photo to Telegram group")

            # Send the text message to the Telegram group
            text_response = await bot.send_message(chat_id=telegram_group_chat_id, text=message_text)

            # Check the response for sending the text message
            if text_response and text_response.message_id:
                print("Text message sent to Telegram group")
            else:
                print("Failed to send text message to Telegram group")
    except TelegramError as e:
            print(f"Telegram error: {e}")

# Run the asynchronous tasks
asyncio.run(send_photo_and_text())


