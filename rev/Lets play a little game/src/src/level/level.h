#ifndef LEVEL_H
#define LEVEL_H

#include <godot_cpp/core/class_db.hpp>
#include <godot_cpp/classes/label.hpp>
#include <godot_cpp/classes/area2d.hpp>
#include <godot_cpp/classes/node.hpp>
#include <godot_cpp/classes/scene_tree.hpp>
#include <godot_cpp/classes/resource_loader.hpp>
#include <godot_cpp/classes/packed_scene.hpp>
#include <godot_cpp/variant/utility_functions.hpp>
#include <gdextension_interface.h>
#include <godot_cpp/classes/window.hpp>


namespace godot {

class level : public Area2D {
	GDCLASS(level, Area2D)

private:
	Label *score_label;
	String current_scene_file;

public:
	level();
	~level();
	void _ready() override;
    void _on_body_entered(Node *body);
	void level_shift(int,int,int);
	void change_scene(int);
	static void _bind_methods();
};

}

using namespace godot;

void initialize_example_module(ModuleInitializationLevel p_level);
void uninitialize_example_module(ModuleInitializationLevel p_level);

#endif