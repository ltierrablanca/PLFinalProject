
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '29F71D2592A773491CC37E870EE365B4'
    
_lr_action_items = {'PRINT':([0,],[1,]),'$end':([2,3,4,5,6,],[-2,-10,0,-1,-7,]),'CONTENTS':([1,],[6,]),'NIL':([0,],[3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'call':([0,],[2,]),'exp':([0,],[4,]),'atom':([0,],[5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> atom','exp',1,'p_exp_atom','yacc.py',21),
  ('exp -> call','exp',1,'p_exp_call','yacc.py',29),
  ('items -> item items','items',2,'p_items','yacc.py',43),
  ('items -> empty','items',1,'p_items_empty','yacc.py',47),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',51),
  ('item -> atom','item',1,'p_item_atom','yacc.py',55),
  ('call -> PRINT CONTENTS','call',2,'p_call','yacc.py',70),
  ('bool -> TRUE','bool',1,'p_true','yacc.py',98),
  ('bool -> FALSE','bool',1,'p_false','yacc.py',102),
  ('atom -> NIL','atom',1,'p_nil','yacc.py',106),
]
