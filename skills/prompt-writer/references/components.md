# Prompt Core Components Guide

## Table of Contents
1. [Role/Persona](#rolepersona)
2. [Context/Background](#contextbackground)
3. [Task/Instruction](#taskinstruction)
4. [Constraints/Rules](#constraintsrules)
5. [Output Format](#output-format)
6. [Examples](#examples)

---

## Role/Persona

### Purpose
Role definition focuses response perspective, vocabulary, professional depth, and communication style by specifying the identity AI should assume.

### Why Important
- **Activate relevant knowledge domains**: Different roles activate different parts of AI's knowledge base
- **Unify response style**: Ensures consistency throughout the response
- **Adjust professional depth**: Controls the depth and breadth of technical details
- **Match audience level**: Enables AI to use appropriate language complexity

### Role Prompt Construction Patterns

#### Expert Pattern
```
You are a [domain] expert with [X] years of experience, specializing in [specific domain].

Example:
You are a machine learning expert with 10 years of experience, specializing in deep learning and natural language processing.
```

#### Professional Pattern
```
You are a [profession], working in [industry/organization type], focusing on [work content].

Example:
You are a product manager, working in a B2B SaaS company, focusing on user experience design for enterprise applications.
```

#### Teacher Pattern
```
You are a [subject] teacher, skilled at explaining complex concepts to [target audience], teaching style is [style characteristics].

Example:
You are a math teacher, skilled at explaining abstract algebra concepts to middle school students, teaching style is patient with many analogies.
```

#### Composite Role Pattern
```
You are a [Role A], also a [Role B]. You combine [A's strengths] and [B's strengths].

Example:
You are a psychologist, also a senior programmer. You combine psychological insights with engineering precision.
```

### Common Mistakes

**Mistake 1: Role too vague**
- ❌ "You are an expert"
- ✅ "You are a Python backend engineer with 8 years of experience, specializing in high-concurrency system design"

**Mistake 2: Role doesn't match task**
- ❌ Role is "poet", task is "review database design"
- ✅ Role is "database architect", task is "review database design"

**Mistake 3: Adding irrelevant role characteristics**
- ❌ "You are an AI teaching assistant, likes rock music, goes to gym three times a week"
- ✅ "You are an AI teaching assistant, skilled at explaining complex concepts, patient and encouraging students"

### Best Practices
1. **Be specific and clear**: Use specific professional titles and domain expertise
2. **Quantify experience**: Add years of experience to increase credibility
3. **Focus expertise**: Specify specialization areas, avoid generalizations
4. **Style characteristics**: Add communication style traits (patient, rigorous, humorous, etc.)
5. **Scenario connection**: Make the role relevant to actual use cases

---

## Context/Background

### Purpose
Provide all background information AI needs to complete the task, including project details, current state, objectives, and constraints.

### Why Important
- **AI has no memory**: Each conversation starts fresh
- **Eliminate ambiguity**: Background information helps AI accurately understand needs
- **Improve relevance**: Ensures responses are relevant to specific situations
- **Avoid assumptions**: Prevents AI from making wrong assumptions

### Context Checklist

Before providing context, check these questions:
- [ ] Does AI know what project I'm working on?
- [ ] Does AI understand my tech stack or tools?
- [ ] Does AI know my objectives and expectations?
- [ ] Does AI understand current constraints?
- [ ] Does AI know who the target audience is?
- [ ] Does AI understand the current state and progress?

### Context Components

#### Project Information
```
Project Type: [type]
Tech Stack: [technology list]
Team Size: [number of people]
Current Stage: [stage]
```

**Example**:
```
Project Information:
- Project Type: E-commerce website backend management system
- Tech Stack: React frontend + Node.js + PostgreSQL database
- Team Size: 5 developers
- Current Stage: MVP development phase, expected launch in 2 months
```

#### Current State
```
Completed: [what's done]
Current Challenges: [problems faced]
Objectives: [desired results]
```

**Example**:
```
Current State:
- Completed: User authentication module, product display module, shopping cart feature
- Current Challenges: Order processing flow has performance bottlenecks, response time exceeds 5 seconds under high concurrency
- Objectives: Optimize order processing time to under 1 second
```

#### Constraints
```
Technical Constraints: [technical limitations]
Time Constraints: [time limitations]
Resource Constraints: [resource limitations]
Business Constraints: [business rules]
```

**Example**:
```
Constraints:
- Technical Constraints: Must be compatible with IE11 browser
- Time Constraints: Need to complete optimization within 2 weeks
- Resource Constraints: Can only use existing database architecture, cannot add new tables
- Business Constraints: Cannot change existing order flow logic
```

#### Audience Information
```
Target Audience: [audience type]
Knowledge Level: [professional level]
Usage Scenario: [usage environment]
```

**Example**:
```
Audience Information:
- Target Audience: Junior developers, 1-3 months on the job
- Knowledge Level: Understands basic programming concepts, but unfamiliar with project architecture
- Usage Scenario: Learning project code during onboarding training
```

### Common Mistakes

**Mistake 1: Insufficient information**
- ❌ "Help me optimize this code"
- ✅ "This is a Python function processing user-uploaded images, needs memory optimization because server only has 4GB RAM"

**Mistake 2: Irrelevant information**
- ❌ "I'm 30 years old, have two children, live in Beijing" (irrelevant to code optimization)
- ✅ "This is an educational app, need to consider parents' privacy concerns"

**Mistake 3: Assuming AI knows**
- ❌ "Do it like before" (AI has no memory of previous conversations)
- ✅ "Reference standard REST API design patterns"

### Best Practices
1. **Provide sufficient but not redundant**: Enough information for understanding, avoid irrelevant details
2. **Structured presentation**: Use lists or sections to make information clear
3. **Clear boundaries**: Explain what can and cannot be done
4. **Specific metrics**: Provide specific numbers and metrics rather than vague descriptions
5. **Clear status**: Explicitly state current stage

---

## Task/Instruction

### Purpose
Clearly tell AI what specific operation to execute; this is the core of the prompt.

### Why Important
- **Directly determines output**: Task description quality directly affects result quality
- **Avoid misunderstanding**: Clear instructions prevent AI from doing wrong things
- **Set expectations**: Clearly know what to expect
- **Measurability**: Clear tasks facilitate result evaluation

### Task Design Principles

#### Use Specific Verbs
Avoid vague verbs, use precise action verbs:

| Vague Verbs | Precise Verbs |
|---------|---------|
| Help me | Analyze/Review/Optimize/Design |
| Process | Transform/Extract/Format/Filter |
| Write | Compose/Create/Summarize/Expand |
| Look at | Check/Evaluate/Compare/Diagnose |

#### Clarify Task Scope
Explain task boundaries and scope:
- What to do
- What not to do
- What to focus on

#### Specify Depth and Breadth
- **Depth**: How detailed? Overview/Detailed/In-depth analysis
- **Breadth**: What aspects to cover? Core only/Comprehensive/Specific angles

### Task Patterns

#### Creation Tasks
```
Create/Write/Generate/Design/Develop [target object]

Examples:
- Write a 500-word user manual
- Design a user flow for login page
- Generate 10 product ideas
```

#### Analysis Tasks
```
Analyze/Evaluate/Review/Diagnose/Compare [object] from [angle]

Examples:
- Analyze sentiment tendencies in user feedback
- Evaluate code security risks
- Compare pros and cons of two technical solutions
```

#### Transformation Tasks
```
 Transform/Translate/Format/Refactor [source object] to [target format]

Examples:
- Transform this text to JSON format
- Translate to Spanish, maintain technical accuracy
- Refactor to functional programming style
```

#### Problem-Solving Tasks
```
Solve/Fix/Debug/Optimize [problem]

Examples:
- Solve memory leak issue in this code
- Optimize database query performance
- Debug login failure causes
```

### Task Optimization Examples

**Original Task**:
```
Help me look at this prompt
```

**Optimized Version 1** (Clarify task type):
```
Review this prompt, identify areas for improvement
```

**Optimized Version 2** (Add focus areas):
```
Review this prompt, focusing on: 1) Are key components missing 2) Are there ambiguous expressions 3) Is output format clear
```

**Optimized Version 3** (Add depth and scope):
```
Deeply review this prompt, identify all areas for improvement. Analyze its clarity, completeness, effectiveness, and list improvement suggestions by priority.
```

### Common Mistakes

**Mistake 1: Vague task**
- ❌ "Help me process this"
- ✅ "Extract all email addresses from this text into a list"

**Mistake 2: Task scope too large**
- ❌ "Help me write a complete e-commerce website"
- ✅ "Design a shopping cart feature for an e-commerce website, including adding items, modifying quantities, calculating totals"

**Mistake 3: Missing specific standards**
- ❌ "Make it better"
- ✅ "Improve response speed by at least 50%"

### Best Practices
1. **Single and clear**: Each prompt focuses on one main task
2. **Actionable**: Use specific action verbs
3. **Measurable**: Set clear standards and metrics
4. **Layered**: Break down complex tasks into subtasks
5. **Bounded**: Clarify task scope and limitations

---

## Constraints/Rules

### Purpose
Set output limitations and rules to prevent common issues and ensure relevance.

### Why Important
- **Control output quality**: Avoid too long, too short, or off-topic
- **Ensure consistency**: Unify style and format
- **Prevent issues**: Avoid common errors and inappropriate content
- **Meet specific needs**: Align with business or technical requirements

### Constraint Types

#### Length Constraints
```
Keep response within [X words/X paragraphs]
Provide exactly [X] suggestions
Each suggestion not exceeding [X words]
```

**Example**:
```
- Keep response under 300 words
- Provide exactly 5 optimization suggestions
- Each explanation not exceeding 2 sentences
```

#### Content Constraints
```
Don't include [content type]
Only focus on [specific aspect]
Avoid [inappropriate content]
```

**Example**:
```
- Don't include code examples
- Only focus on performance optimization, not code readability
- Avoid overly technical terminology
```

#### Style Constraints
```
Use [formal/informal/academic/humorous] tone
Write in [first person/third person]
Use [simple/professional] language
```

**Example**:
```
- Use friendly, encouraging tone
- Write as a tutorial for beginners
- Use concise, clear language, avoid overly complex sentences
```

#### Format Constraints
```
Use [specific format]
Follow [style guide]
Don't use [specific elements]
```

**Example**:
```
- Use Markdown format
- Follow PEP 8 code standards
- Don't use emoji symbols
```

#### Scope Constraints
```
Only consider [condition]
Limit to [scope]
Exclude [content]
```

**Example**:
```
- Only consider Python 3.8+ syntax features
- Limit to free tools range
- Exclude solutions requiring additional dependencies
```

#### Logic Constraints
```
Organize by [order/structure]
Ensure [logic requirements]
Avoid [logic errors]
```

**Example**:
```
- Sort by importance from high to low
- Ensure each suggestion has specific implementation steps
- Avoid contradictory suggestions
```

### Constraint Combination Example

```markdown
Constraints:
- Length: Total response not exceeding 500 words
- Content: Only focus on user experience aspects, not technical implementation
- Style: Use concise, direct language
- Format: Use unordered list
- Scope: Only applicable to mobile scenarios
- Logic: Sort suggestions by implementation difficulty from easy to hard
```

### Common Mistakes

**Mistake 1: Too many constraints**
- ❌ 10+ constraints, AI struggles to satisfy all
- ✅ 3-5 key constraints

**Mistake 2: Conflicting constraints**
- ❌ "Keep concise but also detailed"
- ✅ "Concise but complete"

**Mistake 3: Unreasonable constraints**
- ❌ "Analyze the entire book, but response under 100 words"
- ✅ "Provide a 100-word summary of the entire book"

### Best Practices
1. **Clear priorities**: Most important constraints first
2. **Moderate quantity**: 3-5 key constraints sufficient
3. **Coordinate with each other**: Ensure constraints don't conflict
4. **Verifiable**: Constraints should be checkable and verifiable
5. **Flexibility**: Leave room for creative tasks

---

## Output Format

### Purpose
Specify what format and structure AI should use to present output.

### Why Important
- **Improve usability**: Structured output is easier to use
- **Facilitate processing**: Specific formats are easier for programs to process
- **Ensure completeness**: Structure ensures all required content is included
- **Facilitate comparison**: Unified format makes comparing multiple results easier

### Common Output Formats

#### List Format

**Unordered List**:
```
Use unordered list, each item brief and clear
```

**Ordered List**:
```
Use ordered list, each item includes [content requirements]
```

**Nested List**:
```
- Level 1 heading
  - Level 2 item
    - Level 3 detail
```

#### Structured Text

**Sectioned Structure**:
```
## Title
[Paragraph content]

### Subtitle
[Paragraph content]
```

**Paragraph Template**:
```
Structure your response as:
1. Overview (2-3 sentences)
2. Key Findings (3-5 points)
3. Detailed Analysis (2-3 sentences per point)
4. Conclusions and Recommendations (1-2 sentences)
```

#### Table Format

**Markdown Table**:
```
| Column 1 | Column 2 | Column 3 |
|-----|-----|-----|
| Content | Content | Content |
```

**Table Requirements**:
```
Return as table with columns:
- Column name 1: Description
- Column name 2: Description
- Column name 3: Description
```

#### Data Format

**JSON Format**:
```
Return valid JSON, no other text:
{
  "key1": "value1",
  "key2": "value2",
  "key3": ["item1", "item2"]
}
```

**YAML Format**:
```
key1: value1
key2:
  - item1
  - item2
```

#### Code Format

```
Wrap all code in ```code blocks```
Include necessary comments
Specify code language (python, javascript, etc.)
```

### Format Specification Techniques

#### Clear Structure Template
```
Please organize response in this structure:

## [Title 1]
[Content]

## [Title 2]
- [Point 1]
- [Point 2]

## [Title 3]
[Content]
```

#### Specify Each Part's Content
```
For each improvement suggestion provide:
1. Problem description (1 sentence)
2. Impact analysis (2-3 sentences)
3. Specific solution (step list)
4. Expected effect (1 sentence)
```

#### Add Format Requirements
```
- Use Markdown format
- Use **bold** for key terms
- Use `inline code` or code blocks for code
- Empty line between paragraphs
```

### Format Examples

**Simple List Format**:
```
Return as unordered list with 5 best practices, each not exceeding 20 words.
```

**Structured Report Format**:
```
Structure your analysis report as follows:

# Title

## Executive Summary
[2-3 sentence overall overview]

## Problem Analysis
### Problem 1: [Name]
- **Impact**: [1 sentence]
- **Root Cause**: [2-3 sentences]
- **Evidence**: [Specific data or observations]

### Problem 2: [Name]
[Same structure as above]

## Solutions
### Solution 1: [Name]
- **Description**: [2-3 sentences]
- **Implementation**: [Step list]
- **Expected**: [1 sentence]

## Conclusion
[Final recommendation, 1-2 sentences]
```

**JSON Data Format**:
```
Return pure JSON format (no other text), structure as:
{
  "analysis": {
    "status": "success|error",
    "timestamp": "ISO timestamp",
    "summary": "One-sentence summary"
  },
  "findings": [
    {
      "id": "Unique identifier",
      "category": "Category",
      "description": "Description",
      "severity": "High|Medium|Low",
      "recommendation": "Recommendation"
    }
  ],
  "metadata": {
    "version": "1.0",
    "source": "Data source"
  }
}
```

### Common Mistakes

**Mistake 1: Format undefined**
- ❌ "Give me results"
- ✅ "Return as table with columns: Issue, Severity, Recommendation"

**Mistake 2: Format too complex**
- ❌ Requesting complex nested structures, AI struggles to follow accurately
- ✅ Use clear, simple but complete structures

**Mistake 3: Format doesn't match task**
- ❌ Creative writing task requiring strict JSON format
- ✅ Give some format flexibility

### Best Practices
1. **Provide template**: Give clear structure example
2. **Explain each part**: Tell what each part should contain
3. **Keep simple**: Prioritize clear, simple structures
4. **Show example**: If possible, show expected format example
5. **Balance flexibility**: Adjust format strictness based on task

---

## Examples

### Purpose
Show AI expected behavior patterns and output quality through input-output examples.

### Why Important
- **Most powerful guidance**: Examples are more effective than any description
- **Precisely convey expectations**: Showing is more accurate than explaining
- **Reduce ambiguity**: Examples eliminate understanding bias
- **Improve consistency**: Ensure output matches examples

### Example Types

#### Input-Output Examples
```
Example Input: [Input content]
Example Output: [Output content]
```

**Example**:
```
Example Input:
"User login failed"

Example Output:
**Problem Diagnosis**
- Type: Authentication error
- Possible causes: Wrong password, account locked, network issue
- Priority: High
- Recommendation: Check login logs, reset password process
```

#### Multiple Examples (Few-Shot Learning)
Provide 2-3 examples to show pattern.

**Example**:
```
Example 1:
Input: "Product page loads slowly"
Output: "Check image compression, enable CDN, optimize database queries"

Example 2:
Input: "Payment failed"
Output: "Verify API keys, check payment gateway status, review error logs"

Now analyze:
Input: "User cannot register"
```

#### Negative Examples
Show what output should NOT be.

**Example**:
```
Correct output:
"System response time improved by 40%"

Output to avoid:
"Now the system is so much faster, it's just flying!"
```

### Example Design Principles

#### Relevance
Examples should be relevant to the actual task.

**Relevant Example**:
```
Task: Review code quality
Example: Show code review output format
```

#### Representativeness
Examples should represent typical inputs and expected outputs.

**Representative Example**:
```
Task: Sentiment analysis
Example: Show analysis results for different sentiments (positive, negative, neutral)
```

#### Simplicity
Examples should be concise and clear, highlighting key points.

**Simple Example**:
```
Input: "This feature is terrible"
Output: Sentiment: Negative, Intensity: Strong, Key point: Poor feature
```

#### Completeness
Examples should show complete output structure.

**Complete Example**:
```
Input: "Optimize database query"
Output:
## Problem Diagnosis
- Issue: Low query efficiency
- Cause: Missing index

## Optimization Solution
1. Add index to field X
2. Refactor query statement
3. Use cache

## Expected Effect
Query time from 2 seconds down to 0.1 seconds
```

### Example Application Scenarios

#### Format Examples
```
Return format example:
```json
{
  "status": "success",
  "data": {
    "id": 123,
    "name": "Example",
    "tags": ["tag1", "tag2"]
  }
}
```
```

#### Quality Examples
```
Response quality example:
**Concise**: Each sentence not exceeding 20 words
**Clear**: Avoid vague expressions
**Structured**: Use lists and headings
**Practical**: Provide actionable suggestions
```

#### Style Examples
```
Writing style example:
Don't write: "This thing is really super awesome, you'll love it!"
Write: "This solution performs excellently in cost-benefit analysis, recommend prioritizing."
```

### Common Mistakes

**Mistake 1: Poor quality examples**
- ❌ Providing vague, inaccurate examples
- ✅ Providing high-quality, clear examples

**Mistake 2: Irrelevant examples**
- ❌ Examples don't match actual task
- ✅ Examples represent typical use cases

**Mistake 3: Too few examples**
- ❌ Only one example
- ✅ Provide 2-3 relevant examples

**Mistake 4: Too many examples**
- ❌ Providing 5+ examples, consuming too many tokens
- ✅ 2-3 representative examples sufficient

### Best Practices
1. **Quality first**: Example quality matters more than quantity
2. **Diversify**: Cover different input types
3. **Clear labeling**: Explicitly mark which are examples
4. **Keep concise**: Each example focuses on key points
5. **Align with goals**: Ensure examples align with task objectives

---

## Component Integration Example

### Complete Prompt Example

```markdown
# Role/Persona
You are a senior Python backend engineer with 8 years of experience, specializing in high-concurrency system design and performance optimization.

# Context/Background
I'm developing an order processing service for an e-commerce website. Tech stack is Python + FastAPI + PostgreSQL. Current system average response time for order processing is 2.5 seconds, goal is to optimize to under 1 second. Team has 3 developers, project launches in 2 months.

# Task/Instruction
Review the following order processing function, identify performance bottlenecks and provide optimization suggestions. Focus on:
1. Database query efficiency
2. Caching strategy
3. Concurrency handling capability
4. Resource usage

# Constraints/Rules
- Analysis should be specific, not general
- Each suggestion should have clear implementation steps
- Consider existing architecture limitations
- Provide measurable performance improvement expectations
- Response not exceeding 800 words

# Output Format
Return in this structure:

## Performance Analysis
[Overall performance evaluation, under 100 words]

## Bottleneck Identification
- **Bottleneck 1**: [Name]
  - Location: [Code location]
  - Impact: [Performance impact]
  - Cause: [Technical cause]

- **Bottleneck 2**: [Same structure above]

## Optimization Solutions
### Solution 1: [Name]
- **Description**: [Solution description]
- **Implementation**: [Specific steps]
- **Expected**: [Performance improvement]

### Solution 2: [Same structure above]

## Priority Recommendations
[Optimization plan sorted by implementation difficulty and effect]

# Examples

Example analysis format:
**Bottleneck**: Repeated database queries
**Location**: Lines 45-50 in loop
**Impact**: Each order processing consumes extra 200ms
**Cause**: Querying user info one by one in loop
**Recommendation**: Use batch query or cache
**Expected**: 30% performance improvement

[Code snippet]
```

This example demonstrates how to organically integrate all components to create a complete, high-quality prompt.
