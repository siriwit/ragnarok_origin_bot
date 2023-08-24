is_active ?= True
preset ?= tank
element ?= None
tribe ?= None
size ?= None
mode ?= None

farm:
	python .\ragnarok.py farm

farm_mr:
	python .\ragnarok.py farm_mr

angpao:
	python .\ragnarok.py angpao

forging:
	python .\ragnarok.py forging

fishing:
	python .\ragnarok.py fishing

feast:
	python .\ragnarok.py feast

dldt:
	python .\ragnarok.py daily_demon_treasure

dlcp:
	python .\ragnarok.py daily_catcaravan

dlat:
	python .\ragnarok.py daily_anthem

ygg:
	python .\ragnarok.py ygg

peteh:
	python .\ragnarok.py pet_enhance

dev:
	python .\ragnarok.py dev

boss:
	python .\ragnarok.py boss

boss_fight:
	python .\ragnarok.py boss_fight

oracle:
	python .\ragnarok.py oracle

dbbb:
	python .\ragnarok.py dbbb

boss_hunt:
	python .\ragnarok.py boss_hunt $(is_active)

picky_boss:
	python .\ragnarok.py picky_boss

preset:
	python .\ragnarok.py preset $(preset)

preset_daily:
	python .\ragnarok.py preset_daily

preset_farm:
	python .\ragnarok.py preset_farm

preset_boss:
	python .\ragnarok.py preset_boss

preset_tank:
	python .\ragnarok.py preset_tank $(element)

preset_card:
	python .\ragnarok.py preset_card $(tribe) $(element) $(size)

alfheim:
	python .\ragnarok.py alfheim $(mode)

time_anomaly:
	python .\ragnarok.py time_anomaly

hordor:
	python .\ragnarok.py hordor $(mode)