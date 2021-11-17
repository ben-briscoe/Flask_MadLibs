def make_sure_its_filled_out(input):
    for item in input:
        if item=='':
            try_again=True
            return True
    return False
