#ifndef CRACK_H
#define CRACK_H

#include <gdextension_interface.h>
#include <godot_cpp/classes/window.hpp>
#include <godot_cpp/godot.hpp>

namespace godot {

class crack: public Node {
    GDCLASS(crack, Node)

private:

public:
	crack();
	~crack();

    void crackme();
	static void _bind_methods();
};

}

using namespace godot;

void initialize_example_module(ModuleInitializationLevel p_crack);
void uninitialize_example_module(ModuleInitializationLevel p_crack);

#endif