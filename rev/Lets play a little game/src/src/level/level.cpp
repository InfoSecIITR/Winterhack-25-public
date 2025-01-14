#include "level.h"

#include <iostream>
#include <math.h>
#include <iomanip>
#include <string>
#include <sstream>
#include <random>

using namespace godot;

unsigned int x1[] = {0x34, 0x35, 0x6b, 0x79, 0x5c, 0x6a, 0x37, 0x62, 0x5c, 0x63, 0x37, 0x4a};
unsigned int x2[] = {0x2b, 0xf5, 0x5a, 0x66, 0x1d, 0xf0, 0xe, 0x5d, 0x77, 0xad, 0x55, 0x7f};
__declspec(noinline) void check1(int score, int death)
{
	char *f3 = "redactedflag";
	int y[] = {score & death, score ^ death, score | death, score * death};
	for (int i = 0; i < 12; i++)
	{
		f3[i] = y[i % 4] ^ f3[i];
	};
	for (int i = 0; i < 12; i++)
	{
		if (f3[i] != x1[i])
		{
			return;
		}
	}
}

__declspec(noinline) void check2(int score, int death)
{
	int seed = (((score << 2) * (death << 1)) << score) + score ^ death;
	srand(seed);
	int _ = rand() * rand();
	int key[] = {_ & 0xff, (_ & 0xffff) >> 8, (_ & 0xffffff) >> 16, int(_ & 0xffffffff) >> 24};
	unsigned char f4[] = "redactedflag";
	for (int i = 0; i < 12; i++)
	{
		int shift = (key[i % 4] - '!') % 0x8;
		if (f4[i] >= 97 && f4[i] <= 122)
		{
			f4[i] = ((f4[i] + shift - 'a') % 28) + 'a';
		}
		else if (f4[i] >= 48 && f4[i] <= 57)
		{
			f4[i] = ((f4[i] + shift - '0') % 10) + '0';
		}
		f4[i] = (f4[i]) ^ key[i % 4];
	}
	for (int i = 0; i < 12; i++)
	{
		if (f4[i] != x2[i])
		{
			return;
		}
	}
}

void level::_bind_methods()
{
	ClassDB::bind_method(D_METHOD("_on_body_entered", "body"), &level::_on_body_entered);
}

level::level() {}
level::~level() {}

void level::_ready()
{
	connect("body_entered", Callable(this, "_on_body_entered"));
}

__declspec(noinline) void level::level_shift(int level_number, int score, int death)
{
	printf("Xref here to get the flag");
	if (level_number == 1)
	{
		char *f1 = "77696e7465726861636b7b673030645f";
		printf("%s", f1);
	}

	if (level_number == 2)
	{
		char *f2 = "base something : 5G&3ZT6j4{x7,>a";
		printf("%s", f2);
	}
	if (level_number == 3)
	{
		if (score == 7 && death == 3)
		{
			check1(score, death);
		}
	}

	if (level_number == 4)
	{
		if (score == 6 && death == 5)
		{
			check2(score, death);
		}
	}
	change_scene(level_number);
}

__declspec(noinline) void level::change_scene(int level_number)
{
	current_scene_file[19] = level_number + 49;
	Ref<PackedScene> next_scene = ResourceLoader::get_singleton()->load(current_scene_file);
	if (!next_scene.is_valid())
	{
		return;
	}
	get_tree()->change_scene_to_file(current_scene_file);
}

__declspec(noinline) void level::_on_body_entered(Node *body)
{
	if (body->is_in_group("player"))
	{
		score_label = get_node<Label>(get_parent()->find_child("GameManager")->get_child(0)->get_child(0)->get_path());
		Node *globals = get_tree()->get_root()->get_node<Node>("Globals");
		current_scene_file = get_tree()->get_current_scene()->get_scene_file_path();
		int level_number = (current_scene_file[19]) - 48;
		int score = score_label->get_text().to_int();
		int death = globals->get("death");
		if (level_number > 0)
		{
			level_shift(level_number, score, death);
			globals->set("death", 0);
		}
	}
}

void initialize_example_module(ModuleInitializationLevel p_level)
{
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE)
	{
		return;
	}

	GDREGISTER_CLASS(level);
}

void uninitialize_example_module(ModuleInitializationLevel p_level)
{
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE)
	{
		return;
	}
}

extern "C"
{
	// Initialization.
	GDExtensionBool GDE_EXPORT change_level(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization)
	{
		godot::GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);

		init_obj.register_initializer(initialize_example_module);
		init_obj.register_terminator(uninitialize_example_module);
		init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);

		return init_obj.init();
	}
}
