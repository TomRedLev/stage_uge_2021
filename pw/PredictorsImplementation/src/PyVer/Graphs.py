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
		if (taken) :
			graph.current_state = graph.states[graph.current_state].taken
		else :
			graph.current_state = graph.states[graph.current_state].not_taken

	def check_current_state(graph) :
		"""
		"""
		return graph.states[graph.current_state].taken_state

	def evolving_graph(graph, comp) :
		"""
		"""
		if (graph.check_current_state()) :
			if (comp) :
				graph.running_graph(True)
			else :
				graph.running_graph(False)
				graph.mispredictions += 1
		else :
			if (comp) :
				graph.running_graph(True)
				graph.mispredictions += 1
			else :
				graph.running_graph(False)
		return comp


def create_obsc() :
	"""
	"""
	states = [State(0, False, 0, 1), State(1, True, 0, 1)]
	return Graph(2, 0, states)

def create_tbsc() :
	"""
	"""
	states = [State(0, False, 0, 1), State(1, False, 0, 2), State(2, True, 1, 3), State(3, True, 2, 3)]
	return Graph(4, 0, states)

def create_swapped() :
	states = [State(0, False, 0, 1), State(1, False, 0, 3), State(2, True, 0, 3), State(3, True, 2, 3)]
	return Graph(4, 0, states)
