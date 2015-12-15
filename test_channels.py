import channels
from mock import Mock
import facebook

def test_facebook_broadcast():
    mock = Mock(facebook.GraphAPI)
    face_book = channels.fb("token", "message")
    face_book.broadcast(mock)

    assert mock.put_object.called
    assert mock.put_object.called_with("me", "feed", message = "message")

