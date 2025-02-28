class Cart():
    def __init__(self, request):
        self.session=request.session

        #get the current session key if it exists
        cart=self.session.get('session_key')
        # if the user is new, no session key! Create one !
        if 'session_key' not in request.session:
            cart=self.session['session_key']={}

        #make sure the cart is available on all pages of the site
        self.cart=cart
