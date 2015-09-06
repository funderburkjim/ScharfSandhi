"""scharfsandhiWrapper.py
  wrapper function is a decorator used by scharfsandhi.
  This is one possible implementation, useful with ScharfSandhiArg.py.
"""
def wrapper(f):
 def inner(*args,**kwargs):
  self = args[0]
  if not self.dbg:
   ans = f(*args,**kwargs)
   return ans
  name=f.__name__
  if name in ['deletary','sandhi1']:
   ans = f(*args,**kwargs)
   return ans
  # Append to self.history
  h = self.history
  # sandhi is first routine - add extra line   
  if name in ['sandhi']:
   s = args[1]
   h.append('%s: START: "%s"' %(name,s))
  before = ''.join(self.Linary).strip()
  if name == 'sandhimain':
   h.append('%s: START: "%s"' %(name,before))
  # call the function, and save the answer
  ans = f(*args,**kwargs)
  if name in ['sandhi']:
   h.append('%s: DONE: "%s"' %(name,ans))
  else:
   after = ''.join(self.Linary).strip()
   if name in ['sandhimain']:
    h.append('%s: DONE: "%s"' %(name,after))
   elif (before != after) and (name == 'acsandhi'):
    pass  # acsandhi does no direct changes itself    
   elif (before != after):
    #h.append('%s: "%s" (before="%s")' %(name,after,before))
    h.append('%s: "%s"' %(name,after))
  return ans
 return inner

def wrapper_v1(f):
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
