# Myles Joubert
# 3/24/23

with open('strings.txt', 'r') as f:
    
    for line in f:

        line = line.strip().upper()
        
        print(line)
        
        letter_counts = {}
        
        for char in line:
            
            if char.isalpha():
                
                if char in letter_counts:
                    
                    letter_counts[char] += 1
                else:
                    
                    letter_counts[char] = 1
        
        print("Dictionary:", letter_counts)
        
        min_count = min(letter_counts.values())
        
        min_letters = []
        
        for letter, count in letter_counts.items():
            
            if count == min_count:
                min_letters.append(letter)
        
        print("Letters with min count of", min_count, ":", min_letters)
        
        for letter in min_letters:
            del letter_counts[letter]
        
        print("Dictionary after min letter removed:", letter_counts)
        
        letters_list = list(letter_counts.keys())
        
        letters_list.sort()
        
        print("Letters sorted:", letters_list)
        
        print()