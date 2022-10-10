# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

file_with_source_text_path = 'Homework504 - Task_4\\TextToCompress.txt'
file_with_compressed_text_path = 'Homework504 - Task_4\\CompressedText.txt'
file_with_recovered_text_path = 'Homework504 - Task_4\\RecoveredText.txt'

def text_compress(source_path, target_path):
    with open(source_path, 'r') as source, open(target_path, 'w') as target: 
        source_str = source.readline()
        words_list = source_str.split(" ")
        result_word = ""
        result_list = []
        counter = 0

        for word in words_list:
            result_word = word[0]
            for ch in word:
                if result_word[-1] == ch:
                    counter += 1
                else:
                    result_word += str(counter)
                    result_word += ch
                    counter = 1
            result_word += str(counter)
            result_list.append(result_word)
            counter = 0
        target.write(" ".join(result_list))
    return target_path

def text_recover(source_path, target_path):
    with open(source_path, 'r') as source, open(target_path, 'w') as target: 
        source_str = source.readline()
        words_list = source_str.split(" ")
        result_list = []
        for word in words_list:
            result_word = ""
            i = 0
            while i in range(0,len(word)):
                num=""
                if word[i].isdigit():
                    while word[i].isdigit():
                        num+=word[i]
                        if i < len(word)-1:
                            i+=1
                        else:
                            break
                    else:
                        i-=1
                else:
                    letter=word[i]
                # тут он по непонятной мне причине отказывался делать result_word+=letter*int(num), поэтому я заставил его делать это через try
                try:
                    result_word+=letter*int(num)
                except ValueError:
                    result_word = result_word
                i+=1
            result_list.append(result_word)
        target.write(" ".join(result_list))
    return target_path

text_compress(file_with_source_text_path, file_with_compressed_text_path)
text_recover(file_with_compressed_text_path, file_with_recovered_text_path)