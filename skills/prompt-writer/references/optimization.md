# Prompt Optimization Guide

## Table of Contents
1. [Common Problem Diagnosis](#common-problem-diagnosis)
2. [Optimization Strategies](#optimization-strategies)
3. [Optimization Cases](#optimization-cases)
4. [Iteration Methods](#iteration-methods)

---

## Common Problem Diagnosis

### Problem 1: Output Too Generic

**Symptoms**:
- Response lacks specificity
- Content not in-depth enough
- Doesn't solve specific problem

**Possible Causes**:
- Missing role setting
- Insufficient context
- Task not specific enough
- Target audience unclear

**Diagnosis Check**:
- [ ] Is role specified in prompt?
- [ ] Is sufficient background information provided?
- [ ] Is task description specific?
- [ ] Is target audience explained?

**Optimization Direction**:
1. Add role definition
2. Supplement context information
3. Clarify specific task requirements
4. Specify output depth and focus

---

### Problem 2: Output Too Long or Too Short

**Symptoms**:
- Output verbose, contains lots of irrelevant information
- Output too brief, missing key information

**Possible Causes**:
- Missing length constraints
- Task scope unclear
- No specified focus

**Diagnosis Check**:
- [ ] Are length constraints set?
- [ ] Is task scope clear?
- [ ] Are focus areas specified?

**Optimization Direction**:
1. Add clear length limits
2. Clarify task boundaries
3. Specify focus and excluded content

---

### Problem 3: Format Doesn't Match Expectations

**Symptoms**:
- Output format messy
- Structure unclear
- Hard to read or use

**Possible Causes**:
- No output format specified
- Format requirements unclear
- Missing structure template

**Diagnosis Check**:
- [ ] Is output format specified?
- [ ] Are format requirements clear?
- [ ] Is structure template provided?

**Optimization Direction**:
1. Clearly specify output format (list, table, JSON, etc.)
2. Provide clear structure template
3. Give format example

---

### Problem 4: Inaccurate Information or Hallucination

**Symptoms**:
- Contains incorrect information
- Fabricates non-existent facts
- Cites non-existent sources

**Possible Causes**:
- Requesting model to process content beyond its knowledge range
- No verification requirement
- Missing reasoning process requirement

**Diagnosis Check**:
- [ ] Is task within model capability range?
- [ ] Is model asked to verify information?
- [ ] Is reasoning process required?

**Optimization Direction**:
1. Request information sources
2. Request step-by-step reasoning
3. Request expression of uncertainty
4. Recommend independent verification

---

### Problem 5: Missing Necessary Components

**Symptoms**:
- Output incomplete
- Missing key parts
- Structure incomplete

**Possible Causes**:
- Prompt missing certain core components
- Output format requirements incomplete

**Diagnosis Check**:
Use component checklist:
- [ ] Is there role setting?
- [ ] Is there context information?
- [ ] Is there clear task?
- [ ] Are there constraint conditions?
- [ ] Is there output format requirement?
- [ ] Are there examples?

**Optimization Direction**:
Supplement missing components

---

### Problem 6: Repetitive or Redundant Content

**Symptoms**:
- Content repeats
- Expression redundant
- Information appears multiple times

**Possible Causes**:
- Task expression repetitive
- Constraint conditions overlapping
- No conciseness requirement

**Diagnosis Check**:
- [ ] Are there repetitive expressions in prompt?
- [ ] Are conciseness constraints added?

**Optimization Direction**:
1. Clean up repetitive expressions in prompt
2. Add conciseness requirement
3. Explicitly require avoiding redundancy

---

### Problem 7: Inappropriate Style or Tone

**Symptoms**:
- Tone too formal or too casual
- Style doesn't match expectations
- Inappropriate word choice

**Possible Causes**:
- No role persona specified
- No target audience explained
- Missing style constraints

**Diagnosis Check**:
- [ ] Is role's communication style specified?
- [ ] Is target audience explained?
- [ ] Are there style constraints?

**Optimization Direction**:
1. Clearly specify communication style
2. Explain target audience
3. Add style examples

---

## Optimization Strategies

### Strategy 1: Add Role Setting

**Applicable Scenarios**: Output lacks professional depth or specific perspective

**Method**:
```
You are a [profession], with [years] years of experience, specializing in [domain].
Your characteristic is [style feature].
```

**Example**:
```
Before optimization:
Review this code

After optimization:
You are a senior Python backend engineer with 10 years of experience, specializing in high-concurrency system design and performance optimization. You're skilled at discovering hidden performance bottlenecks and providing practical optimization suggestions.

Review this code:
[code]
```

---

### Strategy 2: Supplement Context Information

**Applicable Scenarios**: Output irrelevant or inaccurate

**Method**:
Provide project background, current state, constraints, audience information

**Example**:
```
Before optimization:
Help me optimize this query

After optimization:
Help me optimize this SQL query.

Background information:
- Database: PostgreSQL 13
- Table size: users table has 1 million rows
- Query frequency: About 100 times per minute
- Current performance: Average response time 2 seconds
- Target performance: Response time under 0.5 seconds
- Index status: Index already built on user_id field

Query statement:
[SQL]
```

---

### Strategy 3: Clarify Task and Output Format

**Applicable Scenarios**: Output structure messy or incomplete

**Method**:
Use specific verbs, clarify task scope, specify output structure

**Example**:
```
Before optimization:
Analyze this product

After optimization:
Analyze this smartwatch's user experience.

Task:
1. Identify 3 main user experience strengths
2. Identify 3 main user experience issues
3. Provide specific improvement suggestions for each issue
4. Assess improvement feasibility and cost

Output format:
## Strengths Analysis
- Strength 1: [Name] - [Description]

## Issues Analysis
- Issue 1: [Name] - [Impact] - [Severity]

## Improvement Suggestions
- Suggestion 1: [Solution] - [Implementation difficulty] - [Expected effect]
```

---

### Strategy 4: Add Constraint Conditions

**Applicable Scenarios**: Output too long, too complex, or doesn't meet requirements

**Method**:
Set length, content, style, scope constraints

**Example**:
```
Before optimization:
Explain machine learning

After optimization:
Explain basic machine learning concepts for high school students.

Constraints:
- Use analogies and examples, avoid complex mathematical formulas
- Total length not exceeding 500 words
- Divide into 3 paragraphs: concept explanation, application scenarios, learning suggestions
- Language vivid and interesting, avoid being too academic
- Focus on "what is machine learning" rather than technical details
```

---

### Strategy 5: Provide Examples

**Applicable Scenarios**: Output format or quality not up to standard

**Method**:
Provide 1-3 input-output examples

**Example**:
```
Before optimization:
Summarize these comments

After optimization:
Summarize user comments, extract main sentiment and key issues.

Example:
Input: "This app crashes frequently, user experience is poor"
Output: Sentiment: Negative, Key issue: Stability

Input: "Features are powerful, but operation is too complex"
Output: Sentiment: Positive but needs improvement, Key issue: Usability

Now summarize these comments:
[Comment list]
```

---

### Strategy 6: Restructure Using Frameworks

**Applicable Scenarios**: Prompt structure messy or missing key components

**Method**:
Reorganize using CRISPE, RTF, or RISE frameworks

**Example**:
```
Before optimization (messy prompt):
I'm in e-commerce, help me write promotional copy, make it attractive, not too long, we sell skincare products, target users are women aged 25-35

After optimization (using CRISPE framework):
**Capacity**: You are a senior marketing copywriter with 5 years of experience, specializing in beauty and skincare brand marketing.

**Request**: Write promotional copy for our new skincare product.

**Information**:
- Product: Natural organic skincare series
- Target users: Urban women aged 25-35, value quality of life and natural ingredients
- Brand positioning: Professional, trustworthy, gentle and effective
- Key selling points: Pure natural ingredients, no additives, clinically proven effective

**Situation**: New product launching this month, will be promoted on social media and Xiaohongshu platform. This is the first introduction to target users, need to build brand awareness.

**Persona**: Use friendly, professional tone, like a friend who understands skincare genuinely recommending. Avoid over-marketing language, express by sharing real experiences.

**Experiment**:
Example style:
"As a user for half a year, I genuinely recommend this serum really improved my sensitive skin..."

**Output requirements**:
- Length: 300-400 words
- Format: Suitable for social media posting
- Content: Include product highlights, usage experience, suitable audience
```

---

### Strategy 7: Add Verification Requirements

**Applicable Scenarios**: Need to ensure output accuracy

**Method**:
Request reasoning process, multi-perspective analysis, self-check

**Example**:
```
Before optimization:
Design this database

After optimization:
Design database structure for this e-commerce website.

Requirements:
1. Analyze in these steps:
   - Identify business entities
   - Define entity relationships
   - Design table structure
   - Consider indexes and constraints

2. Self-check:
   - Does it meet all business requirements
   - Is there redundant data
   - Is scalability considered
   - Does it follow database design principles

3. Multi-perspective validation:
   - From performance angle: How's query efficiency
   - From maintenance angle: Is it easy to maintain
   - From extension angle: Is future extension convenient

4. Mark uncertainty:
   - For design based on assumptions, explain assumptions
   - Point out information needing further confirmation
```

---

### Strategy 8: Adjust Complexity and Focus

**Applicable Scenarios**: Output too complex or too simple

**Method**:
Adjust output complexity and focus based on task needs

**Example**:
```
Before optimization (for beginners):
Explain deep learning

After optimization (for beginners):
Explain basic deep learning concepts in simple language. Assume readers understand basic computer concepts but not AI technology.

Focus:
1. Use life analogies to explain concepts
2. Avoid mathematical formulas and complex terminology
3. Emphasize what deep learning can do, not how to implement
4. Provide 1-2 simple, easy-to-understand application examples

Constraints:
- Use paragraph text, no lists
- Each paragraph 3-4 sentences
- Total length not exceeding 300 words
- Use vivid, interesting language
```

---

## Optimization Cases

### Case 1: Code Review Prompt

**Version 1 (Initial)**:
```
Review this code
[code]
```

**Problem Diagnosis**:
- ❌ No role setting
- ❌ No context
- ❌ Review focus unclear
- ❌ No output format requirement

**Version 2 (Add role and context)**:
```
You are a Python development engineer. This code processes user data, needs review.
[code]
```

**Issues**:
- ✅ Has role setting
- ❌ Context still insufficient
- ❌ Review focus vague
- ❌ No output format

**Version 3 (Complete components)**:
```
You are a senior Python development engineer with 8 years of experience, specializing in code review and security auditing.

Context:
- This is a user authentication module
- Using Flask framework
- Target users: Junior developers

Task:
Review the following code, focusing on:
1. Security vulnerabilities
2. Code style (PEP 8)
3. Performance issues
4. Error handling

Constraints:
- Provide specific line numbers for each issue
- Give fix recommendations
- Keep suggestions beginner-friendly

[code]
```

**Issues**:
- ✅ All components basically complete
- ❌ Output format could be more structured
- ❌ Could add examples

**Version 4 (Final optimization)**:
```
You are a senior Python development engineer with 8 years of experience, specializing in code review and security auditing. You're skilled at discovering potential issues and providing clear, actionable improvement suggestions.

## Context
This is our user authentication module code, developed using Flask framework. Target readers are junior developers, so suggestions should be clear and easy to understand, avoiding overly complex optimization solutions.

## Task
Review the following code, focusing on:
1. Security vulnerabilities (SQL injection, XSS, CSRF, etc.)
2. Code style (Does it follow PEP 8 standards)
3. Performance issues (unnecessary calculations, resource leaks)
4. Error handling (exception handling, edge cases)

## Constraints
- Provide specific line numbers for each issue
- Give directly implementable fix recommendations
- Use beginner-friendly language
- Sort by severity (High→Medium→Low)

## Output Format
Please return in this structure:

## Security Issues
- **Issue 1**: [Name]
  - Location: Line [X-Y]
  - Severity: High/Medium/Low
  - Description: [Brief explanation]
  - Fix: [Specific code or steps]
  - Why important: [1 sentence explaining risk]

## Code Style Issues
[Same structure above]

## Performance Issues
[Same structure above]

## Error Handling Issues
[Same structure above]

## Overall Assessment
- Code quality: [Score/10]
- Main strengths: [2-3]
- Priority fixes: [List 1-2 most critical issues]

## Example Output Format
**Issue**: SQL injection risk
- Location: Line 45
- Severity: High
- Description: Direct SQL query string concatenation, no user input validation
- Fix: Use parameterized queries
  ```python
  cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
  ```
- Why important: Attackers can obtain or modify database data through malicious input

[code snippet]
```

---

### Case 2: Content Creation Prompt

**Version 1 (Initial)**:
```
Write an article about remote work
```

**Problem Diagnosis**:
- ❌ No role
- ❌ No audience
- ❌ No angle
- ❌ No format requirement

**Version 2 (Add role)**:
```
You are a writer. Write an article about remote work.
```

**Issues**:
- ✅ Has role setting
- ❌ Role not specific enough
- ❌ No audience and angle

**Version 3 (Using RTF framework)**:
```
Role: You are a senior HR columnist, having published 20+ feature articles on work styles in well-known tech media.

Task: Write a feature article about remote work, discussing its impact on employees and managers.

Format:
- Title: Engaging title
- Lead: About 100-word introduction
- Body: Divided into 3 sections, each about 300 words
- Conclusion: About 200-word summary and suggestions
- Total length: About 1200 words
```

**Issues**:
- ✅ Clear structure
- ❌ Could add more specific requirements
- ❌ Missing example style

**Version 4 (Final optimization)**:
```
Role: You are a senior HR columnist, having published 20+ feature articles on work styles in well-known tech media. Your writing style is professional but not rigid, skilled at supporting points with data and cases while maintaining readability.

Task: Write a feature article about remote work, deeply exploring the impact of remote work patterns on corporate culture and employee satisfaction in the post-pandemic era.

Context:
- Target media: Professional magazine for business leaders and HR
- Target readers: Corporate management, HR directors
- Current hot topic: Many companies are reconsidering remote work policies
- Article purpose: Provide practical insights and suggestions to help readers make decisions

Format:
## Title
[Engaging but professional title, containing core keywords]

## Lead (100 words)
[Introduce topic, explain importance, summarize article points]

## Current Situation Analysis (300 words)
### Data Support
Cite 2-3 data points from authoritative studies
### Trend Observation
Describe current remote work development trends

## Dual Impact (400 words)
### Positive and Negative Impacts on Employees
- Positive: Flexibility, work-life balance
- Negative: Loneliness, collaboration challenges

### Challenges for Managers
- Transformation of performance management methods
- Maintenance of corporate culture

### Tradeoff Analysis
Use specific cases to explain how to balance

## Practical Suggestions (300 words)
### Suggestions for Managers
3 actionable recommendations

### Suggestions for Employees
2 tips to improve remote work effectiveness

## Conclusion (100 words)
[Summarize core points, look to future, give call to action]

Style Requirements:
- Use professional business language, but avoid being too academic
- Every point supported by data or cases
- Clear logic between paragraphs, use transition sentences
- Use **bold** to emphasize key concepts
- Avoid overly optimistic or pessimistic extreme views, maintain balance

Example Style:
"According to Gartner's 2024 research data, **hybrid work model** has become the first choice for 68% of knowledge-based enterprises. This model is not a simple compromise, but a rethinking of the nature of work..."
```

---

### Case 3: Problem Diagnosis Prompt

**Version 1 (Initial)**:
```
My system is slow, help me check the issue
```

**Problem Diagnosis**:
- ❌ No specific information at all
- ❌ Impossible to provide targeted suggestions

**Version 2 (Add context)**:
```
My website is slow. This is a React frontend and Node.js backend e-commerce site, users experience 5+ second load times on product pages. Help me find the issue.
```

**Issues**:
- ✅ Has basic context
- ❌ Information still not detailed enough
- ❌ No systematic analysis method

**Version 3 (Using RISE framework)**:
```
Role: You are a full-stack performance optimization expert, proficient in frontend and backend performance analysis, with 10 years of large-scale web application optimization experience.

Instructions: I need your help diagnosing my e-commerce website performance issues. Please analyze through a systematic reasoning process, don't jump to conclusions, but show the complete diagnostic process.

Steps:
1. Problem Definition: Clarify specific manifestations and metrics of performance issues
2. Information Gathering: List key information to collect (network, resources, code, etc.)
3. Bottleneck Analysis: Analyze possible bottleneck points
4. Hypothesis Generation: Propose 2-3 possible problem causes
5. Verification Plan: Provide verification methods for each hypothesis
6. Solution Recommendations: Provide optimization plans based on most likely causes

Context:
- Tech stack: React 18 + Node.js + PostgreSQL
- Problem manifestation: Product page load time exceeds 5 seconds
- User scale: About 10K daily active users
- Server configuration: 4-core CPU, 8GB memory
- CDN configuration: Using Alibaba Cloud CDN

Example:
When answering, please follow this reasoning pattern:
"First, I need to clarify the problem boundaries. You say 'product pages are slow', does this specifically mean first-screen load time or overall page load time? Let's assume it's first-screen load time..."

Next, list dimensions to check:
"From network perspective, need to check..."
"From resource perspective, need to check..."
"From code perspective, need to check..."

Based on this information, I generate these hypotheses:
"Hypothesis 1: [Description] - Evidence: [Reason] - Verification method: [Specific steps]"
"Hypothesis 2: [Same above]"

Finally, provide optimization plan based on most likely hypothesis.
```

---

## Iteration Methods

### Iteration Process

```
1. Write initial prompt
   ↓
2. Test and record output
   ↓
3. Analyze gap between output and expectation
   ↓
4. Identify areas for improvement
   ↓
5. Apply optimization strategies
   ↓
6. Retest
   ↓
7. Repeat steps 3-6 until satisfied
```

### Iteration Record Template

```
Task: [Task description]

Version 1:
- Prompt: [Complete prompt]
- Output: [Output result summary]
- Issues: [List issues]
- Improvement direction: [Plan how to improve]

Version 2:
- Prompt: [Modified prompt]
- Output: [Output result summary]
- Improvements: [What improved]
- New issues: [What issues remain]
- Improvement direction: [Next steps]

... (Continue iteration)

Final version:
- Prompt: [Final prompt]
- Effect evaluation: [Satisfaction score]
- Key learnings: [What was learned from iteration]
- Reusable patterns: [Patterns applicable to other tasks]
```

### Single-Variable vs Multi-Variable Iteration

**Single-Variable Iteration** (Recommended for learning):
- Only modify one aspect each time
- Pros: Easy to determine which modification works
- Cons: More iterations

**Example**:
```
Version 1 → Version 2: Add role setting
Version 2 → Version 3: Add context
Version 3 → Version 4: Add format requirement
Version 4 → Version 5: Add constraint conditions
```

**Multi-Variable Iteration** (Recommended when experienced):
- Modify multiple aspects simultaneously
- Pros: Quickly reach goal
- Cons: Hard to determine which change worked

### Fast Iteration Tips

1. **Start with minimum viable prompt**
   - Write most basic version first
   - Quickly test to discover issues

2. **Prioritize most obvious issues**
   - Fix obvious format, structure issues first
   - Then optimize content quality

3. **Use A/B testing**
   - Create two different prompt versions
   - Compare which version works better

4. **Record effective patterns**
   - Discover effective expression styles
   - Save as reusable templates

### Iteration Decision Tree

```
Output doesn't meet expectations
    ↓
Is it a format issue?
    ├─ Yes → Adjust output format requirements
    └─ No → Is it a content issue?
              ├─ Yes → Content generic? → Add role and specific requirements
              │      Content too short? → Adjust length constraints
              │      Content too long? → Add conciseness constraints
              │      Content inaccurate? → Add verification requirements
              └─ No → Is it a structure issue?
                        ├─ Yes → Restructure using framework
                        └─ No → Is it a context issue?
                                  ├─ Yes → Supplement context information
                                  └─ No → Check all components
```

### Best Practices Summary

1. **Be patient**: Good prompts require multiple iterations
2. **Keep records**: Record changes and effects each iteration
3. **Test validation**: Test after each modification
4. **Summarize patterns**: Identify and reuse effective patterns
5. **Continuous learning**: Learn from each iteration

Remember: Prompt engineering is the art of iteration. There are no perfect prompts achieved overnight. Through continuous testing, analysis, and optimization, you will gradually master the skill of creating high-quality prompts.
