# chatter-stats
Python scripts that take formatted mailing list archive and slack content and parse out number of messages and participants

## Mailing Lists
Takes input from an archive here: https://www.mail-archive.com/

Running the script
```
python ChatterStats.py -m ml -f <mailing-list-file-txt>
```

Outputs to console
```
Number of users participating: ...
Number of total messages: ...
Number of messages by user: ...
```

## Slack
Takes input copy/paste from Slack

Running the script
```
python ChatterStats.py -m slack -f <slack-file-txt>
```

Outputs to console
```
Number of users participating: ...
Number of total messages: ...
Number of messages by user: ...
```
