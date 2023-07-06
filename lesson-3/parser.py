def parse(start_symbol,text,grammar):

    tokenizer = grammar[' '] + '(%s)'

    def parse_sequence(sequence,text):
        result = []
        for atom in sequence:
            tree,text = parse_atom(atom,text)
            if text is None:return File
            result.append(tree)
        return result,text

