from game.casting.actor import Actor


class Artifact(Actor):
    """
   
    
    The responsibility of an Artifact is to provide pointsf.

    Attributes:
        _message (string): to display the score when the gems or rocks touch the actor player.
    """
    def __init__(self):
        super().__init__()
        self._score = ""
        
    def get_score(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._score
    
    def set_score(self, score):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._score = score