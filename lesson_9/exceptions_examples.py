

def example():
    try:
        d = {'url': 'https://google.com'}
        link = d['url']        # KeyError
        print(link)
        s = 'some_string'
        # s.get('link')           # AttributeError
        # print(s + 12)               # TypeError
        a = int(input('Enter your number: '))  # ValueError
        print(a)
    except KeyError as e:
        print(f'Looks like your key is missing : {e.args[0]}')
    except ValueError:
        print('Your "number" is not correct')
    except Exception as e:
        print('i got an error: ', type(e), ' : ', str(e))
    else:
        print('from else block')
        return a**2
    finally:
        print('THIS PART IS ALWAYS COMPLETED')


if __name__ == '__main__':

    result = example()
    print(result)

    print('--=== END ===---')


