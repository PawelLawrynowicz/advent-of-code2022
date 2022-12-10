def find_n_unique(path, n):
    with open(path, 'r') as payload:
        payload_str = payload.read()
        for i in range(len(payload_str) - n):
            if len(set(payload_str[i:i+n])) == n:
                return i + n


if __name__ == "__main__":
    PATH = "day6/input"
    message_start = find_n_unique(PATH, 4)
    print(message_start)
