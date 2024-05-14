# try - except- else - finally
# raise
# open(), writeXXX(), readXXX(), close()

def f():
    try:
        fp = open('todo.txt', 'r')
        print(fp.readlines())

    except PermissionError as pe:  # keine Leseberechtigung
        print('there is no read access')
    except FileNotfoundError as fne:
        print('File does not exist')
    except OSError as ose:
        print('there is some IO error')
    finally:
        fp.close()


def f2():
    try:
        fp = open('todo.txt', 'r')
        print(fp.readlines())

    except (PermissionError, FileNotFoundError) as e:  # Multi-Catch
        print(e)
    except OSError as e:
        print('there is some IO error')
    finally:
        fp.close()


def f3():
    try:
        # zum Schluss wird die Datei automatisch friegegeben (close())
        # Der Aufruf von der Methode clsoe() ist nicht mehr notwendig!
        with open('todo.txt', 'r') as fp:
            print(fp.readlines())

    except (PermissionError, FileNotFoundError) as e:  # Multi-Catch
        print(e)
    except OSError as e:
        print('there is some IO error')
