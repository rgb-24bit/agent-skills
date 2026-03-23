---
name: llm-prompt-engineering
description: Provides systematic LLM prompt writing and optimization guidance; use when users need to create new prompts, optimize existing prompts, learn prompt engineering techniques, or improve prompt quality
---

# LLM Prompt Engineering Guide

## Task Objectives
- Help users write high-quality LLM prompts from scratch
- Analyze and optimize users' existing prompts
- Enhance users' prompt engineering capabilities and understanding
- Recommend appropriate prompt frameworks based on task complexity

## Capabilities
- Guide users step-by-step through prompt component design
- Diagnose deficiencies in existing prompts and provide optimization solutions
- Provide instructional explanations to help users understand underlying principles
- Select appropriate frameworks based on task requirements (CRISPE, RTF, RISE, etc.)

## Trigger Conditions
- User requests help writing, creating, designing, or building prompts
- User requests optimization, improvement, or enhancement of existing prompts
- User asks how to write better prompts or improve AI response quality
- User wants to learn prompt engineering methods or frameworks

## Operation Steps

### Scenario 1: Writing New Prompts

#### Step 1: Understand User Requirements
- Ask what problem the user wants to solve
- Clarify usage scenarios and target audience
- Understand expected output types and quality requirements
- Note: This is the first step in the instructional process, helping users clarify their goals

#### Step 2: Assess Task Complexity
Evaluate complexity based on the following characteristics:
- Does the task contain multiple sub-steps?
- Does it require specific domain knowledge?
- Are there strict format requirements?
- Does it involve complex reasoning or analysis?

**Decision**:
- Simple tasks (single objective, clear): Guide component design directly
- Complex tasks: Recommend using prompt frameworks

If recommending a framework, introduce options and guide selection:
- CRISPE: Suitable for complex tasks requiring comprehensive structure
- RTF: Suitable for medium-complexity tasks requiring clear roles and formats
- RISE: Suitable for tasks requiring systematic reasoning

Reference: [frameworks.md](references/frameworks.md) for framework details

#### Step 3: Step-by-Step Prompt Component Design

Guide users through component design in the following order (if using a framework, follow the framework sequence):

**3.1 Role Definition**
- Ask: What role should AI play? What expertise is needed?
- Guide: Consider using roles to adjust vocabulary, perspective, professional depth, and communication style
- Example: "You are a Python backend engineer with 10 years of experience"
- Note: Roles act like filters, focusing AI's knowledge base

**3.2 Context**
- Ask: What background information does AI need to know?
- Guide: Include project details, current state, objectives, constraints
- Example: "I'm developing an e-commerce API using Node.js and Express, with a team of 3 developers"
- Note: AI has no knowledge of the user's situation; all relevant context must be provided

**3.3 Task**
- Ask: What specifically should AI do? What action verbs to use?
- Guide: Use specific, clear verbs (analyze, create, explain, optimize, etc.)
- Example: "Review the following code, identify performance bottlenecks, and provide optimization suggestions"
- Note: The task is the core of the prompt; it must be specific and unambiguous

**3.4 Constraints**
- Ask: What limitations exist?
- Guide: Consider length constraints, content constraints, style constraints, scope constraints
- Example: "Keep response under 300 words, use technical terminology but avoid excessive complexity"
- Note: Constraints prevent common issues and ensure output relevance

**3.5 Output Format**
- Ask: What format is expected for the output?
- Guide: Consider lists, tables, JSON, structured text, etc.
- Example: "Return in markdown table format with columns: Issue, Severity, Suggested Solution"
- Note: Clear formatting ensures output usability

**3.6 Examples**
- Ask: Can you provide input-output examples?
- Guide: Examples are the most powerful guidance method, demonstrating expected behavior patterns
- Example: "Input: User login failed. Output: Check password hash verification logic (line 45)"
- Note: Few-shot learning enables AI to precisely understand expectations through examples

Reference: [components.md](references/components.md) for detailed component descriptions

#### Step 4: Integration and Validation
- Integrate all components into a complete prompt
- Present the complete prompt to the user
- Explain the purpose and principles of each part line-by-line
- Ask if adjustments are needed
- Note: This is not just completing the prompt, but a teaching process

#### Step 5: Testing and Iteration Recommendations
- Suggest users test the prompt
- Provide iteration recommendations based on actual results
- Encourage users to record what works and what needs adjustment
- Note: Prompt engineering is an iterative process; first attempts are rarely perfect

### Scenario 2: Optimizing Existing Prompts

#### Step 1: Analyze Existing Prompt
Request the user to provide:
- Complete prompt text
- Usage scenario and objectives
- Current output effectiveness (or actual returned results)
- Specific aspects of dissatisfaction

#### Step 2: Diagnose Issues
Check for problems in the following areas:

**Completeness Check**:
- Is role definition missing?
- Is context sufficient?
- Is the task clear and specific?
- Are constraint conditions missing?
- Is output format specified?
- Are examples needed?

**Quality Check**:
- Is language clear and unambiguous?
- Are there ambiguities or multiple interpretations?
- Is sufficient context provided?
- Is the reasoning process guided?

Reference: [principles.md](references/principles.md) for core principles

#### Step 3: Provide Optimization Solutions
Based on diagnosis results, provide 1-3 optimization solutions:

**Solution Types**:
- Progressive optimization: Add missing components to the original
- Structured reconstruction: Reorganize using frameworks
- Targeted improvement: Adjust for specific issues

For each solution, explain:
- Main improvement points
- Expected effects
- Applicable scenarios

Reference: [optimization.md](references/optimization.md) for optimization techniques

#### Step 4: Selection and Implementation
- Guide user to choose the most suitable solution
- Implement the selected optimization
- Explain the principles of each change

#### Step 5: Iterative Optimization (Optional)
- Ask about effectiveness after actual use
- If actual results are provided, further analyze based on results
- Provide more refined adjustment suggestions
- Note: Optimization based on real feedback is most effective

### Scenario 3: Teaching and Learning
When users ask how to learn prompt engineering:
- Explain core concepts and principles
- Provide practice suggestions
- Recommend learning paths
- Encourage learning through practice

## Resource Index

### Essential Reference Documents
- [frameworks.md](references/frameworks.md) - Detailed prompt framework descriptions (CRISPE, RTF, RISE, etc.), read when framework selection is needed
- [components.md](references/components.md) - Detailed explanations of six core prompt components, reference during prompt design
- [principles.md](references/principles.md) - Eight core principles explanation, reference during problem analysis
- [optimization.md](references/optimization.md) - Optimization techniques and common issue diagnosis, reference during prompt optimization

## Key Guiding Principles

### Instructional Guidance
- Explain "why" for each step
- Use concrete examples to illustrate abstract concepts
- Encourage user thinking and questioning
- Enhance user understanding while completing prompts

### Progressive Approach
- Don't present all information at once
- Progressively deepen based on user responses
- Proceed to next step after user understands current concept
- Maintain natural conversation flow

### Practice-Oriented
- Encourage actual user testing
- Iterate based on real feedback
- Provide actionable recommendations
- Avoid pure theoretical explanations

### Personalized Adaptation
- Adjust guidance depth based on user background and needs
- For beginners: More explanations and examples
- For experienced users: Direct tips and optimization suggestions
- Respect user choices and preferences

## Important Notes

- The agent already possesses powerful language understanding and reasoning capabilities; no scripts needed for simple text analysis, content generation, etc.
- All work is completed through agent-user dialogue; no independent user interface exists
- Keep context concise; only read reference documents when needed
- Fully utilize the agent's professional knowledge; avoid over-reliance on fixed templates
- Encourage users to understand principles rather than mechanically apply templates

## Usage Examples

### Example 1: Writing Code Review Prompt (Simple Task)

**User**: Help me write a prompt for AI to review Python code

**Agent Guidance**:
1. Ask about review focus (performance, security, readability, etc.)
2. Guide role definition (senior Python development engineer)
3. Gather context (project type, team size, code standards)
4. Clarify task (identify issues and provide suggestions)
5. Set constraints (focus on specific aspects, output format)
6. Integrate complete prompt and explain each part

### Example 2: Writing Content Creation Prompt (Complex Task - Using Framework)

**User**: Help me write a prompt for AI to write blog articles

**Agent Guidance**:
1. Assess complexity: Multi-step task, recommend using CRISPE framework
2. Introduce CRISPE framework and guide selection
3. Progressively design according to framework sequence:
   - Capacity: AI as content marketing expert
   - Request: Write blog article
   - Information: Brand positioning, target audience, content topic
   - Situation: Publishing channel, competitive environment
   - Persona: Professional yet approachable writing style
   - Experiment: Provide sample paragraphs
4. Generate complete prompt with instruction

### Example 3: Optimizing Vague Prompt

**User**: This prompt isn't working well, help me check it

**Prompt**: Help me write a product introduction

**Agent Analysis**:
1. Diagnose issues: Missing role, context, constraints, format
2. Provide 3 optimization solutions:
   - Solution A: Add product information and target audience
   - Solution B: Restructure using RTF framework
   - Solution C: Create detailed marketing copy prompt
3. Guide user to select and implement
