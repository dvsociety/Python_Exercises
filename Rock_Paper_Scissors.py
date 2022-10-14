options = {
    'rock': {
        'scissors': 'Has ganado',
        'rock': 'Empate',
        'paper': 'Has perdido'
    },
    
    'paper': {
        'rock': 'Has ganado',
        'paper': 'Empate',
        'scissors': 'Has perdido'
    },
    
    'scissors': {
        'paper': 'Has ganado',
        'scissors': 'Empate',
        'rock': 'Has perdido'
    }
}

def play_rps(user_input, computer_input):
    return options[user_input][computer_input]

print(play_rps('rock','rock'))