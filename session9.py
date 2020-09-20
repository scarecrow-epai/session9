def odd_sec(fn: "fn") -> "fn":
    """
    Decorator to run a function only if the current datetime
    second is odd.
    """
    import datetime

    def inner(*args, **kwargs):
        curr_sec = datetime.datetime.now().second
        if curr_sec % 2 == 0:
            return False
        return fn(*args, **kwargs)

    return inner


def authenticate(fn: "fn", current_password: str, user_password: str) -> "fn":
    """
    Decorator to run a function only if the user_password matches the 
    current password.
    """
    if user_password == current_password:

        def inner(*args, **kwargs):
            print(f"{fn.__name__} was called.")
            return fn(*args, **kwargs)

        return inner
    else:
        return False


def logged(fn: "fn") -> "fn":
    """
    Decorator to log the datetime when a function is called.
    """
    from functools import wraps
    import datetime

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.datetime.now().hour
        result = fn(*args, **kwargs)
        return f"{run_dt}: called {fn.__name__} = {result}"

    return inner


def timed_fac(reps: int) -> "fn":
    """
    Decorator to run a function n times where n is an integer.
    """

    def timed(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            elapsed_total = 0
            elapsed_count = 0

            for i in range(reps):
                print(f"Running iteration {i+1}")
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                elapsed = end - start
                elapsed_total += elapsed
                elapsed_count += 1

            args_ = [str(a) for a in args]
            kwargs_ = ["{0}={1}".format(k, v) for k, v in kwargs.items()]
            all_args = args_ + kwargs_
            args_str = ", ".join(all_args)

            elapsed_avg = elapsed_total / elapsed_count

            print(f"{fn.__name__} ({args_str}) took {elapsed_avg} seconds.")

            return result

        return inner

    return timed


def add(a, b):
    return a + b
