def validate_obligatory_fields(cls, obligatory_fields):
    missing_fields = []
    for field in obligatory_fields:
        if field not in vars(cls):
            missing_fields.append(field)

    if missing_fields:
        raise AttributeError(f"The {cls.__name__} class has to define the following properties:"
                             f" {', '.join(missing_fields)}")
