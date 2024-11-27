if __name__ == '__main__':
    
    name_list = []
    score_list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())  

        name_list.append(name)
        score_list.append(score)

    unique_scores = list(set(score_list))
    unique_scores.sort()
    
    if len(unique_scores) < 2:
        print("There are not enough unique scores to find the second lowest.")
    else:
        second_lowest_score = unique_scores[1]

        second_lowest_names = []
        for i, score in enumerate(score_list):
            if score == second_lowest_score:
                second_lowest_names.append(name_list[i])
        
        second_lowest_names.sort()

        for i in second_lowest_names:
            print(i)
