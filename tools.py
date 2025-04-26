from typing import Callable

#To represent things that the agent will do
class Tool:
    def __init__(self, name : str, description : str, func : Callable):
        # Initializes a Tool
        self.name = name
        self.description = description
        self.func = func

    def run(self, *args, **kwargs):
        # Executes the tool's function with provided arguments and returns fucntions output
        return self.func(*args,**kwargs)
    
    def get_metadata(self):
        # Returns the metadata which is the name and description of the Tool
        return {
            "name" : self.name,
            "description" : self.description
        } 