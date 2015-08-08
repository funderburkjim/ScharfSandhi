def wrapper(f):
 def inner(*args,**kwargs):
  self = args[0]
  if not self.dbg:
   ans = f(*args,**kwargs)
   return ans
  name=f.__name__
  if name in ['deletary']:
   ans = f(*args,**kwargs)
   return ans
  # Append to self.history
  h = self.history
  # sandhi is first routine - add extra line   
  if name in ['sandhi','sandhi1']:
   s = args[1]
   h.append('%s: START="%s"' %(name,s))
  before = ''.join(self.Linary)
  if name == 'sandhimain':
   h.append('%s: START Linary="%s"' %(name,before))
  # call the function, and save the answer
  ans = f(*args,**kwargs)
  after = ''.join(self.Linary)
  if (before != after):
   h.append('%s: Linary="%s"' %(name,after))
  return ans
 return inner
