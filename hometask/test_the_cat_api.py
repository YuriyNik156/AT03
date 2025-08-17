import pytest
from the_cat_api import get_image_api_cat

def test_get_image_api_cat(mocker):
    mock_get = mocker.patch("the_cat_api.requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {
        'id' : '34578',
        'url' : 'https://cdn2.thecatapi.com/images/34578.jpg'
    }
    ]

    cat_url = get_image_api_cat()

    assert cat_url == 'https://cdn2.thecatapi.com/images/34578.jpg'

