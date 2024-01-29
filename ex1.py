def is_lucky(ticket_number):
    digits = [int(digit) for digit in str(ticket_number)]
    half_len = len(digits) // 2
    first_half_sum = sum(digits[:half_len])
    second_half_sum = sum(digits[half_len:])
    return first_half_sum == second_half_sum


def get_lucky_tickets(N):
    lucky_tickets = []
    ticket_number = 111111

    while len(lucky_tickets) < N:
        if is_lucky(ticket_number):
            lucky_tickets.append(ticket_number)
        ticket_number += 1

    return lucky_tickets

N = 5
result = get_lucky_tickets(N)
print(f"{N} счастливых билетов: {result}")
