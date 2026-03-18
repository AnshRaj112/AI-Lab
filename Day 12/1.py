import sys
import pygame


WIDTH, HEIGHT = 600, 700
BOARD_SIZE = 600
CELL_SIZE = BOARD_SIZE // 3
LINE_WIDTH = 8
MARK_WIDTH = 12
PADDING = 35

BG_COLOR = (240, 245, 255)
GRID_COLOR = (40, 44, 52)
X_COLOR = (220, 20, 60)
O_COLOR = (30, 100, 220)
TEXT_COLOR = (30, 30, 30)


def is_winner(board, player):
    win_states = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]
    return any(all(board[i] == player for i in state) for state in win_states)


def is_full(board):
    return " " not in board


def minimax(board, is_max, alpha, beta, depth=0):
    if is_winner(board, "X"):
        return 10 - depth
    if is_winner(board, "O"):
        return depth - 10
    if is_full(board):
        return 0

    if is_max:
        best = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, False, alpha, beta, depth + 1)
                board[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best

    best = float("inf")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, True, alpha, beta, depth + 1)
            board[i] = " "
            best = min(best, score)
            beta = min(beta, best)
            if beta <= alpha:
                break
    return best


def best_move(board):
    best_score = -float("inf")
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            score = minimax(board, False, -float("inf"), float("inf"))
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move


def draw_grid(screen):
    for i in range(1, 3):
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, BOARD_SIZE),
            LINE_WIDTH,
        )
        pygame.draw.line(
            screen,
            GRID_COLOR,
            (0, i * CELL_SIZE),
            (BOARD_SIZE, i * CELL_SIZE),
            LINE_WIDTH,
        )


def draw_marks(screen, board):
    for idx, mark in enumerate(board):
        row, col = divmod(idx, 3)
        cx = col * CELL_SIZE + CELL_SIZE // 2
        cy = row * CELL_SIZE + CELL_SIZE // 2

        if mark == "X":
            x1, y1 = cx - (CELL_SIZE // 2 - PADDING), cy - (CELL_SIZE // 2 - PADDING)
            x2, y2 = cx + (CELL_SIZE // 2 - PADDING), cy + (CELL_SIZE // 2 - PADDING)
            pygame.draw.line(screen, X_COLOR, (x1, y1), (x2, y2), MARK_WIDTH)
            pygame.draw.line(screen, X_COLOR, (x1, y2), (x2, y1), MARK_WIDTH)
        elif mark == "O":
            pygame.draw.circle(
                screen,
                O_COLOR,
                (cx, cy),
                CELL_SIZE // 2 - PADDING,
                MARK_WIDTH,
            )


def draw_status(screen, game_over, status):
    status_rect = pygame.Rect(0, BOARD_SIZE, WIDTH, HEIGHT - BOARD_SIZE)
    pygame.draw.rect(screen, BG_COLOR, status_rect)

    # Visual indicator bar (green while playing, amber when game over)
    indicator_color = (50, 170, 90) if not game_over else (220, 160, 40)
    pygame.draw.rect(
        screen,
        indicator_color,
        pygame.Rect(30, BOARD_SIZE + 60, WIDTH - 60, 20),
        border_radius=10,
    )

    # Render the status text
    font = pygame.font.SysFont(None, 40)
    text = font.render(status, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, BOARD_SIZE + 30))
    screen.blit(text, text_rect)


def reset_game(human_starts):
    if human_starts:
        return [" "] * 9, False, "Your turn (O)", "O"
    else:
        return [" "] * 9, False, "AI thinking...", "X"


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic-Tac-Toe (Minimax AI)")

    clock = pygame.time.Clock()

    human_starts = True
    board, game_over, status, current_turn = reset_game(human_starts)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                human_starts = not human_starts
                board, game_over, status, current_turn = reset_game(human_starts)

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over and current_turn == "O":
                mx, my = event.pos
                if my < BOARD_SIZE:
                    row = my // CELL_SIZE
                    col = mx // CELL_SIZE
                    idx = row * 3 + col

                    if board[idx] == " ":
                        board[idx] = "O"

                        if is_winner(board, "O"):
                            game_over = True
                            status = "You win!"
                        elif is_full(board):
                            game_over = True
                            status = "Draw!"
                        else:
                            current_turn = "X"
                            status = "AI thinking..."

        if current_turn == "X" and not game_over:
            # Force a frame draw so "AI thinking..." is displayed before AI computes move
            screen.fill(BG_COLOR)
            draw_grid(screen)
            draw_marks(screen, board)
            draw_status(screen, game_over, status)
            pygame.display.set_caption(f"Tic-Tac-Toe (Minimax AI) | {status} | Press R to restart")
            pygame.display.flip()

            ai_idx = best_move(board)
            if ai_idx != -1:
                board[ai_idx] = "X"

            if is_winner(board, "X"):
                game_over = True
                status = "AI wins!"
            elif is_full(board):
                game_over = True
                status = "Draw!"
            else:
                current_turn = "O"
                status = "Your turn (O)"

        screen.fill(BG_COLOR)
        draw_grid(screen)
        draw_marks(screen, board)
        draw_status(screen, game_over, status)

        pygame.display.set_caption(f"Tic-Tac-Toe (Minimax AI) | {status} | Press R to restart")

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()