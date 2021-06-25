#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class State(object):
	def __init__(self, state, taken_state, not_taken, taken):
		"""
		"""
		self.state = state
		self.taken_state = taken_state
		self.not_taken = not_taken
		self.taken = taken


class Graph(object):
	def __init__(self, nb_states, current_state, states):
		"""
		"""
		self.nb_states = nb_states
		self.current_state = current_state
		self.states = states
		self.mispredictions = 0

	def running_graph(graph, taken) :
		"""
		"""
		if (taken == 1) :
			graph.current_state = graph.states[graph.current_state].taken
		else :
			graph.current_state = graph.states[graph.current_state].not_taken

	def check_current_state(graph) :
		"""
		"""
		return graph.current_state

	def evolving_graph(graph, comp) :
		"""
		"""
		if (graph.check_current_state()) :
			if (comp) :
				graph.running_graph(1)
			else :
				graph.running_graph(0)
				graph.mispredictions += 1;
		else :
			if (comp) :
				graph.running_graph(1)
				graph.mispredictions += 1;
			else :
				graph.running_graph(0)
		return comp


def create_tbsc() :
	"""
	"""
	states = [State(0, 0, 0, 1), State(1, 0, 0, 2), State(2, 1, 1, 3), State(3, 1, 2, 3)]
	return Graph(4, 1, states);