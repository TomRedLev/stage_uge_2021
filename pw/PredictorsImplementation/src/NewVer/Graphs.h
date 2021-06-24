#ifndef _GRAPHS_H_
#define _GRAPHS_H_

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

typedef struct {
	int state;
	int taken_state;
	int taken;
	int not_taken;
} State;

typedef struct graph {
	int nb_states;
	int current_state;
	State * states;
} Graph;

Graph * create_tbsc(void);
void running_graph(Graph * graph, int taken);
int check_current_state(Graph * graph);
int evolving_graph(Graph * graph, int comp, int * misp);

#endif
