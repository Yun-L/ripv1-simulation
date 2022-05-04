MAX_ITERATIONS = 100

def main():
    hosts = []
    for i in range(MAX_ITERATIONS):
        # tick one time step of every host per iteration
        list(map(lambda host:host.tick(), hosts))
