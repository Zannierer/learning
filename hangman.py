def hangman(word):
        chance = 3
        board = []
        print("Word has {} letter(s)".format(len(word)))
        while (chance != 0) and (len(word) != 0):
                ans = input("Type the letter you guess: ")
                answer = ans[0].lower()
                board.append(answer)
                finder = word.find(answer)
                if finder != (-1):
                        count = 1
                        finder = word.find(answer, finder+1)
                        while finder != (-1):
                                count += 1
                                finder = word.find(answer, finder+1)
                        word = word.replace(answer,"")
                        print('{} instance(s) of letter {} found!'.format(count, answer))
                else:
                        chance += (-1)
                        print('{} not found, {} chance(s) left'.format(answer, chance))
                        
                print("{} letter(s) left".format(len(word)))
                print("Already answered: ", board)
        if chance == 0:
                return False
        elif len(word) == 0:
                return True


if __name__ == "__main__":
        word = 'wow'
        if hangman(word):
                print("you win!!")
        else:
                print("you lose")


