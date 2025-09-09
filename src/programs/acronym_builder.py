def build_acronym(s: str):
    exceptions = ["FOR", "A", "BY", "AN", "AND", "OF"]
    words = s.strip().split(" ")
    for i in range(len(words)):
        if i != 0 and words[i].upper() in exceptions:
            words[i]= ""
            continue
        words[i] = words[i][0].upper()
    acronym = "".join(words)
    return acronym

if __name__ == "__main__":
    build_acronym("world wide web")
    build_acronym("Central Bureau of Investigation")