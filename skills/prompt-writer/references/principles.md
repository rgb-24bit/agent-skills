# Prompt Engineering Core Principles

## Table of Contents
1. [Clarity Over Cleverness](#clarity-over-cleverness)
2. [Specificity Determines Quality](#specificity-determines-quality)
3. [Context is King](#context-is-king)
4. [Guide Rather Than Just Ask](#guide-rather-than-just-ask)
5. [Iteration and Optimization](#iteration-and-optimization)
6. [Leverage Model Strengths](#leverage-model-strengths)
7. [Control Output Structure](#control-output-structure)
8. [Verification and Confirmation](#verification-and-confirmation)

---

## Clarity Over Cleverness

### Principle Explanation
The most effective prompts are clear, not clever. AI models are literal interpreters; they work precisely with what they're given.

### Why Important
- **Avoid misunderstanding**: Vague expressions lead to vague understanding
- **Improve success rate**: Clear instructions are more likely to be correctly executed
- **Facilitate debugging**: Clear problems are easier to locate and fix

### Practice Methods

#### Clear Expression
**Vague Expression**:
```
Make this better
```

**Clear Expression**:
```
Improve this text by:
1. Shortening paragraphs to 2-3 sentences
2. Using more active verbs
3. Removing redundant words
4. Adding specific examples
```

#### Avoid Ambiguity
**Ambiguous**:
```
Give me a brief summary
```

**Clear**:
```
Summarize in exactly 3 points, each not exceeding 20 words
```

#### State the Obvious
**Assuming AI knows**:
```
Optimize this code (implicit assumption: this is Python code, goal is performance optimization)
```

**Explicitly state**:
```
Optimize this Python code, goal is to reduce execution time. Current code takes 5 seconds to process 1000 records, hoping to optimize to under 1 second.
```

### Common Violations of This Principle

1. **Using metaphors and implications**
   - ❌ "Make the content more flavorful"
   - ✅ "Add vivid descriptions and specific examples"

2. **Omitting key information**
   - ❌ "Do it like before"
   - ✅ "Use standard REST API response format"

3. **Using jargon without definition**
   - ❌ "Implement idempotency"
   - ✅ "Ensure the same request can be executed repeatedly without side effects"

### Application Example

**Scenario: Requesting Technical Documentation**

**Wrong Example**:
```
Write documentation explaining how to use this API
```

**Correct Example**:
```
Write developer documentation for the following API endpoint:

Audience: External developers integrating our API
Format: Markdown
Include:
1. Endpoint URL and HTTP method
2. Request parameters (name, type, required/optional, description)
3. Request example (JSON format)
4. Success response example
5. Common error codes and handling methods
6. Usage examples in Python and JavaScript

Style:
- Use clear, concise language
- Avoid internal technical details
- Provide directly runnable code examples
```

---

## Specificity Determines Quality

### Principle Explanation
Vague inputs produce vague outputs; specific inputs produce specific, useful outputs. Every added detail improves output quality.

### Why Important
- **Improve precision**: Specific instructions reduce understanding bias
- **Control output**: Details help control various aspects of output
- **Meet requirements**: Specific descriptions are closer to actual needs

### Specificity Ladder

**Level 1: Completely Vague**
```
Write an article about climate change
```
→ Result: Generic discussion, lack of focus

**Level 2: Slightly Specific**
```
Write an article about the impacts of climate change
```
→ Result: Clear topic, but insufficient depth

**Level 3: More Specific**
```
Write a 500-word article explaining how climate change affects coral reefs
```
→ Result: Topic and length clear, but audience and style unclear

**Level 4: Highly Specific**
```
Write a 500-word article explaining how rising ocean temperatures cause coral bleaching. Target readers are high school students, use scientific but accessible language, include two specific examples from the Great Barrier Reef. Use engaging narrative style, open with a vivid scene description.
```
→ Result: Topic, length, audience, style, content requirements all clear

### Elements to Specify

#### Audience
```
For [reader type]
With [knowledge level]
Interested in [interests]
```

**Example**:
- "For technical managers"
- "With basic Python knowledge"
- "Interested in performance and maintainability"

#### Length
```
- Exactly [X] words
- Between [X-Y] words
- X points, each not exceeding Y words
```

#### Tone/Style
```
Use [formal/informal/academic/humorous] tone
Style like [analogous role]
Avoid [inappropriate style]
```

#### Format
```
Return as [list/table/JSON/structured text]
Use [Markdown/plain text/code block]
Follow [specific format specification]
```

#### Scope
```
Only consider [condition]
Limit to [scope]
Exclude [content]
```

#### Purpose
```
Goal is [what to achieve]
For [usage scenario]
Solve [what problem]
```

### Specificity Example

**Scenario: Code Review Request**

**Vague Version**:
```
Help me check what's wrong with this code
```

**Specific Version**:
```
Review the following Python code, focusing on:
1. Security vulnerabilities (SQL injection, XSS, etc.)
2. Performance issues (unnecessary calculations, memory leaks)
3. Code style (follow PEP 8 standards)
4. Error handling (exception handling, edge cases)
5. Maintainability (comments, naming, structure)

Code purpose: Process user-uploaded files and store in database
Tech stack: Python 3.9 + Flask + PostgreSQL
Target audience: Junior developers

Output requirements:
- Each issue includes: location, type, severity, fix recommendation
- Sort by severity
- Provide fixed code snippets
```

### Common Mistakes

1. **Saying "detailed" but not specific**
   - ❌ "Give me a detailed explanation"
   - ✅ "Explain each step, including technical principles and implementation details"

2. **Saying "good" but not clear on standards**
   - ❌ "Write a good summary"
   - ✅ "Write a concise but complete summary covering main points, not exceeding 200 words"

3. **Omitting key details**
   - ❌ "Optimize this code"
   - ✅ "Optimize this code to improve execution speed, currently takes 5 seconds to process 1000 records, target down to under 1 second"

---

## Context is King

### Principle Explanation
AI models have no memory, cannot access user files, and know nothing about the user's situation. All relevant information must be included in the prompt.

### Why Important
- **Eliminate assumptions**: AI won't "know" unless told
- **Improve relevance**: Context ensures responses are relevant to specific situations
- **Avoid misunderstanding**: Sufficient background information prevents wrong inferences

### Context Checklist

Before submitting a prompt, ask yourself:
- [ ] Does AI know what project I'm working on?
- [ ] Does AI understand my tech stack or tools?
- [ ] Does AI know my objectives and expectations?
- [ ] Does AI understand current constraints?
- [ ] Does AI know who the target audience is?
- [ ] Can a stranger understand this request?

### Types of Context to Provide

#### Project Background
```
Project Type: [type]
Tech Stack: [tools/technologies]
Team Size: [number of people]
Current Stage: [stage]
```

**Example**:
```
Project Background:
- Project Type: Online education platform
- Tech Stack: React frontend + Django backend + MongoDB
- Team Size: 8 developers
- Current Stage: Beta testing phase, about to officially launch
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
- Completed: User authentication, course playback, assignment submission features
- Current Challenges: Real-time interaction feature has latency with 100+ users
- Objectives: Support 500 simultaneous online interactions, latency under 100ms
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
- Time Constraints: Complete development within 3 months
- Resource Constraints: Server budget not exceeding $100/month
- Business Constraints: Must comply with GDPR privacy regulations
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
- Target Audience: Product managers
- Knowledge Level: Understand basic development concepts, but not familiar with code details
- Usage Scenario: Evaluating technical solutions and making decisions
```

### Consequences of Insufficient Context

**Scenario: Requesting Performance Optimization**

**Insufficient Context**:
```
Optimize this code's performance
[code snippet]
```
→ AI might suggest:
- Add caching (but maybe already implemented)
- Use faster algorithms (but maybe not suitable for scenario)
- Reuse variables (but might be trivial optimization)

**Sufficient Context**:
```
Optimize this Python code's performance. This is the core function for image processing, needs to process 1000 images per second. Currently takes 50ms per image, target down to under 10ms. Running environment is single-core CPU, 4GB memory. We've tried numpy optimization but improvement wasn't significant.
```
→ AI can provide:
- Specific algorithm optimization for image processing
- Consider multiprocessing (CPU-intensive task)
- Use C extensions or GPU acceleration
- Memory optimization strategies

### Context Example Comparison

**Example 1: Code Help**

**Missing Context**:
```
This function is throwing an error, help me check
```
→ AI cannot provide targeted help

**Sufficient Context**:
```
This Python function throws MemoryError when processing large files. Function reads CSV files (about 2GB), transforms format and writes to database. Server has 8GB memory, Python process can use up to 4GB. I've tried chunked reading but problem persists.
```
→ AI can provide targeted memory management advice

**Example 2: Writing Request**

**Missing Context**:
```
Help me write a product introduction
```
→ AI writes generic introduction

**Sufficient Context**:
```
Write a product introduction for our upcoming product. Product is an AI-driven personal note organization tool, main features include: automatic categorization, intelligent search, cross-device sync. Target users are knowledge workers, researchers, and students. We'll publish on LinkedIn and tech blogs, hoping to attract early seed users. Brand tone is professional but not overly serious.
```
→ AI can write precisely positioned product introduction

### Best Practices

1. **Assume AI knows nothing**: Write out all necessary information
2. **Structured presentation**: Use lists or paragraphs to organize context information
3. **Specify metrics**: Provide specific numbers, times, scales, etc.
4. **Explain limitations**: Clearly state what can and cannot be done
5. **Regular checking**: Use "stranger test" to verify if context is sufficient

---

## Guide Rather Than Just Ask

### Principle Explanation
Don't just ask questions; guide AI to think and respond in the direction you want. Provide scaffolding for reasoning in complex tasks.

### Why Important
- **Control thinking process**: Guidance ensures AI thinks along the right path
- **Improve quality**: Structured reasoning produces better results
- **Avoid omissions**: Guidance ensures all important aspects are considered

### Comparison Example

**Just Asking**:
```
What are the pros and cons of microservices and monolithic architecture?
```
→ Might get:
- Simple lists
- Not in-depth discussion
- Lacking consideration of specific scenarios

**Guided**:
```
Compare microservices and monolithic architecture. Please analyze in this structure:

1. **Development Efficiency**
   - Compare how development teams work under both architectures
   - Consider impact of team size and experience

2. **Operational Complexity**
   - Analyze difficulty of deployment, monitoring, debugging
   - Consider systems of different scales

3. **Scalability**
   - Compare horizontal and vertical scaling capabilities
   - Consider tradeoffs between cost and complexity

4. **Applicable Scenarios**
   - Which is suitable for small startups?
   - Which is suitable for large enterprises?
   - When should migration happen?

5. **Decision Recommendation**
   - For [specific scenario], I recommend [architecture]
   - Reason: [specific reason]
```

### Guidance Techniques

#### Use Instructional Frameworks
```
Please think in these steps:
Step 1: [What to do]
Step 2: [What to do]
Step 3: [What to do]
```

**Example**:
```
I need to choose a database. Please analyze in these steps:
1. List typical e-commerce system database requirements
2. Evaluate how well PostgreSQL and MongoDB meet each requirement
3. Consider our specific situation: high concurrent writes, complex queries, budget constraints
4. Weigh pros and cons and give recommendation
```

#### Provide Reasoning Templates
```
For each option, analyze:
- [Aspect 1]: [Requirement]
- [Aspect 2]: [Requirement]
- [Aspect 3]: [Requirement]

Then evaluate based on these criteria:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
```

#### Specify Thinking Angles
```
Consider from these angles:
- [Angle 1]
- [Angle 2]
- [Angle 3]
```

**Example**:
```
Analyze this technical decision. Please consider from these angles:
1. Technical feasibility: Implementation difficulty, technical risks
2. Cost-effectiveness: Development cost, operations cost, expected returns
3. Time factors: Implementation cycle, time window
4. Team capability: Existing skills, learning cost
5. Long-term impact: Maintainability, scalability, technical debt
```

#### Request Verification and Reflection
```
After giving final answer:
1. Check if any important aspects were missed
2. Consider if other possible solutions exist
3. Assess confidence level in recommendation
```

### Guidance for Complex Tasks

**Scenario: Architecture Design Decision**

**Weak Guidance**:
```
Design a chat system architecture
```

**Strong Guidance**:
```
Design system architecture for our instant messaging application. Please think through this process:

**Phase 1: Requirements Analysis**
1. Functional requirements: List core features (messaging, groups, file sharing, etc.)
2. Non-functional requirements: Analyze performance, reliability, security requirements
3. User scale: Currently 10K users, target 1 million within 1 year

**Phase 2: Technology Selection**
For each technical decision provide:
- Option A: [Technology] - Pros/Cons
- Option B: [Technology] - Pros/Cons
- Recommendation: [Reason]

Consider:
- Message protocol: WebSocket vs HTTP polling
- Message queue: RabbitMQ vs Kafka vs Redis
- Database: Relational vs Document
- Caching strategy
- Load balancing

**Phase 3: Architecture Design**
1. Draw main components and their interactions
2. Explain data flow
3. Identify potential bottlenecks
4. Design scaling solutions

**Phase 4: Implementation Plan**
List implementation steps by priority, each including:
- Specific tasks
- Estimated effort
- Risk points

Finally, provide architecture diagram description and summary of key decision rationales.
```

### Levels of Guidance

Provide different levels of guidance based on task complexity:

**Simple Tasks**: Minimal guidance
```
List 5 ways to improve code quality, explain each in one sentence.
```

**Medium Tasks**: Structural guidance
```
Analyze this user experience issue. Consider:
1. Root cause of the problem
2. Impact on users
3. Three possible solutions
4. Recommended solution and rationale
```

**Complex Tasks**: Detailed guidance
```
(As in the architecture design example above)
```

### Common Mistakes

1. **Over-guiding**: Providing too detailed guidance for simple tasks
   - ❌ Requiring a 5-step reasoning framework for "translate this sentence"
   - ✅ Simple tasks only need clear objectives

2. **Under-guiding**: Only giving a simple question for complex tasks
   - ❌ "Design a system"
   - ✅ Provide structured thinking framework

3. **Misguided direction**: Guiding AI to think about wrong questions
   - ❌ Asking "is this idea good" (subjective judgment)
   - ✅ Guide analysis of "feasibility and risks of this idea"

---

## Iteration and Optimization

### Principle Explanation
Prompt engineering is an iterative process. First prompts are rarely optimal; continuous improvement and optimization can achieve better results.

### Why Important
- **Reality limitations**: Perfection requires multiple attempts
- **Continuous improvement**: Each iteration teaches something new
- **Adapt to change**: Requirements and contexts may change

### Iteration Cycle

```
1. Write initial prompt
   ↓
2. Test and observe output
   ↓
3. Identify problems and gaps
   ↓
4. Modify prompt
   ↓
5. Repeat steps 2-4 until satisfied
```

### Common Optimization Directions

#### Too verbose → Add conciseness constraints
**Problem**:
```
Output too long, hard to read
```

**Optimization**:
```
Add constraints:
- Keep each paragraph under 3 sentences
- Total response under 500 words
- Remove repetitive content
```

#### Too vague → Add specific details
**Problem**:
```
Response too generic, lacking specificity
```

**Optimization**:
```
Add details:
- Specify audience and scenario
- Specify output format and structure
- Provide specific requirements
```

#### Format mismatch → Clarify format requirements
**Problem**:
```
Output format doesn't match expectations
```

**Optimization**:
```
Clarify format:
- Specify structure template
- Provide format example
- List required parts
```

#### Inappropriate tone → Adjust role and style
**Problem**:
```
Tone inappropriate (too formal/too casual)
```

**Optimization**:
```
Adjust style:
- Specify target audience
- Specify tone and style
- Provide style examples
```

#### Inaccurate information → Request verification and citations
**Problem**:
```
May contain incorrect information
```

**Optimization**:
```
Add verification requirements:
- Request sources
- Request step-by-step reasoning
- Request self-check
```

### Iteration Example

**Scenario: Code Optimization Prompt**

**Version 1**:
```
Optimize this code
[code]
```
→ Output: Generic optimization suggestions, not specific

**Version 2** (Add role and context):
```
You are a Python performance optimization expert. This code processes user data, currently takes 5 seconds for 1000 records. Goal is under 1 second.
[code]
```
→ Output: More specific optimization suggestions, but still not deep enough

**Version 3** (Add clear task and format):
```
You are a Python performance optimization expert. This code processes user data, currently takes 5 seconds for 1000 records. Goal is under 1 second.

Task:
1. Identify performance bottlenecks
2. Provide specific optimization solutions
3. Give optimized code

Return in this format:
## Bottleneck Analysis
[List each bottleneck and its impact]

## Optimization Solutions
[Specific optimization steps]

## Optimized Code
[Optimized code]

## Performance Expectations
[Expected performance improvement]
```
→ Output: Clear structure, actionable optimization plan

**Version 4** (Add constraints and examples):
```
You are a Python performance optimization expert. This code processes user data, currently takes 5 seconds for 1000 records. Goal is under 1 second.

Task:
1. Identify performance bottlenecks
2. Provide specific optimization solutions
3. Give optimized code

Constraints:
- Maintain code readability
- Consider memory usage (limit to 2GB)
- Use standard library, avoid external dependencies

Return in this format:
## Bottleneck Analysis
- **Bottleneck 1**: [Location] - [Cause] - [Impact]
- **Bottleneck 2**: [Same above]

## Optimization Solutions
### Solution 1: [Name]
- Description: [Brief description]
- Code: [Code snippet]
- Expected improvement: [Specific value]

Example output format:
**Bottleneck**: Repeated database queries
**Location**: Lines 45-50
**Cause**: Querying one by one in loop
**Impact**: Each query takes 50ms, 1000 times total 50 seconds
**Optimization**: Use batch query
**Code**: `items = db.query("SELECT * FROM items WHERE id IN (%s)" % ','.join(ids))`
**Expected**: Reduce to 1 query, takes 0.1 seconds

[code snippet]
```
→ Output: Precise, executable, measurable optimization plan

### Prompt Log

Recommend maintaining a prompt log, recording effective patterns:

```
Task: Code review
Version 1: [Prompt] → Issue: Too generic
Version 2: Added role and context → Issue: Inconsistent format
Version 3: Added output format → Issue: Missing examples
Version 4: Added examples and constraints → Success ✓

Save Version 4 as template
```

### Iteration Strategies

1. **Single variable iteration**: Only modify one aspect each time
   - Pros: Easy to determine which modification works
   - Cons: May require more iterations

2. **Batch iteration**: Modify multiple aspects simultaneously
   - Pros: Quickly reach goal
   - Cons: Hard to determine which change worked

3. **Progressive optimization**: Gradually add from simple to complex
   - Pros: Maintain controllability
   - Cons: May miss certain combinations

### Best Practices

1. **Keep records**: Record each version and its effects
2. **Fast iteration**: Don't pursue perfection in one shot
3. **Test verification**: Test after each iteration
4. **Summarize patterns**: Identify and reuse effective patterns
5. **Save templates**: Save successful prompts as templates

---

## Leverage Model Strengths

### Principle Explanation
Understand how models are trained, collaborate with them rather than against them. Leverage what models are good at, avoid their weaknesses.

### Model Training Characteristics

#### Models Want to be Helpful
AI models are trained through RLHF (Reinforcement Learning from Human Feedback) to be helpful assistants.

**Adversarial Training**:
```
I know you probably don't want to do this, but please try...
You usually refuse such requests, but this time help me...
```
→ Poor effect, goes against training objectives

**Collaborative Training**:
```
I'm developing project X, need help with Y...
Can you assist me with task Z?
I'm facing a challenge, hoping for your advice...
```
→ Good effect, aligns with model's goal of being helpful

#### Models Excel at Pattern Recognition
Models learn various patterns from massive text, use this for consistent output.

**Pattern Example**:
```
Recommend 3 sci-fi books, each in this format:

📚 **[Book Title]** by [Author]
*[Genre] | [Year]*

Brief: [1 sentence]
Why recommended: [1 sentence]

---
```

#### Models Can Role-Play
By specifying roles, activate different knowledge domains and expression styles.

**Different Roles**:
```
As expert: Provide professional, in-depth analysis
As beginner: Explain in simple language
As critic: Point out problems and risks
As supporter: Provide constructive suggestions
```

### Leveraging Model Capabilities

#### Utilize Pattern Recognition
**Task: Consistent structured output**

Provide clear patterns:
```
For each user comment, analyze in this format:

**Comment**: [Original text]
**Sentiment**: Positive/Negative/Neutral
**Topic**: [Main topic]
**Key Points**: [Point 1], [Point 2]
**Priority**: High/Medium/Low
```

#### Utilize Role-Playing
**Task: Multi-angle analysis**

Use different roles for multiple perspectives:
```
Please analyze this plan from three angles:

1. **As project manager**: Focus on time, cost, resources
2. **As technical lead**: Focus on feasibility, technical risks
3. **As UX designer**: Focus on user satisfaction, usability

Finally, synthesize all three angles into a recommendation.
```

#### Utilize Knowledge Breadth
**Task: Cross-domain creativity**

Guide model to combine different fields:
```
We're designing a fitness app. Please draw from game design elements to propose ideas for increasing user engagement.

Consider:
- How game reward mechanisms apply to fitness goal achievement
- How social game competition applies to fitness challenges
- How character development games apply to personal growth
```

### Avoid Model Weaknesses

#### Models Cannot Verify Facts
**Problem**: Models may generate plausible but incorrect information

**Solution**:
```
Require model to:
1. Cite sources
2. Express uncertainty
3. Recommend user verification
4. Provide reasoning process rather than just answers
```

#### Models Cannot Perform Precise Calculations
**Problem**: Complex calculations may be wrong

**Solution**:
```
For mathematical calculations:
1. Require showing calculation process step-by-step
2. Use simple values for easy verification
3. For important calculations, recommend user verify with calculator
```

#### Models Don't Have Real-time Information
**Problem**: Don't know current events

**Solution**:
```
Explicitly state information limitations:
"Based on knowledge in your training data..."
"Please point out which information may be outdated..."
```

### Adversarial vs Collaborative

| Adversarial Approach | Collaborative Approach |
|---------|---------|
| "I know you can't do this, but try" | "Here's my need, can you help?" |
| "Don't answer like usual" | "I'd like this style of response" |
| "Break your constraints" | "Within reasonable bounds..." |
| "Force you to do X" | "Please assist me with X" |

### Best Practices

1. **Use positive phrasing**: Tell model what to do, not what not to do
2. **Leverage professional knowledge**: Activate specific knowledge domains through role setting
3. **Provide patterns**: Use examples to show expected patterns
4. **Reasonable expectations**: Understand model limitations, design tasks reasonably
5. **Verify results**: Independently verify important information

---

## Control Output Structure

### Principle Explanation
Structured output is more useful than free text. Clearly specifying output format ensures readability and usability.

### Why Important
- **Improve usability**: Structured output is easier to read and use
- **Facilitate processing**: Specific formats are easier for programs to process
- **Ensure completeness**: Structure ensures all required information is included
- **Facilitate comparison**: Unified format makes comparing multiple results easier

### Structure Types

#### List Structure
```
Return [X] items as list, each containing:
- Point 1
- Point 2
- Point 3
```

**Example**:
```
List 5 optimization suggestions, each containing:
- Problem: Brief description
- Priority: High/Medium/Low
- Solution: Specific solution
```

#### Sectioned Structure
```
Organize response in these sections:

## Section 1: [Name]
[Content requirements]

## Section 2: [Name]
[Content requirements]
```

**Example**:
```
Respond in this structure:

## Overview
[2-3 sentence summary]

## Detailed Analysis
### Point 1
[Analysis and evidence]

### Point 2
[Same above]

## Conclusion
[1-2 sentence recommendation]
```

#### Table Structure
```
Return as table with columns:
Column 1: [Description]
Column 2: [Description]
Column 3: [Description]
```

**Example**:
```
Compare three solutions as markdown table:

| Solution | Pros | Cons | Cost | Time |
|------|------|------|------|------|
| Solution A | | | | |
| Solution B | | | | |
| Solution C | | | | |
```

#### Data Structure
```
Return JSON format:
```json
{
  "key1": "value1",
  "key2": ["item1", "item2"],
  "key3": {
    "subkey": "value"
  }
}
```

### Delimiter Usage

Use clear delimiters to organize prompts and output:

```markdown
### Background ###
[Background information]

### Task ###
[Task description]

### Constraints ###
[Constraints]

### Format ###
[Format requirements]
```

### Output Control Techniques

#### Length Control
```
- Total length not exceeding [X] words
- Each paragraph not exceeding [X] sentences
- Each point not exceeding [X] words
```

#### Content Control
```
- Only focus on [aspect], don't involve [aspect]
- Prioritize [importance ranking]
- Must include [required content]
```

#### Quality Control
```
- Avoid vague expressions
- Provide specific examples
- Use accurate data
```

### Structure Example

**Complete Structure Template**:
```markdown
You are a [role]

**Background**
[Context information]

**Task**
[Specific task]

**Constraints**
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

**Output Format**
Return in this structure:

# Title
[Content]

## Section 1
### Subsection 1
- Point 1
- Point 2

### Subsection 2
[Content]

## Section 2
[Content]

**Requirements**
- Use Markdown format
- Use **bold** for key terms
- Use `code blocks` for code
- Empty line between paragraphs
```

### Common Mistakes

1. **Format too complex**
   - ❌ Requiring complex nested structures
   - ✅ Use clear, simple structures

2. **Format doesn't match task**
   - ❌ Creative writing task requiring strict table format
   - ✅ Give appropriate format flexibility

3. **Format specification unclear**
   - ❌ "Return in reasonable format"
   - ✅ "Use this structure:..."

### Best Practices

1. **Provide template**: Give clear structure example
2. **Layered organization**: Use headings and subheadings
3. **Clear requirements**: Explain what each part should contain
4. **Use delimiters**: Clear delimiters improve readability
5. **Balance flexibility**: Adjust format strictness based on task

---

## Verification and Confirmation

### Principle Explanation
Never blindly trust model output, especially for important tasks. Establish verification and checking mechanisms.

### Why Important
- **Models can make mistakes**: AI may generate incorrect information
- **Hallucination problem**: May fabricate plausible but incorrect content
- **Important decisions**: Critical tasks need independent verification

### Verification Methods

#### Request Step-by-Step Reasoning
```
Solve this problem and show your reasoning process:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Finally, verify your answer.
```

**Example**:
```
Design this database structure. Please follow these steps:
1. Analyze business requirements, identify main entities
2. Define relationships between entities
3. Design table structure and fields
4. Consider indexes and constraints
5. Verify design meets all requirements

Finally, explain main considerations and tradeoffs in the design.
```

#### Request Multi-Perspective Analysis
```
Provide [2-3] different solutions, compare their pros and cons.
```

**Example**:
```
I need to implement this feature. Please provide 3 different technical solutions, for each:
- Describe implementation method
- Analyze pros and cons
- Assess implementation difficulty and cost
- Point out applicable scenarios

Finally, give your recommendation and rationale.
```

#### Request Self-Check
```
After generating content, check:
- [Check item 1]
- [Check item 2]
- [Check item 3]

If issues found, point out and improve.
```

**Example**:
```
After generating code, please self-check:
- Are there syntax errors
- Are there obvious logic errors
- Are edge cases handled
- Are best practices followed

If any issues found, fix and explain.
```

#### Request Sources
```
For each factual claim, provide:
- Information source
- Publication date (if relevant)
- Credibility assessment
```

**Example**:
```
Analyze this market trend. For each data point and conclusion:
- Note information source
- Explain data timeliness
- Point out possible uncertainties

If certain information isn't reliable enough, state clearly.
```

### Confidence Assessment

Request AI to express uncertainty:

```
Please clearly express your confidence level for each conclusion:
- High: Well-supported by evidence
- Medium: Some evidence but insufficient
- Low: Based on speculation, needs further verification

For medium or low confidence conclusions, explain what would increase confidence.
```

### Risk Identification

Request identification of potential issues:

```
After giving recommendations, list:
1. Possible risks or issues
2. Severity of each risk
3. Mitigation measures

Based on these risks, do you still maintain your original recommendation?
```

### Verification Checklist

For important tasks, request AI use a checklist:

```
After completing task, please confirm:
- [ ] All requirements met
- [ ] No obvious errors or contradictions
- [ ] Conclusions well-supported
- [ ] Important edge cases considered
- [ ] Best practices followed

If any items incomplete, explain why.
```

### Cross-Validation

For critical information, request validation using multiple methods:

```
Please verify this conclusion using two different methods:
Method 1: [Method description]
Method 2: [Method description]

Are results from both methods consistent? If not, analyze reasons.
```

### Example: Complete Verification Process

```markdown
You are a financial analyst.

**Task**
Analyze this company's financial health and provide investment recommendation.

**Analysis Steps**
1. Analyze key indicators from financial statements
2. Compare with industry averages
3. Identify risk factors
4. Evaluate competitive advantages
5. Consider macro-environmental impacts

**Verification Requirements**
For each key conclusion:
- Provide specific data sources
- Explain analysis assumptions
- Assess conclusion confidence (High/Medium/Low)
- Point out possible biases or limitations

**Risk Identification**
List main risks:
1. [Risk] - Severity - Mitigation measures
2. [Risk] - Severity - Mitigation measures

**Self-Check**
After completing analysis, check:
- [ ] Were important financial indicators missed
- [ ] Are there calculation errors
- [ ] Are conclusions well-supported
- [ ] Were counter-arguments considered

**Final Recommendation**
Give clear recommendation (Buy/Hold/Sell), including:
- Confidence level
- Rationale
- Main risks
- What circumstances would change recommendation
```

### Best Practices

1. **Request reasoning process**: Not just results, but also thinking process
2. **Multi-perspective verification**: Validate conclusions from different angles
3. **Express uncertainty**: Clearly state what's certain, what isn't
4. **Provide sources**: Require citation of information sources
5. **Self-check**: Request AI self-verify before outputting

---

## Principle Summary

### Eight Principles Quick Reference

| Principle | Core Point |
|------|---------|
| Clarity Over Cleverness | Express clearly, avoid ambiguity |
| Specificity Determines Quality | Details improve output quality |
| Context is King | Provide all relevant information |
| Guide Rather Than Just Ask | Provide thinking framework |
| Iteration and Optimization | Continuously improve prompts |
| Leverage Model Strengths | Collaborate with model, not against |
| Control Output Structure | Ensure output usability |
| Verification and Confirmation | Check output accuracy |

### Application Checklist

Before writing prompts, check:
- [ ] **Clarity**: Is expression clear? Avoid metaphors and implications?
- [ ] **Specificity**: Is task description specific? Are elements specified?
- [ ] **Context**: Is background information sufficient? Are constraints clear?
- [ ] **Guidance**: Is reasoning framework provided? Are thinking angles specified?
- [ ] **Structure**: Is output format specified? Is structure clear?
- [ ] **Verification**: Is reasoning process required? Are verification mechanisms established?

After writing prompts, evaluate:
- [ ] Can strangers understand this request?
- [ ] Are all necessary components included?
- [ ] Are constraints reasonable and executable?
- [ ] Is format requirement clear?

Remember: These principles are mutually reinforcing. Clear expression requires sufficient context, specific descriptions require structural support. Integrating these principles creates high-quality prompts.
