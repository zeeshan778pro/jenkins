import fire

def hello(name="My World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
