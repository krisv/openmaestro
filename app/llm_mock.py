import threading

MOCK_TOOL_RESPONSES = { 
    "scenario1": {
        "gpt-4o": [
            # PlanningAgent: create plan
            r"""ChatCompletion(id='replay-BCQrdZ1d25KWxkoO5AJ9TfypIA9mE', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_DDkLV5q8GUjfpSq1KtakwnCj', function=Function(arguments='{"command":"create","plan_id":"plan_10005632","title":"Save Organizational Structure Reporting to MarkL","steps":["Identify the organizational structure and list everyone reporting to MarkL.","Organize the information in a structured format suitable for a text file.","Save the organized information into a text file."]}', name='planning'), type='function')]))], created=1742302901, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_90d33c15d4')""",
            # MaestroAgent: data_lookup
            r"""ChatCompletion(id='replay-BCRt4HEN6yLGrNCrjnl9qBzspuaID', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_YSmAUS7HCcgprM6AmS2QKsYj', function=Function(arguments='{"source":"organizational_database","query":"everyone reporting to MarkL"}', name='data_lookup'), type='function')]))], created=1742306834, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_f9f4fb6dbf')""",
            # PlanningAgent: complete step 0
            r"""ChatCompletion(id='replay-BCS1XXKcDb5MTtqvL8d0m5tauJKsb', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_Y6UxWLoKSkMn60rRUe33PaAr', function=Function(arguments='{"command":"mark_step","plan_id":"plan_10005632","step_index":0,"step_status":"completed","step_notes":"Identified the organizational structure and listed everyone reporting to MarkL."}', name='planning'), type='function')]))], created=1742307359, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_90d33c15d4')""",
            # MaestroAgent: create information structure
            r"""ChatCompletion(id='replay-BCS93lB66hME7CkjTk3r0HFnEaJ0B', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content="The next step is to organize the information in a structured format suitable for a text file. Here's how the information can be structured:\n\n```\nOrganizational Structure Reporting to Mark Little:\n\n1. Mark Proctor\n   - Kris Verlaenen\n\n2. David Gutierrez\n   - Ricardo Zanini\n   - Francisco Javier Tirado Sarti\n\n3. Marek Novotny\n   - Mario Fusco\n```\n\nThis format clearly shows the hierarchy and the reporting lines under Mark Little. \n\nI will now proceed to mark this step as completed.", refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[]))], created=1742307825, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_f9f4fb6dbf')""",
            # PlanningAgent: complete step 1
            r"""ChatCompletion(id='replay-BCSDlz4Q1vR4nRb3CthOp5em5vNv9', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_TioVg58h1RKKHTfa3z3UGqTg', function=Function(arguments='{"command":"mark_step","plan_id":"plan_10005632","step_index":1,"step_status":"completed","step_notes":"Organized the information in a structured format suitable for a text file."}', name='planning'), type='function')]))], created=1742308117, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_90d33c15d4')""",
            # MaestroAgent: create file
            r"""ChatCompletion(id='replay-BCSEwGOwdyDmoaKfG06dc3jp60XpY', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_aG57W18yeIzzVpblhNojDr6D', function=Function(arguments='{"content":"Organizational Structure Reporting to Mark Little:\\n\\n1. Mark Proctor\\n   - Kris Verlaenen\\n\\n2. David Gutierrez\\n   - Ricardo Zanini\\n   - Francisco Javier Tirado Sarti\\n\\n3. Marek Novotny\\n   - Mario Fusco","file_path":"organizational_structure_markl.txt"}', name='file_saver'), type='function')]))], created=1742308190, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_f9f4fb6dbf')""",
            # PlanningAgent: complete step 2
            r"""ChatCompletion(id='replay-BCSHqOsV7BmPx8t7e7SJIZKV7aTsT', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_NFjJnG2ZvzMz7QoI1cek0mHF', function=Function(arguments='{"command":"mark_step","plan_id":"plan_10005632","step_index":2,"step_status":"completed","step_notes":"Saved the organized information into a text file named \'organizational_structure_markl.txt\'."}', name='planning'), type='function')]))], created=1742308370, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_90d33c15d4')"""
        ],
    },
    "scenario2": {
        "gpt-4o": [
            # When using predefined plan
            r"""ChatCompletion(id='replay-BExDqL0jmDlJltgL4Zx7PymfIF6Vb', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content="The plan is sufficient as it clearly outlines the steps needed to accomplish the task. However, the plan has not been created yet. The next action is to create the plan using the provided steps.\n\nI'll proceed to create the plan.", refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_bQivIP8Sji7qsJx2FLQRIkvR', function=Function(arguments='{"command":"create","plan_id":"plan_10005632","title":"Plan definition for getting organizational structure","steps":["Identify the organizational structure and list everyone reporting to the selected user.","[mini_maestro] Organize the information in a structured format suitable for a text file.","Save the organized information into a text file named \'red_hat_organizational_structure.md\'."]}', name='planning'), type='function')]))], created=1742903942, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_90d33c15d4')""",
            # MaestroAgent: data_lookup
            r"""ChatCompletion(id='replay-BCRt4HEN6yLGrNCrjnl9qBzspuaID', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_YSmAUS7HCcgprM6AmS2QKsYj', function=Function(arguments='{"source":"organizational_database","query":"everyone reporting to MarkL"}', name='data_lookup'), type='function')]))], created=1742306834, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_f9f4fb6dbf')""",
            # PlanningAgent: complete step 0
            r"""ChatCompletion(id='replay-BCS1XXKcDb5MTtqvL8d0m5tauJKsb', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_Y6UxWLoKSkMn60rRUe33PaAr', function=Function(arguments='{"command":"mark_step","plan_id":"plan_10005632","step_index":0,"step_status":"completed","step_notes":"Identified the organizational structure and listed everyone reporting to MarkL."}', name='planning'), type='function')]))], created=1742307359, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_90d33c15d4')""",
            # Mini-MaestroAgent: create information structure is done by Llama model
            # PlanningAgent: complete step 1
            r"""ChatCompletion(id='replay-BCSDlz4Q1vR4nRb3CthOp5em5vNv9', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_TioVg58h1RKKHTfa3z3UGqTg', function=Function(arguments='{"command":"mark_step","plan_id":"plan_10005632","step_index":1,"step_status":"completed","step_notes":"Organized the information in a structured format suitable for a text file."}', name='planning'), type='function')]))], created=1742308117, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_90d33c15d4')""",
            # MaestroAgent: create file
            r"""ChatCompletion(id='chatcmpl-BF6mksYSKRBHxJv95cHe3BWym3rdZ', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_440TW0O1a9PGaZoOkCN1Pc9l', function=Function(arguments='{"content":"**Organizational Structure for MarkL**\\n=====================================\\n\\n*   **Line Manager:** Mark Little\\n*   **Reports:**\\n    * Kris Verlaenen\\n    * Mark Proctor\\n    * Ricardo Zanini\\n    * Francisco Javier Tirado Sarti\\n    * David Gutierrez\\n    * Mario Fusco\\n    * Marek","file_path":"red_hat_organizational_structure.md"}', name='file_saver'), type='function')]))], created=1742940702, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_6bb567654c')""",
            # PlanningAgent: complete step 2
            r"""ChatCompletion(id='chatcmpl-BF6mmnd4VrFKXZ8xgcbXITvz6iumB', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_ekp5dsgzW9HpUbUOQdn5J3RI', function=Function(arguments='{"command":"mark_step","plan_id":"plan_10005632","step_index":2,"step_status":"completed","step_notes":"Saved the organized information into a text file named \'red_hat_organizational_structure.md\'."}', name='planning'), type='function')]))], created=1742940704, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_90d33c15d4')"""
        ],
        "meta-llama/Llama-3.1-8B-Instruct": [
            # Mini-MaestroAgent: create information structure
            r"""ChatCompletion(id='chatcmpl-a559de43832541beabf121cfbadb04c2', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='**Organizational Structure for MarkL**\n=====================================\n\n*   **Line Manager:** Mark Little\n*   **Reports:**\n    * Kris Verlaenen\n    * Mark Proctor\n    * Ricardo Zanini\n    * Francisco Javier Tirado Sarti\n    * David Gutierrez\n    * Mario Fusco\n    * Marek', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[]), stop_reason=None)], created=1742914833, model='meta-llama/Llama-3.1-8B-Instruct', object='chat.completion', service_tier=None, system_fingerprint=None)""",
        ]
    },
}

class MockLLM:
    _instance = None
    _lock = threading.Lock()
    _scenario = None
    #_initialized = False

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def _get_mock_llm_message(self, model_name: str) -> dict:
        return MOCK_TOOL_RESPONSES[self._scenario][model_name]
    
    def _set_scenario(self, scenario: str):
        self._scenario = scenario

#    def __init__(self):
#        if not self._initialized:
#            with self._lock:
#                if not self._initialized:
#                    self._config = None
#                    self._load_initial_config()
#                    self._initialized = True

mockLLM = MockLLM()