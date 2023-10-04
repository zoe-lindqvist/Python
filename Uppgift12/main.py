import random

# Lista över aritmetiska operatorer
operators = ['*', '//', '%']


# Funktion för att generera ett unikt matematiskt problem
def generate_math_problem(num_questions, chosen_operator, table_or_divisor, asked_questions):
    while True:
        factor_or_dividend = random.randint(0, 12)
        question = (factor_or_dividend, chosen_operator, table_or_divisor)
        # Kontrollera om frågan redan har ställts eller om antalet gånger den ställts överstiger tröskelvärdet
        if question not in asked_questions or asked_questions.count(question) < (num_questions // 13 + 1):
            asked_questions.append(question)
            return question


# Funktion för att utvärdera det matematiska problemet
def evaluate_math_problem(factor_or_dividend, operator, table_or_divisor):
    return eval(f'{factor_or_dividend} {operator} {table_or_divisor}')


def get_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            user_input = int(input(prompt))
            if (min_value is None or user_input >= min_value) and (max_value is None or user_input <= max_value):
                return user_input
            else:
                print(f"Vänligen mata in ett nummer mellan {min_value} och {max_value}.")
        except ValueError:
            print("\nDet var inte ett giltigt heltal. Försök igen.")


# Huvudfunktion
def main():
    while True:
        # Användaren väljer antal frågor
        num_questions = get_int_input('\nVälj antal frågor (12 - 39): ', 12, 39)
        # Användaren väljer vilken typ av räknesätt
        operator_type = get_int_input('\nVälj räknesätt (1 för multiplikation, 2 för heltalsdivision, 3 för modulus, 4 för slumpade räknesätt): ', 1, 4)

        # Initialisera en tom lista för att lagra frågorna som har ställts
        asked_questions = []

        # Loop över antalet frågor som användaren valde
        for i in range(num_questions):
            # Om användaren valde slumpade räknesätt, välj en slumpmässig operator
            if operator_type == 4:
                chosen_operator = random.choice(operators)
            # Annars, använd den operator som användaren valde    
            else:
                chosen_operator = operators[operator_type - 1]
            # Om användaren valde multiplikation, låt dem välja vilken tabell att använda    
            if chosen_operator == '*':
                table_or_divisor = get_int_input('\nVälj tabell (2 - 12): ', 2, 12)
            # Annars, låt dem välja vilken divisor att använda
            else:
                table_or_divisor = get_int_input('\nVälj divisor (2 - 5): ', 2, 5)
            
            # Generera en matematisk fråga med hjälp av en funktion
            factor_or_dividend, operator, table_or_divisor = generate_math_problem(num_questions, chosen_operator, table_or_divisor, asked_questions)
            # Beräkna det korrekta svaret på frågan
            correct_answer = evaluate_math_problem(factor_or_dividend, operator, table_or_divisor)
            # Fråga användaren om svaret på frågan
            user_answer = get_int_input(f'\nFråga {i+1}: Vad blir {factor_or_dividend} {operator} {table_or_divisor}? ')

            # Kontrollera om användarens svar är korrekt
            if user_answer != correct_answer:
                # Om användaren svarade fel, informera dem om det korrekta svaret och avsluta spelet
                print(f'\nTyvärr, svaret är fel. Rätt svar är {correct_answer}.')
                break
            else:
                # Om användaren svarade rätt, bekräfta detta
                print('\nRätt svar!')

                # Om det inte är den sista frågan, fortsätt med zombie-dörren
                if i != num_questions - 1:
                    # Generera en slumpmässig dörr som innehåller zombies
                    zombie_door = random.randint(1, num_questions - i)
                    user_door = get_int_input(f'\nVälj en dörr (1 - {num_questions - i}): ', 1, num_questions - i)
                    # Be användaren att välja en dörr

                    # Kontrollera om användaren öppnade zombie-dörren
                    if user_door == zombie_door:
                        # Om så är fallet, informera dem om detta och avsluta spelet
                        print('\nTyvärr, du öppnade dörren med zombies. Spelet är över.')
                        break
                    else:
                        # Om de valde en säker dörr, informera dem om detta
                        print(f'\nPuh! Zombiesarna var bakom dörr nummer {zombie_door}. Du är säker... än så länge.')
        else:
            # Om alla frågor har besvarats korrekt och användaren inte öppnade zombie-dörren, gratulera dem till att vinna spelet
            print('\nGrattis, du har vunnit spelet!')

        play_again = input('\nVill du spela igen? (ja/nej): ').lower().strip()
        if play_again != 'ja':
            break


main()
