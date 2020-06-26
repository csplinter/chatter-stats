import argparse
import re


def get_slack_stats(filename):
    with open(filename, mode='r') as input:
        users = {}
        messages_count = 0
        for line in input:
            messages_count += 1
            x = re.match(r"(.*)\s\s\d+:\d+\s(AM|PM)", line)
            if x:
                user = x.group(1)
                if user not in users:
                    users[user] = 1
                else:
                    users[user] += 1
        print("Number of users participating: " + str(len(users.keys())))
        print("Number of total messages: " + str(sum(users.values())))
        print("Number of messages by user: " + str(sorted(users.items(), key=lambda x: x[1], reverse=True)))


def get_mailing_list_stats(filename):
    with open(filename, mode='r') as input:
        users = {}
        messages_count = 0
        for line in input:
            messages_count += 1
            last_two = line.strip().split(' ')[-2:]
            name = ' '.join(last_two)
            if name not in users:
                users[name] = 1
            else:
                users[name] += 1
        print("Number of users participating: " + str(len(users.keys())))
        print("Number of total messages: " + str(sum(users.values())))
        print("Number of messages by user: " + str(sorted(users.items(), key=lambda x: x[1], reverse=True)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', default='mode', action='store')
    parser.add_argument('-f', '--filename', action='store')

    args = parser.parse_args()

    if args.mode == 'slack':
        get_slack_stats(args.filename)

    if args.mode == 'ml':
        get_mailing_list_stats(args.filename)


if __name__ == "__main__":
    main()
