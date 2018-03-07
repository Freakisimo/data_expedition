
def is_list(item):
    return isinstance(item, list) or isinstance(item, tuple)

def is_dict(item):
    return isinstance(item, dict)

def depth_structure(doc, with_value=True, current=[], row=[]):
    if is_dict(doc):
        for k,v in doc.items():
            current.append(k)
            if is_dict(v):
                for d in depth_structure(v, with_value, current, row):
                    pass
            elif is_list(v):
                for i in v:
                    for j in depth_structure(i, with_value, current, row):
                        pass
            else:
                if with_value:
                    current.append(v)
                row.append(current)
                current = []
    else:
        current.append(doc)
    return row

if __name__ == '__main__':
    depth_structure({'a':'b'})
