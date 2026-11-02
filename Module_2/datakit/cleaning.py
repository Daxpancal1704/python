def drop_missing(rows):
    return[
        row for row in rows
        if all (value is not None and value != ""
                for value in row.values()) 
    ]

def remove_duplicate(rows):
    seen=set()

    return[ row for row in rows
           if tuple(row.item()) not in seen
            and not seen.add(tuple(row.item())) 
            ]

def clean_rows(rows):
    return remove_duplicate(drop_missing(rows))

