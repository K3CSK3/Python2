from colored import * # Terminálon futtatni való      | pip install colored |
def greeting(text:str) -> None:
    text = text.title()
    color = len(text)
    print(f'%s Üdvözlöm {text}%s' % (fg(color), attr(0)))