from annoying.decorators import render_to


@render_to('labs/index.html')
def main(request):
    return {}