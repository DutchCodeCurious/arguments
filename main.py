# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting_template="Hello, <name>!"):
    return greeting_template.replace("<name>", name)


def force(mass, body="earth"):
    gravity = {"earth": 9.8, "sun": 274, "jupiter": 24.9, "neptune": 11.2,
            "saturn": 10.4, "uranus": 8.9, "venus": 8.9, "mars": 3.7,
            "mercury": 3.7, "moon": 1.6, "pluto": 0.6}
    f = mass * gravity[body]
    return f


def pull(m1, m2, d):
    g = (6.674*10**-11) * ((m1 * m2)/d**2)
    return g


print(pull(800, 1500, 3))
