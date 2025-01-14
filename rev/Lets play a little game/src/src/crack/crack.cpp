#include "crack.h"

#include <windows.h>
#include <string>
#include <iomanip>
#include <sstream>
// #include <iostream>

// Function to create a new window and display a message

using namespace godot;
using namespace std;

crack::crack() {}
crack::~crack() {}

int key[] = {0x84, 0x9e, 0x62, 0x8b, 0xe1, 0xc3, 0xf4};
int checker[] = { 0xed, 0xeb, 0x18, 0xed, 0x90, 0xa7, 0x80, 0xe9, 0xf1, 0x15, 0xf0, 0xd1, 0xb7, 0xc0, 0xbc, 0xc1, 0x56, 0xb3, 0xbe, 0xf4, 0xab, 0xbc, 0xaa, 0x1b, 0xe9, 0x99, 0xf5, 0xab, 0xeb, 0xfa, 0x55, 0xe4, 0x96, 0xba, 0xc2, 0xdb, 0xbf, 0x13, 0xec, 0xb9, 0xb0, 0xcd, 0xb4, 0xa8, 0x5a, 0xf6 };

__declspec(noinline) void create_console()
{
	AllocConsole();
	FILE *stream;
	freopen_s(&stream, "CONOUT$", "w", stdout);
	freopen_s(&stream, "CONIN$", "r", stdin);
	freopen_s(&stream, "CONOUT$", "w", stderr);
}


__declspec(noinline) bool check(unsigned char *a)
{
	int i = 0;
	while (a[i] != '\0')
	{
		if (a[i] > 64 && a[i] < 91)
			a[i] = (((a[i] - 65) + 18) % 26) + 65;
		else if (a[i] > 96 && a[i] < 123)
			a[i] = (((a[i] - 97) + 12) % 26) + 97;
		else if (a[i] > 47 && a[i] < 58)
			a[i] = (((a[i] - 48) + 13) % 10) + 48;
		a[i] = (a[i] ^ key[i % 7]);
		if(a[i]!=checker[i])
			return 0;
		i++;
	}
	return 1;
}

void crack::_bind_methods()
{
	ClassDB::bind_method(D_METHOD("crackme"), &crack::crackme);
}
void crack::crackme()
{
	create_console();

	unsigned char a[128];
	printf("Enter the password: ");
	scanf("%s", a);
	if (check(a))
		printf("You have unlocked the game\nNow close the console and enjoy the game\n");
	else{
		printf("Wrong password\n");
		FreeConsole();
		exit(0);
	}
	FreeConsole();
}

// Not to interfere area

void initialize_example_module(ModuleInitializationLevel p_level)
{
	if (p_level != MODULE_INITIALIZATION_LEVEL_SCENE)
	{
		return;
	}

	GDREGISTER_CLASS(crack);
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
	GDExtensionBool GDE_EXPORT crack_level(GDExtensionInterfaceGetProcAddress p_get_proc_address, const GDExtensionClassLibraryPtr p_library, GDExtensionInitialization *r_initialization)
	{
		godot::GDExtensionBinding::InitObject init_obj(p_get_proc_address, p_library, r_initialization);

		init_obj.register_initializer(initialize_example_module);
		init_obj.register_terminator(uninitialize_example_module);
		init_obj.set_minimum_library_initialization_level(MODULE_INITIALIZATION_LEVEL_SCENE);
		return init_obj.init();
	}
}