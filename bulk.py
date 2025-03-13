import json

for x in range(1088):  # Updated range to 1088 files (0-1087)
    with open(f'C:\\Users\\Admin\\Desktop\\GITHUBREPOS\\ipfs-nft-collection-scrapper\\GMers\\metadata\\{x}.json', 'r+') as f:  # Updated path
        data = json.load(f)
        # Update description field
        data['description'] = "A relic and celebration of FTM. The GMers collab with FUNERAL and DRACULA PRESLEY. GM."
        # Preserve existing image or add new one if needed
        # If you want to keep the image line from your example, uncomment the next line
        # data['image'] = f"https://gateway/ipfs/CID/{x}.png"
        
        f.seek(0)        # Reset file position to the beginning
        json.dump(data, f, indent=4)
        f.truncate()     # Remove remaining part