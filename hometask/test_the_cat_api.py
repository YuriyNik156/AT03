import pytest
from the_cat_api import get_image_api_cat

@pytest.mark.parametrize(
    "status_code, json_return_value, expected",
    [
        (
            200,
            [{"id": "34578", "url": "https://cdn2.thecatapi.com/images/34578.jpg"}],
            "https://cdn2.thecatapi.com/images/34578.jpg",
        ),
        (
            404,
            None,
            None,
        ),
    ],
)
def test_get_image_api_cat(mocker, status_code, json_return_value, expected):
    mock_get = mocker.patch("the_cat_api.requests.get")
    mock_get.return_value.status_code = status_code
    mock_get.return_value.json.return_value = json_return_value

    cat_url = get_image_api_cat()

    assert cat_url == expected

