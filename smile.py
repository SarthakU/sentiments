def happy_sad(word):
    # word = ''
    with open('positive.txt', 'r') as f:
        words = f.read().split('\n')
        if word in words:
            print(':)')
            return
        else: 
            f.close()

    with open('negative.txt', 'r') as f:
        words = f.read().split('\n')
        if word in words:
            print(':(')
            return
        else: 
            f.close()

    print(':|')

# happy_sad('yay')
