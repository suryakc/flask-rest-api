from .people import PeopleAPI

# Constants
BASE_URL = "/api/v1/"

def initialize_routes(api):
    api.add_resource(PeopleAPI,f'{BASE_URL}people')