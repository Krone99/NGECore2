import sys

def setup(core, object):
	object.setStfFilename('static_item_n')
	object.setStfName('item_wookiee_hat_02_01')
	object.setDetailFilename('static_item_d')
	object.setDetailName('item_wookiee_hat_02_01')
	object.setIntAttribute('cat_stat_mod_bonus.@stat_n:agility_modified', 3)
	object.setStringAttribute('class_required', 'Spy')
	return