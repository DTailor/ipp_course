from annoying.decorators import render_to


@render_to('lab1/index.html')
def main(request):
    return {}