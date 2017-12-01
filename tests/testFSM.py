import unittest
import fsm.state_machine as fsm


class TestCreateFSM(unittest.TestCase):
    def test_create_state_machine(self):
        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized","start","finish"]
        transitions=[]
        transitions.append(["IDLE","initialized","READY"])
        transitions.append(["READY", "start", "RUNNING"])
        transitions.append(["RUNNING", "finish", "IDLE"])
        self.state_machine = fsm.StateMachine(states,initial_state, events, transitions)

        self.assertEqual(self.state_machine.initialState, "IDLE")
        self.assertEqual(len(self.state_machine._states), 3)
        self.assertEqual(len(self.state_machine._events), 3)
        self.assertEqual(self.state_machine.currentState, None)

    def test_start_FSM(self):
        states = ["READY", "RUNNING", "IDLE"]
        initial_state = "IDLE"
        events = ["initialized", "start", "finish"]
        transitions = []
        transitions.append(["IDLE", "initialized", "READY"])
        transitions.append(["READY", "start", "RUNNING"])
        transitions.append(["RUNNING", "finish", "IDLE"])
        self.state_machine = fsm.StateMachine(states, initial_state, events, transitions)

        self.assertEqual(self.state_machine.started, False)
        self.state_machine.startFSM()
        self.assertEqual(self.state_machine.currentState.name, "IDLE")
        self.assertEqual(self.state_machine.started, True)
if __name__ == '__main__':
    unittest.main()
