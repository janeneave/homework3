import time

# [A]
class Hyperlink:
    def __init__(self, name, url, options):
        self.name = name
        self.url = url
        self.options = options

    def append_to_hyperlink_history(self):
        hyperlink_history.append(self.url)


base_url = "https://codefirstgirls.com/"

menus = {
    'base': Hyperlink('base', base_url, ['Courses', 'Opportunities']),
    'courses': Hyperlink('courses', base_url + 'courses', ['CFGDegree', 'Back']),
    'cfgdegree': Hyperlink('cfgdegree', base_url + 'courses/cfgdegree', ['Back']),
    'opportunities': Hyperlink('opportunities', base_url + 'opportunities', ['Ambassadors', 'Back']),
    'ambassadors': Hyperlink('ambassadors', base_url + 'opportunities/ambassadors', ['Back']),
}

current_menu = menus['base']
hyperlink_history = [current_menu.url]

if __name__ == '__main__':
    start_time = time.process_time()
    while True:
        print(f"You are currently on the URL {current_menu.url}")
        print("Where are you clicking? (Type 'exit' to quit and print your Hyperlink History)")
        print('Options:', ', '.join(current_menu.options))

        user_input = input().lower()

        if user_input == 'exit':
            break

        if user_input in menus:
            current_menu = menus[user_input]
            current_menu.append_to_hyperlink_history()
        elif user_input == 'back':
            if len(hyperlink_history) > 1:
                if current_menu.name in ['courses', 'opportunities']:
                    current_menu = menus['base']
                else:
                    previous_url_field = hyperlink_history[-2].split('/')[-1]
                    current_menu = menus[previous_url_field]
                current_menu.append_to_hyperlink_history()
        elif user_input not in menus:
            print('Invalid Input. Please try again.')

    print('HYPERLINK HISTORY:')
    for item in hyperlink_history:
        print(f'{item}\n')

    end_time = time.process_time()
    run_time = end_time - start_time
    print(run_time)

# [B]
# TTIME COMPLEXITY:
# Mainly, I believe the time complexity of my solution depends on the number of user interactions
# and the overall size of the hyperlink history.
# The main loop runs for as long as the user doesn't use the 'exit' and break it, this makes the
# time complexity of the user input/handling O(N), whereby N is the number of user interactions, because
# this modulates how many iterations of the loop are performed. In a worst case, the user could run
# the loop a significant number of times.
# Moreover, the operations in the main loop take constant time (e.g. print, input).
# Appending the url to the hyperlink_history provides a time complexity of O(1) (constant time)
# per user interaction/iteration.
# In conclusion, I think the time complexity is O(N) becuase the largest contributing factor is the
# main loop, where N is the number of user interactions.

# SPACE COMPLEXITY:
# I believe the space complexity of my solution depends on the data structures used to store the menus
# and hyperlink history.
# There are quite a few data structures, and the ones are the menus dictionary, current_menu object,
# and hyperlink_history list. Their sizes are constant and unchanged by input size therefore
# making their space complexity O(1).
# the hyper_link history has a space complexity of O(N) whereby N is the numer of urls in the list.
# Overall I think that becuase of these factors, the space complexity is mainly determined by
# the hyperlink_history list, making it to be O(N), where M is the number of URLs visited by the user during
# the running of the program which are then stored in the list.

# Assumptions:
# The user input is reasonable and does not result in extreme cases. For instance, I'm probably assuming
# that the size of the hyperlink_history won't get exceptionally large, (I did attempt to use one of the types of
# collections data structure but couldn't get it to work with my current logic).
# I am assuming that the number of menus and hyperlinks is constant and does not change or grow with input size.
