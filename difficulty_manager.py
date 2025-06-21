# Create a class to manage different difficulties
class DifficultyManager:
    def __init__(self):
        self.word_levels = {
            "easy": [
                "code", "data", "loop", "func", "var", "int", "str", "list", "dict", "set",
                "tuple", "def", "class", "True", "False", "None", "if", "else", "elif", "for",
                "while", "try", "except", "pass", "break", "cont", "ret", "arg", "kwarg", "self",
                "init", "main", "path", "file", "read", "write", "open", "close", "sort", "map",
                "filt", "iter", "next", "call", "obj", "type", "cast", "comp", "pip", "env"
            ],
            "medium": [
                "module", "import", "return", "lambda", "method", "object", "string", "number",
                "float", "integer", "boolean", "global", "local", "scope", "syntax", "error",
                "debug", "output", "input", "print", "library", "package", "function", "program",
                "script", "compile", "execute", "iterate", "console"
            ],
            "hard": [
                "decorator", "generator", "comprehension", "encapsulation", "inheritance",
                "polymorphism", "abstraction", "classmethod", "staticmethod", "metaclass",
                "descriptor", "contextmanager", "coroutine", "asynchronous", "multithreading",
                "multiprocessing", "serialization", "deserialization", "introspection",
                "reflection", "recursion", "algorithm", "structure", "bytecode", "interpreter",
                "framework", "dependency", "virtual", "environment", "paradigm"
            ]
        }
 # Return a word list based on selected difficulty
    def get_words(self, level):
        return self.word_levels.get(level, self.word_levels["medium"])