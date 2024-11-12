if __name__ == '__main__':
    n = int(input())
    if 2 <= n <= 6:
        students = []
        
        for i in range(n):
            name = list(input())
            grade = list(float(input()))
            students.append([name, grade])
            
            scores = [i[1] for i in students]
            lowest_score = min(grade)
            filtered_score = [i for i in scores if i!= lowest_score]
            second_lowest = min(filtered_score)
            
            second_lowest_students = [i[0] for i in students if i[1] == second_lowest]
            
            second_lowest_students.sort()
            
            for i in second_lowest_students:
                print(i)
            
        
            