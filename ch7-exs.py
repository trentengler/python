print('Ex 7-4')
print()
poem = "My kitty cat likes %s, \
my kitty cat likes %s, \
my kitty cat fell on his %s, \
and now thinks he's a %s." % ('roast beef','ham','head','clam')

print(poem)
print()
print('Ex 7-4 alternate a')
print()
poem2 = "My kitty cat likes %(one)s, \
my kitty cat likes %(two)s, \
my kitty cat fell on his %(three)s, \
and now thinks he's a %(four)s." \
% {'one':'roast beef','two':'ham','three':'head','four':'clam'}
print(poem2)
print()
print('Ex 7-4 alternate b')
print()
values = {'one':'roast beef','two':'ham','three':'head','four':'clam'}
poem2 = "My kitty cat likes %(one)s, \
my kitty cat likes %(two)s, \
my kitty cat fell on his %(three)s, \
and now thinks he's a %(four)s."
print(poem2 % values)
print()
print()
print('Ex 7-5')
print()
letter = """Dear {salutation} {name},

Thank you for your letter. We are sorry that our {product} {verbed} in 
your {furniture}. Please note that it should never be used on a {furniture},
especially near any {animals}.

Send us your receipt and {amount} for shipping and handling. We will 
send you another {product} that, in our tests, is {percent} percent less 
likely to have {verbed}.

Thank you for your support.

Sincerely,
{spokesman}
{job_title}"""

response = {'salutation':'Stupid','name':'Fuck','product':'GiantSmellyShitBall','verbed':'leaked','furniture':'couch','animals':'GoldenRetrievers','amount':'lotsOf$$$','percent':'10','spokesman':'D_Mofo_Trump','job_title':'ChiefDickHead'}

print(letter.format(**response))
