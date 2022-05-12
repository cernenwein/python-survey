import os
import survey as survey

TXT = 'file.txt'


def reading():
    # script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    # saved_umask = os.umask(0o077)
    # path = os.path.join(script_dir)
    with open(TXT, 'rb') as handle:
        return {
            'Is your app containerized? ':
                {'answer': 'N/A',
                 'possibleAnswers': ['Yes', 'No', 'N/A', 'TBD'],
                 'type': 'select'
                 },
            'Runs in Kubernetes in production? ':
                {'answer': 'N/A',
                 'possibleAnswers': ['Yes', 'No', 'N/A', 'TBD'],
                 'type': 'select'
                 }
        }


def writing(a):
    with open(TXT, 'wb') as handle:
        pass


def ask_question(q_key, parts):
    answer = survey.select(parts['possibleAnswers'], f'{q_key}', hint='test')
    print(f'Answered {answer}.')
    # convert back to string
    return parts['possibleAnswers'][answer]


if __name__ == '__main__':
    config = reading()
    for key in config.keys():
        print(key, '->', config[key])
        config[key] = ask_question(key, config[key])
    writing(config)
    print(config)
