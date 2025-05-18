N1,N2,N3,N4 = map(lambda x: round(float(x),1),input().split())
average = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Media: {average:.1f}")

if average >= 7.0:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exam_score = float(input())
    print(f"Nota do exame: {exam_score:.1f}")
    final_average = (average + exam_score) / 2
    if final_average >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {final_average:.1f}")