#ifndef _GRAPHS_H_
#define _GRAPHS_H_

#include <stdlib.h>
#include <stdio.h>
#include <time.h>


typedef struct state {
	int num_state;
	int taken_state; /* If 1 : Taken, else : Not Taken */
	struct state * taken;
	struct state * not_taken;	
} State;

typedef struct graph {
	int num_states;
	State * head;
} Graph;

Graph * create_tbsc(void);
void running_graph(Graph * graph, int taken);
int check_current_state(Graph * graph);

#endif
