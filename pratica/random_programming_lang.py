import random

langs = [
  "Python", "Java", "C", "C++",
  "C#", "JavaScript", "TypeScript",
  "Ruby", "Swift", "Kotlin",
  "Objective-C", "R", "Go", "PHP",
  "Perl", "Scala", "Rust", "Haskell",
  "Dart", "Lua", "Assembly", "MATLAB",
  "Visual Basic", "Groovy", "Clojure",
  "F#", "Scheme", "Elixir", "Erlang",
  "Julia", "Racket", "Fortran", "COBOL",
  "Ada", "Lisp", "Prolog", "SQL","HTML",
  "CSS", "Shell Script", "Batch Script",
  "PowerShell", "D", "Objective-C",
  "ActionScript", "Delphi", "VBScript",
  "Scratch", "Assembly"
]

rand = random.randint(0, len(langs))

print(langs[rand])