#include "Graphs.h"



Graph * create_tbsc(void) {
	Graph * tbsc = (Graph *) malloc(sizeof(Graph));
	tbsc->num_states = 3;
	State * state_1 = (State *) malloc(sizeof(State));
	state_1->num_state = 1;

	State * state_2 = (State *) malloc(sizeof(State));
	state_2->num_state = 2;

	State * state_3 = (State *) malloc(sizeof(State));
	state_3->num_state = 3;

	state_1->not_taken = state_1;
	state_1->taken = state_2;
	state_2->not_taken = state_1;
	state_2->taken = state_3;
	state_3->not_taken = state_2;
	state_3->taken = state_3;
	tbsc->head = state_1;

	return tbsc;
}

void running_graph(Graph * graph, int taken) {
	if (taken == 1) {
		graph->head = graph->head->taken;
	} else {
		graph->head = graph->head->not_taken;
	}
}