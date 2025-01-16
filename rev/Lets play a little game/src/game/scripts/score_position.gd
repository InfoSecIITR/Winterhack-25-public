extends Control

func _ready():
	update_score_position()

func _process(delta):
	update_score_position()

func update_score_position():
	var viewport_size = get_viewport_rect().size
	# Position in the top-right corner with padding
	position = Vector2(viewport_size.x - size.x - 10, 10)
