#ifndef _GRAPHS_H_
#define _GRAPHS_H_

#include <stdlib.h>
#include <stdio.h>
#include <time.h>


typedef struct state {
	int num_state;
	struct state * taken;
	struct state * not_taken;	
} State;

typedef struct graph {
	int num_states;
	State * head;
} Graph;

Graph * create_tbsc(void);
void running_graph(Graph * graph, int taken);

#endif
