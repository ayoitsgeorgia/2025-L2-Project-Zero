# Function go here
def make_statement(statement, decoration):
    """Emphasise headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Check that users enter the full word
    or the "n" letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")

def instructions():
    make_statement("Instructions", "ℹ️")

    print('''
    
For each ticket holder enter ...
- Their name
- Their age
- Their payment method (cash / card)

The program will record the ticket sale and calculate the
ticket cost (and the profit).

Once you will have either solf all of the tickets or entered the
exit code ('xxx'), the program will display the ticket
sales information and write the data in a text file.

It will also choose one luck ticket holder who wins the
draw (their ticket is free).

    ''')

# main routine goes here

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions?" )

if want_instructions == "yes":
    instructions()

print()
print("program continues...")