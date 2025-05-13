import random
from collections import Counter


def generate_domino_set():
    return [[i, j] for i in range(7) for j in range(i, 7)]


def determine_start(player, computer):
    for i in range(6, -1, -1):
        if [i, i] in player:
            if [i, i] in computer:
                return [i, i], "player"
            else:
                return [i, i], "player"
        elif [i, i] in computer:
            return [i, i], "computer"
    return None, None


def print_game(stock, computer, player, domino_snake, current_player):
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}\n")

    if len(domino_snake) > 6:
        print(f"{domino_snake[:3]}...{domino_snake[-3:]}")
    else:
        print(domino_snake)

    print("\nYour pieces:")
    for i, piece in enumerate(player):
        print(f"{i + 1}:{piece}")

    if current_player == "player":
        print("Status: It's your turn to make a move. Enter your command.")
    else:
        print("Status: Computer is about to make a move. Press Enter to continue...")


def is_legal_move(piece, domino_snake, to_left):
    left = domino_snake[0][0]
    right = domino_snake[-1][1]
    if to_left:
        return piece[0] == left or piece[1] == left
    else:
        return piece[0] == right or piece[1] == right


def apply_move(piece, domino_snake, to_left):
    if to_left:
        if piece[1] == domino_snake[0][0]:
            domino_snake.insert(0, piece)
        else:
            domino_snake.insert(0, piece[::-1])
    else:
        if piece[0] == domino_snake[-1][1]:
            domino_snake.append(piece)
        else:
            domino_snake.append(piece[::-1])


def get_piece_scores(computer, domino_snake):
    counts = Counter()
    for piece in computer + domino_snake:
        counts[piece[0]] += 1
        counts[piece[1]] += 1
    scores = {tuple(piece): counts[piece[0]] + counts[piece[1]] for piece in computer}
    return scores


def player_move(player, domino_snake, stock):
    while True:
        try:
            move = int(input("> "))
            if move == 0:
                if stock:
                    player.append(stock.pop())
                break
            idx = abs(move) - 1
            if idx >= len(player):
                raise ValueError
            piece = player[idx]
            if move < 0 and is_legal_move(piece, domino_snake, to_left=True):
                apply_move(piece, domino_snake, to_left=True)
                player.pop(idx)
                break
            elif move > 0 and is_legal_move(piece, domino_snake, to_left=False):
                apply_move(piece, domino_snake, to_left=False)
                player.pop(idx)
                break
            else:
                print("Illegal move. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


def computer_move(computer, domino_snake, stock):
    input()
    scores = get_piece_scores(computer, domino_snake)
    sorted_pieces = sorted(computer, key=lambda x: scores[tuple(x)], reverse=True)

    for piece in sorted_pieces:
        if is_legal_move(piece, domino_snake, to_left=True):
            apply_move(piece, domino_snake, to_left=True)
            computer.remove(piece)
            return
        elif is_legal_move(piece, domino_snake, to_left=False):
            apply_move(piece, domino_snake, to_left=False)
            computer.remove(piece)
            return

    if stock:
        computer.append(stock.pop())


def check_game_over(player, computer, domino_snake, stock):
    if not player:
        return "You won!"
    elif not computer:
        return "The computer won!"
    elif domino_snake[0][0] == domino_snake[-1][1]:
        num = domino_snake[0][0]
        count = sum(piece.count(num) for piece in domino_snake)
        if count >= 8:
            return "It's a draw!"
    elif not stock and all(
            not is_legal_move(piece, domino_snake, True) and not is_legal_move(piece, domino_snake, False)
            for piece in player + computer
    ):
        return "It's a draw!"
    return None


def main():
    while True:
        domino_set = generate_domino_set()
        random.shuffle(domino_set)
        player = domino_set[:7]
        computer = domino_set[7:14]
        stock = domino_set[14:]

        starting_piece, current_player = determine_start(player, computer)
        if starting_piece:
            if current_player == "player":
                player.remove(starting_piece)
                current_player = "computer"
            else:
                computer.remove(starting_piece)
                current_player = "player"
            domino_snake = [starting_piece]
            break

    while True:
        print_game(stock, computer, player, domino_snake, current_player)
        result = check_game_over(player, computer, domino_snake, stock)
        if result:
            print(f"Status: {result}")
            break
        if current_player == "player":
            player_move(player, domino_snake, stock)
            current_player = "computer"
        else:
            computer_move(computer, domino_snake, stock)
            current_player = "player"


if __name__ == "__main__":
    main()