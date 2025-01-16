extends Node

var score = 0
@onready var score_label = $Control/ScoreLabel
@onready var crack_instance : crack = null

func _ready():
	if not crack_instance:
		crack_instance = crack.new()
		add_child(crack_instance) 
	if Globals.show_window:
		Globals.show_window=false
		crack_instance.crackme()


func add_point():
	score += 1
	score_label.text ="Coins: " + str(score)
