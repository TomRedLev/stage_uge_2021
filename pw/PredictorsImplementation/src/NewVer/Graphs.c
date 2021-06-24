#include "Graphs.h"



Graph * create_tbsc(void) {
	Graph * tbsc = (Graph *) malloc(sizeof(Graph));

	tbsc->nb_states = 4;

	tbsc->current_state = 1;

	tbsc->states = (State *) malloc(sizeof(State) * tbsc->nb_states);

	tbsc->states[0].state = 0;
	tbsc->states[0].taken_state = 0;
	tbsc->states[0].not_taken = 0;
	tbsc->states[0].taken = 1;

	tbsc->states[1].state = 1;
	tbsc->states[1].taken_state = 0;
	tbsc->states[1].not_taken = 0;
	tbsc->states[1].taken = 2;

	tbsc->states[2].state = 2;
	tbsc->states[2].taken_state = 1;
	tbsc->states[2].not_taken = 1;
	tbsc->states[2].taken = 3;

	tbsc->states[3].state = 3;
	tbsc->states[3].taken_state = 1;
	tbsc->states[3].not_taken = 2;
	tbsc->states[3].taken = 3;

	return tbsc;
}

void running_graph(Graph * graph, int taken) {
	if (taken == 1) {
		graph->current_state = graph->states[graph->current_state].taken;
	} else {
		graph->current_state = graph->states[graph->current_state].not_taken;
	}
}

int check_current_state(Graph * graph) {
	return graph->current_state;
}

int evolving_graph(Graph * graph, int comp, int * misp) {
	if (check_current_state(graph) == 1) {
		if (comp) {
			running_graph(graph, 1);
		} else {
			running_graph(graph, 0);
            *misp += 1;
		}
	} else {
        if (comp) {
            running_graph(graph, 1);
            *misp += 1;
        } else {
            running_graph(graph, 0);
        }
    }
    return comp;
}