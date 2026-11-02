import statistics
def summary(rows):


    if not rows:
        return{
            "row_count":0,
            "columns":[],
            "numeric_summery":{}
        }

    columns=list(rows[0].key())

    numeric_column=[
        col for col in columns
        if all (isinstance(row[col], (int,float))
        and not isinstance(row [col],bool)
        for row in rows)
    ]

    numeric_summary={
        col:{
            "min":min(row[col]for row in rows),
            "max":max(row[col] for row in rows),
            "mean": statistics.mean(row[col] for row in rows)

        }
        for col in numeric_column
    }
    return {
        "row_count":len(rows),
        "columns":columns,
        "numeric_summery":numeric_summary
    }
