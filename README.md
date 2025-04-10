# OpenMaestro

Orchestrating multi-agent collaboration through a shared plan and event stream!
This is an extension of OpenManus.

## Installation

1. Clone the repository:
2. Create Python virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

Update the `config.toml` file in the `config` directory to add your API keys and customize settings.

Note that the repository is configured to mock the actual LLM calls (for simplicity and avoiding cost), by replaying answers that were collected earlier.
To do actual LLM calls, update app/llm.py and set useMock to False.

## Quick Start

One line to run the predefined example:

```bash
python run_alternate1.py
```

You should see an output like this:

````bash
2025-03-19 12:20:57.470 | INFO     | __main__:run_flow:20 - Created agent planning
2025-03-19 12:20:57.471 | INFO     | __main__:run_flow:20 - Created agent Maestro
2025-03-19 12:20:57.471 | WARNING  | __main__:run_flow:34 - Processing your request...
2025-03-19 12:20:57.471 | INFO     | app.flow.alternate:execute:32 - Executing AlternateFlow 0
2025-03-19 12:20:57.471 | INFO     | app.flow.alternate:execute:38 - Executing agent planning
2025-03-19 12:20:57.472 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-19 12:21:05.273 | INFO     | app.agent.toolcall:think:54 - ✨ planning's thoughts: None
2025-03-19 12:21:05.274 | INFO     | app.agent.toolcall:think:55 - 🛠️ planning selected 1 tools to use
2025-03-19 12:21:05.274 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['planning']
2025-03-19 12:21:05.275 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'planning'...
2025-03-19 12:21:05.276 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'planning' completed its mission! Result: Observed output of cmd `planning` executed:
Plan created successfully with ID: plan_10005632

Plan: Save Organizational Structure Reporting to MarkL (ID: plan_10005632)
===========================================================================

Progress: 0/3 steps completed (0.0%)
Status: 0 completed, 1 in progress, 0 blocked, 2 not started

Steps:
0. [→] Identify the organizational structure and list everyone reporting to MarkL.
1. [ ] Organize the information in a structured format suitable for a text file.
2. [ ] Save the organized information into a text file.

2025-03-19 12:21:05.276 | INFO     | app.flow.alternate:execute:38 - Executing agent Maestro
2025-03-19 12:21:05.277 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-19 12:21:19.265 | INFO     | app.agent.toolcall:think:54 - ✨ Maestro's thoughts: None
2025-03-19 12:21:19.266 | INFO     | app.agent.toolcall:think:55 - 🛠️ Maestro selected 1 tools to use
2025-03-19 12:21:19.266 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['data_lookup']
2025-03-19 12:21:19.267 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'data_lookup'...
2025-03-19 12:21:19.267 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'data_lookup' completed its mission! Result: Observed output of cmd `data_lookup` executed:

            Kris Verlaenen reports to Mark Proctor
            Mark Proctor reports to Mark Little
            Ricardo Zanini reports to David Gutierrez
            Francisco Javier Tirado Sarti reports to David Gutierrez
            David Gutierrez reports to Mark Little
            Mario Fusco reports to Marek Novotny
            Marek reports to Mark Little

2025-03-19 12:21:19.268 | INFO     | app.flow.alternate:execute:32 - Executing AlternateFlow 1
2025-03-19 12:21:19.268 | INFO     | app.flow.alternate:execute:38 - Executing agent planning
2025-03-19 12:21:19.269 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-19 12:21:26.189 | INFO     | app.agent.toolcall:think:54 - ✨ planning's thoughts: None
2025-03-19 12:21:26.189 | INFO     | app.agent.toolcall:think:55 - 🛠️ planning selected 1 tools to use
2025-03-19 12:21:26.190 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['planning']
2025-03-19 12:21:26.190 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'planning'...
2025-03-19 12:21:26.191 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'planning' completed its mission! Result: Observed output of cmd `planning` executed:
Step 0 updated in plan 'plan_10005632'.

Plan: Save Organizational Structure Reporting to MarkL (ID: plan_10005632)
===========================================================================

Progress: 1/3 steps completed (33.3%)
Status: 1 completed, 1 in progress, 0 blocked, 1 not started

Steps:
0. [✓] Identify the organizational structure and list everyone reporting to MarkL.
   Notes: Identified the organizational structure and listed everyone reporting to MarkL.
1. [→] Organize the information in a structured format suitable for a text file.
2. [ ] Save the organized information into a text file.

2025-03-19 12:21:26.191 | INFO     | app.flow.alternate:execute:38 - Executing agent Maestro
2025-03-19 12:21:26.192 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-19 12:21:31.743 | INFO     | app.agent.toolcall:think:54 - ✨ Maestro's thoughts: The next step is to organize the information in a structured format suitable for a text file. Here's how the information can be structured:

```
Organizational Structure Reporting to Mark Little:

1. Mark Proctor
   - Kris Verlaenen

2. David Gutierrez
   - Ricardo Zanini
   - Francisco Javier Tirado Sarti

3. Marek Novotny
   - Mario Fusco
```

This format clearly shows the hierarchy and the reporting lines under Mark Little.

I will now proceed to mark this step as completed.
2025-03-19 12:21:31.743 | INFO     | app.agent.toolcall:think:55 - 🛠️ Maestro selected 0 tools to use
2025-03-19 12:21:31.743 | INFO     | app.flow.alternate:execute:32 - Executing AlternateFlow 2
2025-03-19 12:21:31.744 | INFO     | app.flow.alternate:execute:38 - Executing agent planning
2025-03-19 12:21:31.744 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-19 12:21:36.217 | INFO     | app.agent.toolcall:think:54 - ✨ planning's thoughts: None
2025-03-19 12:21:36.217 | INFO     | app.agent.toolcall:think:55 - 🛠️ planning selected 1 tools to use
2025-03-19 12:21:36.218 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['planning']
2025-03-19 12:21:36.218 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'planning'...
2025-03-19 12:21:36.219 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'planning' completed its mission! Result: Observed output of cmd `planning` executed:
Step 1 updated in plan 'plan_10005632'.

Plan: Save Organizational Structure Reporting to MarkL (ID: plan_10005632)
===========================================================================

Progress: 2/3 steps completed (66.7%)
Status: 2 completed, 1 in progress, 0 blocked, 0 not started

Steps:
0. [✓] Identify the organizational structure and list everyone reporting to MarkL.
   Notes: Identified the organizational structure and listed everyone reporting to MarkL.
1. [✓] Organize the information in a structured format suitable for a text file.
   Notes: Organized the information in a structured format suitable for a text file.
2. [→] Save the organized information into a text file.

2025-03-19 12:21:36.219 | INFO     | app.flow.alternate:execute:38 - Executing agent Maestro
2025-03-19 12:21:36.219 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-19 12:21:39.099 | INFO     | app.agent.toolcall:think:54 - ✨ Maestro's thoughts: None
2025-03-19 12:21:39.100 | INFO     | app.agent.toolcall:think:55 - 🛠️ Maestro selected 1 tools to use
2025-03-19 12:21:39.100 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['file_saver']
2025-03-19 12:21:39.101 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'file_saver'...
2025-03-19 12:21:39.108 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'file_saver' completed its mission! Result: Observed output of cmd `file_saver` executed:
Content successfully saved to organizational_structure_markl.txt
2025-03-19 12:21:39.108 | INFO     | app.flow.alternate:execute:32 - Executing AlternateFlow 3
2025-03-19 12:21:39.108 | INFO     | app.flow.alternate:execute:38 - Executing agent planning
2025-03-19 12:21:39.109 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-19 12:21:42.940 | INFO     | app.agent.toolcall:think:54 - ✨ planning's thoughts: None
2025-03-19 12:21:42.941 | INFO     | app.agent.toolcall:think:55 - 🛠️ planning selected 1 tools to use
2025-03-19 12:21:42.941 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['planning']
2025-03-19 12:21:42.942 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'planning'...
2025-03-19 12:21:42.942 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'planning' completed its mission! Result: Observed output of cmd `planning` executed:
Step 2 updated in plan 'plan_10005632'.

Plan: Save Organizational Structure Reporting to MarkL (ID: plan_10005632)
===========================================================================

Progress: 3/3 steps completed (100.0%)
Status: 3 completed, 0 in progress, 0 blocked, 0 not started

Steps:
0. [✓] Identify the organizational structure and list everyone reporting to MarkL.
   Notes: Identified the organizational structure and listed everyone reporting to MarkL.
1. [✓] Organize the information in a structured format suitable for a text file.
   Notes: Organized the information in a structured format suitable for a text file.
2. [✓] Save the organized information into a text file.
   Notes: Saved the organized information into a text file named 'organizational_structure_markl.txt'.

2025-03-19 12:21:42.943 | INFO     | __main__:run_flow:43 - Request processed in 45.47 seconds
````

You can also try the second scenario:

```bash
python run_alternate2.py
```

You should see an output like this:

````bash
2025-03-25 23:47:57.421 | INFO     | app.llm:__init__:61 - Initializing llm meta-llama/Llama-3.1-8B-Instruct
2025-03-25 23:47:57.440 | INFO     | app.llm:__init__:61 - Initializing llm gpt-4o
2025-03-25 23:47:57.444 | WARNING  | __main__:run_flow:37 - Processing your request...
2025-03-25 23:47:57.444 | INFO     | app.agent.planning:load_plan_definition:108 - Found plan definition Plan: Plan definition for getting organizational structure
===========================================================

Steps:
[ ] Identify the organizational structure and list everyone reporting to the selected user.
[ ] [mini_maestro] Organize the information in a structured format suitable for a text file.
[ ] Save the organized information into a text file named 'red_hat_organizational_structure.md'.

2025-03-25 23:47:57.444 | INFO     | app.flow.alternate:execute:37 - Executing AlternateFlow 0
2025-03-25 23:47:57.444 | INFO     | app.flow.alternate:execute:42 - Executing planning agent
2025-03-25 23:47:57.444 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-25 23:48:15.704 | INFO     | app.agent.toolcall:think:54 - ✨ planning's thoughts: The plan is sufficient as it clearly outlines the steps needed to accomplish the task. However, the plan has not been created yet. The next action is to create the plan using the provided steps.

I'll proceed to create the plan.
2025-03-25 23:48:15.705 | INFO     | app.agent.toolcall:think:55 - 🛠️ planning selected 1 tools to use
2025-03-25 23:48:15.705 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['planning']
2025-03-25 23:48:15.705 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'planning'...
2025-03-25 23:48:15.705 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'planning' completed its mission! Result: Observed output of cmd `planning` executed:
Plan created successfully with ID: plan_10005632

Plan: Plan definition for getting organizational structure (ID: plan_10005632)
===============================================================================

Progress: 0/3 steps completed (0.0%)
Status: 0 completed, 1 in progress, 0 blocked, 2 not started

Steps:
0. [→] Identify the organizational structure and list everyone reporting to the selected user.
1. [ ] [mini_maestro] Organize the information in a structured format suitable for a text file.
2. [ ] Save the organized information into a text file named 'red_hat_organizational_structure.md'.

2025-03-25 23:48:15.706 | INFO     | app.flow.alternate:execute:59 - Executing agent Maestro
2025-03-25 23:48:15.706 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-25 23:48:18.073 | INFO     | app.agent.toolcall:think:54 - ✨ Maestro's thoughts: None
2025-03-25 23:48:18.073 | INFO     | app.agent.toolcall:think:55 - 🛠️ Maestro selected 1 tools to use
2025-03-25 23:48:18.073 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['data_lookup']
2025-03-25 23:48:18.074 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'data_lookup'...
2025-03-25 23:48:18.074 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'data_lookup' completed its mission! Result: Observed output of cmd `data_lookup` executed:

            Kris Verlaenen reports to Mark Proctor
            Mark Proctor reports to Mark Little
            Ricardo Zanini reports to David Gutierrez
            Francisco Javier Tirado Sarti reports to David Gutierrez 
            David Gutierrez reports to Mark Little
            Mario Fusco reports to Marek Novotny
            Marek reports to Mark Little
            
2025-03-25 23:48:18.074 | INFO     | app.flow.alternate:execute:37 - Executing AlternateFlow 1
2025-03-25 23:48:18.074 | INFO     | app.flow.alternate:execute:42 - Executing planning agent
2025-03-25 23:48:18.075 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-25 23:48:19.281 | INFO     | app.agent.toolcall:think:54 - ✨ planning's thoughts: None
2025-03-25 23:48:19.281 | INFO     | app.agent.toolcall:think:55 - 🛠️ planning selected 1 tools to use
2025-03-25 23:48:19.281 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['planning']
2025-03-25 23:48:19.281 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'planning'...
2025-03-25 23:48:19.281 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'planning' completed its mission! Result: Observed output of cmd `planning` executed:
Step 0 updated in plan 'plan_10005632'.

Plan: Plan definition for getting organizational structure (ID: plan_10005632)
===============================================================================

Progress: 1/3 steps completed (33.3%)
Status: 1 completed, 1 in progress, 0 blocked, 1 not started

Steps:
0. [✓] Identify the organizational structure and list everyone reporting to the selected user.
   Notes: Identified the organizational structure and listed everyone reporting to MarkL.
1. [→] [mini_maestro] Organize the information in a structured format suitable for a text file.
2. [ ] Save the organized information into a text file named 'red_hat_organizational_structure.md'.

2025-03-25 23:48:19.282 | INFO     | app.flow.alternate:execute:55 - Found task type mini_maestro and agent Mini-Maestro
2025-03-25 23:48:19.282 | INFO     | app.flow.alternate:execute:59 - Executing agent Mini-Maestro
2025-03-25 23:48:19.282 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-25 23:48:28.266 | INFO     | app.agent.toolcall:think:54 - ✨ Mini-Maestro's thoughts: **Organizational Structure for MarkL**
=====================================

*   **Line Manager:** Mark Little
*   **Reports:**
    * Kris Verlaenen
    * Mark Proctor
    * Ricardo Zanini
    * Francisco Javier Tirado Sarti
    * David Gutierrez
    * Mario Fusco
    * Marek
2025-03-25 23:48:28.267 | INFO     | app.agent.toolcall:think:55 - 🛠️ Mini-Maestro selected 0 tools to use
2025-03-25 23:48:28.267 | INFO     | app.flow.alternate:execute:37 - Executing AlternateFlow 2
2025-03-25 23:48:28.267 | INFO     | app.flow.alternate:execute:42 - Executing planning agent
2025-03-25 23:48:28.267 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-25 23:48:32.060 | INFO     | app.agent.toolcall:think:54 - ✨ planning's thoughts: None
2025-03-25 23:48:32.060 | INFO     | app.agent.toolcall:think:55 - 🛠️ planning selected 1 tools to use
2025-03-25 23:48:32.061 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['planning']
2025-03-25 23:48:32.061 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'planning'...
2025-03-25 23:48:32.061 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'planning' completed its mission! Result: Observed output of cmd `planning` executed:
Step 1 updated in plan 'plan_10005632'.

Plan: Plan definition for getting organizational structure (ID: plan_10005632)
===============================================================================

Progress: 2/3 steps completed (66.7%)
Status: 2 completed, 1 in progress, 0 blocked, 0 not started

Steps:
0. [✓] Identify the organizational structure and list everyone reporting to the selected user.
   Notes: Identified the organizational structure and listed everyone reporting to MarkL.
1. [✓] [mini_maestro] Organize the information in a structured format suitable for a text file.
   Notes: Organized the information in a structured format suitable for a text file.
2. [→] Save the organized information into a text file named 'red_hat_organizational_structure.md'.

2025-03-25 23:48:32.061 | INFO     | app.flow.alternate:execute:59 - Executing agent Maestro
2025-03-25 23:48:32.062 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-25 23:48:33.450 | INFO     | app.agent.toolcall:think:54 - ✨ Maestro's thoughts: None
2025-03-25 23:48:33.450 | INFO     | app.agent.toolcall:think:55 - 🛠️ Maestro selected 1 tools to use
2025-03-25 23:48:33.451 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['file_saver']
2025-03-25 23:48:33.451 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'file_saver'...
2025-03-25 23:48:33.453 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'file_saver' completed its mission! Result: Observed output of cmd `file_saver` executed:
Content successfully saved to red_hat_organizational_structure.md
2025-03-25 23:48:33.454 | INFO     | app.flow.alternate:execute:37 - Executing AlternateFlow 3
2025-03-25 23:48:33.454 | INFO     | app.flow.alternate:execute:42 - Executing planning agent
2025-03-25 23:48:33.454 | INFO     | app.agent.base:run:137 - Executing step 1/1
Press enter to continue
2025-03-25 23:48:37.498 | INFO     | app.agent.toolcall:think:54 - ✨ planning's thoughts: None
2025-03-25 23:48:37.498 | INFO     | app.agent.toolcall:think:55 - 🛠️ planning selected 1 tools to use
2025-03-25 23:48:37.498 | INFO     | app.agent.toolcall:think:59 - 🧰 Tools being prepared: ['planning']
2025-03-25 23:48:37.498 | INFO     | app.agent.toolcall:execute_tool:145 - 🔧 Activating tool: 'planning'...
2025-03-25 23:48:37.498 | INFO     | app.agent.toolcall:act:118 - 🎯 Tool 'planning' completed its mission! Result: Observed output of cmd `planning` executed:
Step 2 updated in plan 'plan_10005632'.

Plan: Plan definition for getting organizational structure (ID: plan_10005632)
===============================================================================

Progress: 3/3 steps completed (100.0%)
Status: 3 completed, 0 in progress, 0 blocked, 0 not started

Steps:
0. [✓] Identify the organizational structure and list everyone reporting to the selected user.
   Notes: Identified the organizational structure and listed everyone reporting to MarkL.
1. [✓] [mini_maestro] Organize the information in a structured format suitable for a text file.
   Notes: Organized the information in a structured format suitable for a text file.
2. [✓] Save the organized information into a text file named 'red_hat_organizational_structure.md'.
   Notes: Saved the organized information into a text file named 'red_hat_organizational_structure.md'.

2025-03-25 23:48:37.499 | INFO     | __main__:run_flow:46 - Request processed in 40.05 seconds
````