# Prompt Frameworks Guide

## Table of Contents
1. [CRISPE Framework](#crispe-framework)
2. [RTF Framework](#rtf-framework)
3. [RISE Framework](#rise-framework)
4. [Other Frameworks](#other-frameworks)
5. [Framework Comparison and Selection](#framework-comparison-and-selection)

---

## CRISPE Framework

### Overview
CRISPE is a comprehensive prompt framework suitable for complex tasks and scenarios requiring precise control. It ensures prompt completeness and effectiveness through six dimensions.

### Framework Components

#### C - Capacity/Role
**Definition**: Specify the role and professional capabilities AI should possess

**Key Points**:
- Use professional identities (engineer, doctor, lawyer, etc.)
- Specify years of experience and domain expertise
- Clarify role characteristics (patient, rigorous, innovative, etc.)

**Examples**:
- "You are a senior data scientist with 15 years of experience"
- "You are a product designer focused on user experience"
- "You are a computer science professor skilled at explaining complex concepts"

**Why Important**: Roles focus AI's response perspective, activate relevant knowledge domains, and unify response style

#### R - Request
**Definition**: Clearly tell AI what task to execute

**Key Points**:
- Use specific action verbs
- Avoid vague expressions
- Clarify task boundaries

**Examples**:
- "Analyze this user feedback report and extract main sentiment tendencies"
- "Design a Python function to process time series data"
- "Write a technical blog post about machine learning introduction"

**Why Important**: Clear requests are the core for AI to understand the task, directly affecting output quality

#### I - Information
**Definition**: Provide background information AI needs to complete the task

**Key Points**:
- Provide sufficient context
- Include project details, objectives, constraints
- Avoid assuming AI knows anything

**Examples**:
- "We are a B2B SaaS company, mainly serving SMEs, developing backend services with Node.js"
- "This API processes payment requests, about 1000 requests per second, needs high availability"
- "Target audience is product managers who have some technical background but aren't developers"

**Why Important**: AI has no memory or ability to access user files; all relevant information must be provided in the prompt

#### S - Situation
**Definition**: Describe the current specific situation and environment

**Key Points**:
- Explain current stage or state
- Describe specific challenges faced
- Explain time pressure or other limitations

**Examples**:
- "We're preparing for next week's product launch, time is tight"
- "Current system has performance bottlenecks, needs urgent optimization"
- "This is the project's first prototype, prioritize validating core functionality over completeness"

**Why Important**: Situation information helps AI adjust response priorities and strategies

#### P - Persona
**Definition**: Specify AI's communication style and tone

**Key Points**:
- Determine formality level (formal/informal)
- Choose language style (technical/accessible/humorous)
- Specify cultural or regional characteristics

**Examples**:
- "Use a friendly, encouraging tone, like a patient mentor"
- "Maintain a professional, objective academic style"
- "Use relaxed, humorous internet slang style"

**Why Important**: Persona ensures output aligns with user expectations and brand tone

#### E - Experiment
**Definition**: Provide input-output examples to demonstrate expected behavior

**Key Points**:
- Provide 1-3 clear examples
- Show input-to-output mapping
- Explain expected format and quality

**Example**:
```
Example Input:
"Login page loads slowly"

Example Output:
**Performance Issue Diagnosis**
- Issue Type: Page loading performance
- Possible Causes: Large resource files, network latency, slow server response
- Priority: High
- Suggested Solutions: Optimize image compression, use CDN, check database queries
```

**Why Important**: Examples are the most powerful guidance method, enabling AI to precisely understand expectations through few-shot learning

### CRISPE Complete Example

```markdown
You are a senior marketing copywriter with 10 years of experience (Capacity).

Please write a product introduction for our new product (Request).

Background: We are a startup developing an AI-driven personal knowledge management tool. Target users are knowledge workers, researchers, and students. Core features include: intelligent note organization, automatic content association, quick search, multi-device sync. Our brand tone is professional but not overly serious (Information).

Current Situation: Product launches next month, this is the first public introduction. We'll publish on LinkedIn and Twitter, hoping to generate attention in professional communities (Situation).

Communication Style: Use professional yet approachable tone, avoid over-marketing language, focus on value rather than feature lists (Persona).

Example Style:
Don't write: "Our product has intelligent note organization feature"
Write: "Let your knowledge automatically form networks, easily discovering hidden connections" (Experiment)
```

---

## RTF Framework

### Overview
RTF is a concise and efficient framework suitable for medium-complexity tasks. It emphasizes three core elements: Role, Task, and Format.

### Framework Components

#### R - Role
**Definition**: The role AI should play

**Key Points**:
- Concise and clear
- Relevant to the task
- Include necessary professional background

**Examples**:
- "You are a Python development expert"
- "You are a creative writing coach"
- "You are a psychological counselor"

#### T - Task
**Definition**: The specific task AI needs to execute

**Key Points**:
- Use action verbs
- Clarify task scope
- Specify expected depth

**Examples**:
- "Review the following code, identify 3 areas for improvement"
- "Write a 500-word sequel to this story"
- "Provide 5 methods to relieve work stress"

#### F - Format
**Definition**: Expected output format

**Key Points**:
- Clarify structure
- Specify length
- Explain presentation method

**Example**:
```
- Use markdown format
- Divide into 3 sections: Overview, Analysis, Recommendations
- Total length not exceeding 500 words
```

### RTF Complete Example

```markdown
Role: You are a frontend engineer with 8 years of experience, expert in React and performance optimization.

Task: Review the following React component code, identify performance issues and optimization opportunities.

Format:
Please return in the following format:
## Performance Issues
List discovered performance issues, each including:
- Issue location (line number)
- Issue type (repeated rendering, memory leak, unnecessary computation, etc.)
- Severity (High/Medium/Low)

## Optimization Recommendations
Provide specific optimization solutions for each issue, including:
- Solution description
- Expected improvement
- Implementation difficulty

## Code Example
Provide an optimized code snippet demonstrating improvement methods
```

---

## RISE Framework

### Overview
RISE framework focuses on systematic reasoning and structured thinking, suitable for tasks requiring in-depth analysis and logical reasoning.

### Framework Components

#### R - Role
**Definition**: Professional role executing the task

#### I - Input
**Definition**: Describe information or resources

**Examples**:
- "Provide the following user feedback data: [data]"
- "Based on the following market analysis report: [report]"
- "Reference the following technical documentation: [documentation]"

#### S - Steps
**Definition**: Break down complex tasks into executable steps

**Example**:
```
Step 1: Define problem boundaries
Step 2: Collect key information
Step 3: Apply analysis framework
Step 4: Draw conclusions
Step 5: Verify results
```

#### E - Expectation
**Definition**: Describe required results

**Examples**:
- "Provide clear decision recommendations"
- "Give detailed optimization solutions"
- "Output structured analysis report"

### RISE Complete Example

```markdown
Role: You are a strategy consultant, skilled in business analysis and decision support.

Input: I need your help evaluating whether we should add a new feature to our product.

Steps:
1. Problem Definition: Clarify the feature to evaluate and core decision question
2. Information Gathering: List key factors to consider (user needs, technical feasibility, cost, competitive environment, etc.)
3. Stakeholder Analysis: Identify all stakeholders and their concerns
4. Option Evaluation: Analyze supporting and opposing arguments, weigh pros and cons
5. Risk Assessment: Identify potential risks and mitigation measures
6. Final Recommendation: Provide clear recommendation and implementation plan based on analysis

Expectation: Provide a structured decision analysis report including clear recommendations and risk assessment.
```

---

## Other Frameworks

### A.P.E Framework

#### Overview
APE is a concise three-element framework suitable for quickly building basic prompts.

#### Framework Components

**A - Action**
- Definition: Define the work or activity to complete
- Example: "Analyze this dataset"
- Key Points: Use clear action verbs

**P - Purpose**
- Definition: Discuss intent or objective
- Example: "Purpose is to identify sales trends"
- Key Points: Clearly state why this is being done

**E - Expectation**
- Definition: State expected results
- Example: "Expect 3-5 key findings"
- Key Points: Specifically describe expected output

#### APE Example
```markdown
Action: Analyze this month's sales data

Purpose: Purpose is to identify sales trends and anomalies to inform next month's marketing strategy

Expectation: Expect to receive:
- 3-4 key findings on sales trends
- 2-3 identified anomaly data points
- 2 specific recommendations based on findings
```

---

### B.R.O.K.E Framework

#### Overview
BROKE is a comprehensive five-element framework, particularly suitable for scenarios requiring clear objectives and results.

#### Framework Components

**B - Background**
- Definition: Explain background, provide sufficient information
- Example: "We are an e-commerce company with annual sales of 50 million"
- Key Points: Provide sufficient context

**R - Role**
- Definition: The role I want ChatGPT to play
- Example: "You are a marketing expert"
- Key Points: Clearly define AI's role

**O - Objectives**
- Definition: What we want to achieve
- Example: "Goal is to increase brand awareness and user engagement"
- Key Points: Clear objective statement

**K - Key Result**
- Definition: What specific effects I want
- Example: "Social media followers increase by 50%"
- Key Points: Quantifiable result metrics

**E - Evolve**
- Definition: Three improvement methods freely combined
- Example: "Test different content strategies, adjust based on data feedback"
- Key Points: Emphasize iterative optimization

#### BROKE Example
```markdown
Background: We are a B2B SaaS company providing project management tools, currently 20K monthly active users, preparing to enter the North American market.

Role: You are a marketing director with 10 years of experience, skilled in B2B SaaS market entry strategies.

Objectives: Help us develop a market entry strategy for North America, goal is to acquire 1000 paid users within 6 months.

Key Result: Expect to receive:
- Detailed market entry strategy
- 3 core marketing channels
- Estimated customer acquisition cost and budget allocation
- Milestone targets for month 1, 3, and 6

Evolve: Provide 2-3 alternative strategies and explain how to adjust based on initial data.
```

---

### C.O.A.S.T Framework

#### Overview
COAST is a five-element framework emphasizing scenario and action, suitable for task-oriented scenarios.

#### Framework Components

**C - Context**
- Definition: Set the stage for dialogue
- Example: "We are developing a mobile application"
- Key Points: Provide basic situation information

**O - Objective**
- Definition: Describe the goal
- Example: "Goal is to design user registration flow"
- Key Points: Clarify task objective

**A - Action**
- Definition: Explain required actions
- Example: "Design a simple and fast registration interface"
- Key Points: Explain what specifically to do

**S - Scenario**
- Definition: Describe the scenario
- Example: "User opens the app for the first time"
- Key Points: Provide specific usage scenario

**T - Task**
- Definition: Describe the task
- Example: "Design UI flow and interaction details"
- Key Points: Clear task description

#### COAST Example
```markdown
Context: We are developing a fitness tracking app, target users are urban professionals aged 25-35.

Objective: Design the onboarding flow for users opening the app for the first time.

Action: Design a concise, engaging onboarding interface that quickly introduces core features and completes initial setup.

Scenario: User downloads and opens the app for the first time, knows nothing about app features, needs to establish first impression within 30 seconds.

Task: Design an onboarding flow including:
- 3-4 key feature introduction pages
- Simple setup wizard (profile, goal setting)
- Encourage users to complete first record
```

---

### T.A.G Framework

#### Overview
TAG is an ultra-concise three-element framework suitable for quick, simple tasks.

#### Framework Components

**T - Task**
- Definition: Define specific task
- Example: "Translate this text"
- Key Points: Concise task description

**A - Action**
- Definition: Describe what needs to be done
- Example: "Translate to English, maintain technical accuracy"
- Key Points: Specific action description

**G - Goal**
- Definition: Explain final goal
- Example: "Goal is for international team to understand"
- Key Points: Explain ultimate purpose

#### TAG Example
```markdown
Task: Translate the following technical documentation fragment

Action: Translate to English, maintain accuracy of technical terms, sentence structure conforming to English conventions

Goal: Goal is for international technical team to understand and implement these technical solutions
```

---

### T.R.A.C.E Framework

#### Overview
TRACE is a five-element framework emphasizing request and examples, suitable for tasks requiring clear guidance.

#### Framework Components

**T - Task**
- Definition: Define specific task
- Example: "Design a database schema"
- Key Points: Clear task

**R - Request**
- Definition: Describe your requirements
- Example: "Require support for high concurrent read/write"
- Key Points: Specific requirements

**A - Action**
- Definition: Explain operations needed
- Example: "Design table structure and indexing strategy"
- Key Points: Operation description

**C - Context**
- Definition: Provide context or situation
- Example: "This is an e-commerce system"
- Key Points: Background information

**E - Example**
- Definition: Give an example to illustrate your point
- Example: "Design like this..."
- Key Points: Provide reference examples

#### TRACE Example
```markdown
Task: Design database schema for user comment feature

Request: Require support for high concurrent read/write (1000+ writes per second), full-text search, ability to quickly query comments from specific users

Action: Design table structure, indexing strategy, consider possibility of table partitioning

Context: This is an e-commerce website, expected 1 million monthly active users, 100K daily comments

Example: Reference design approach:
```
comments table:
- id (primary key)
- user_id (foreign key, indexed)
- product_id (foreign key, indexed)
- content (text)
- created_at (time index)
```
Please design a complete solution based on this approach.
```

---

### E.R.A Framework

#### Overview
ERA is a concise three-element framework emphasizing the sequence of expectation, role, and action.

#### Framework Components

**E - Expectation**
- Definition: Describe required results
- Example: "Expect 3 optimization solutions"
- Key Points: Clearly state expected output

**R - Role**
- Definition: Specify ChatGPT's role
- Example: "You are a performance optimization expert"
- Key Points: Define role

**A - Action**
- Definition: Specify what actions to take
- Example: "Analyze and optimize this code"
- Key Points: Specific actions

#### ERA Example
```markdown
Expectation: Expect 3 executable code optimization solutions, each including problem description, optimization method, and expected effect.

Role: You are a Python performance optimization expert with 15 years of experience.

Action: Analyze the following code, identify performance bottlenecks, provide specific optimization recommendations.
```

---

### C.A.R.E Framework

#### Overview
CARE is a four-element framework emphasizing the complete loop of context, action, result, and example.

#### Framework Components

**C - Context**
- Definition: Set stage or context for discussion
- Example: "We are refactoring legacy system"
- Key Points: Background setting

**A - Action**
- Definition: Describe what you want to do
- Example: "Refactor user authentication module"
- Key Points: Action description

**R - Result**
- Definition: Describe required results
- Example: "More secure, more maintainable code"
- Key Points: Result explanation

**E - Example**
- Definition: Give an example to illustrate your point
- Example: "For example using JWT tokens"
- Key Points: Example explanation

#### CARE Example
```markdown
Context: We are refactoring a legacy system developed 5 years ago, the user authentication module has security issues and is hard to maintain.

Action: Redesign user authentication module using modern security standards and best practices.

Result: Expect to receive:
- Improved security (support JWT, OAuth2)
- Clear code structure, easy to maintain and extend
- Support multiple authentication methods (password, social login)

Example: Reference the following design approach:
```python
class AuthService:
    def authenticate(self, username, password):
        # Verify credentials
        pass
    
    def generate_token(self, user):
        # Generate JWT token
        pass
```
Please design a complete authentication system based on this approach.
```

---

### R.O.S.E.S Framework

#### Overview
ROSES is a five-element framework with complete structure, suitable for scenarios requiring systematic solutions.

#### Framework Components

**R - Role**
- Definition: Specify ChatGPT's role
- Example: "You are a product manager"
- Key Points: Role positioning

**O - Objective**
- Definition: State goal or objective
- Example: "Goal is to improve user retention"
- Key Points: Objective statement

**S - Scenario**
- Definition: Describe situation
- Example: "Current monthly churn rate 15%"
- Key Points: Scenario description

**E - Expected Solution**
- Definition: Define required results
- Example: "Expect 3 specific solutions"
- Key Points: Solution definition

**S - Steps**
- Definition: Require measures to achieve solution
- Example: "Explain implementation methods step-by-step"
- Key Points: Implementation steps

#### ROSES Example
```markdown
Role: You are a product manager with 8 years of experience, skilled in user growth and retention strategies.

Objective: Help us improve mobile app user retention rate, current 30-day retention is 15%, target is 30%.

Scenario: App is a social fitness application, main users are urban professionals aged 25-35, currently 50K daily active users, 200K monthly active users. Highest churn rate at day 7.

Expected Solution: Expect to receive:
- In-depth analysis of user churn reasons
- 3 specific retention improvement solutions
- Estimated effect and implementation cost for each solution
- Priority ranking

Steps: For each solution, please provide:
1. Core approach of the solution
2. Specific implementation steps
3. Required resources and time
4. Success metrics and evaluation methods
```

---

### I.C.I.O Framework

#### Overview
ICIO is a four-element framework particularly suitable for data processing and transformation tasks.

#### Framework Components

**I - Instruction**
- Definition: Specific task for AI to execute
- Example: "Transform data format"
- Key Points: Clear instruction

**C - Context**
- Definition: Give AI more background information
- Example: "This is customer feedback data"
- Key Points: Background information

**I - Input Data**
- Definition: Tell the model what data needs processing
- Example: "Input CSV format data"
- Key Points: Data description

**O - Output Indicator**
- Definition: Tell what type or style to output
- Example: "Output as JSON format"
- Key Points: Output format

#### ICIO Example
```markdown
Instruction: Transform user feedback data into structured analysis report, identify main issues and trends.

Context: This is user feedback from our product over the past 30 days, including App Store reviews, customer service tickets, and social media feedback. We want to understand what users are most concerned about.

Input Data: Provide CSV format data with fields: User ID, Feedback Time, Feedback Channel, Feedback Content, Sentiment Label

Output Indicator: Output JSON format with structure:
```json
{
  "summary": {
    "total_feedback": 1000,
    "period": "30 days",
    "main_channels": ["App Store", "Customer Service", "Social Media"]
  },
  "top_issues": [
    {
      "issue": "Issue description",
      "count": 50,
      "percentage": 5,
      "sentiment": "Negative"
    }
  ],
  "trends": [
    {
      "trend": "Trend description",
      "direction": "Increasing/Decreasing"
    }
  ]
}
```
```

---

### R.A.C.E Framework

#### Overview
RACE is a four-element framework, concise yet complete, suitable for most common tasks.

#### Framework Components

**R - Role**
- Definition: Specify ChatGPT's role
- Example: "You are a technical documentation writer"
- Key Points: Role definition

**A - Action**
- Definition: Detailed explanation of what actions to take
- Example: "Write API documentation"
- Key Points: Action explanation

**C - Context**
- Definition: Provide relevant details about the situation
- Example: "This is RESTful API documentation"
- Key Points: Context information

**E - Expectation**
- Definition: Describe expected results
- Example: "Expect clear developer documentation"
- Key Points: Result expectation

#### RACE Example
```markdown
Role: You are a technical documentation writer with 10 years of experience, specializing in writing API documentation for developers.

Action: Write complete developer documentation for the following API endpoint.

Context: This is a payment processing service API using RESTful architecture. Target readers are external developers integrating our API, they have basic HTTP and JSON knowledge. Documentation will be published on our developer portal.

Expectation: Expect documentation to include:
- Endpoint overview (function description, purpose)
- Request details (method, URL, headers, body parameters with examples)
- Response details (success response, error response with examples)
- Code examples (Python and JavaScript)
- Common questions and usage notes

Documentation style:
- Clear and concise, avoid over-technicalization
- Use Markdown format
- Include directly runnable code examples
```

---

## Framework Comparison and Selection

### Framework Complexity Grading

**Simple Frameworks (3 elements)**:
- A.P.E
- T.A.G
- E.R.A
- Suitable for: Quick tasks, simple requests, daily use

**Medium Frameworks (4-5 elements)**:
- R.T.F
- R.A.C.E
- C.A.R.E
- I.C.I.O
- Suitable for: Regular tasks, technical work, clear scenarios

**Complex Frameworks (5-6 elements)**:
- C.R.I.S.P.E
- B.R.O.K.E
- C.O.A.S.T
- T.R.A.C.E
- R.I.S.E
- R.O.S.E.S
- Suitable for: Complex projects, systematic analysis, important decisions

### Framework Selection by Scenario

#### Creative Writing
- Recommended: C.O.A.S.T (emphasizes scenario)
- Alternative: C.R.I.S.P.E (complete control)

#### Technical Development
- Recommended: R.T.F (concise and effective)
- Alternative: T.R.A.C.E (includes examples)

#### Data Processing
- Recommended: I.C.I.O (designed for data)
- Alternative: T.A.G (quick processing)

#### Decision Analysis
- Recommended: R.I.S.E (emphasizes reasoning)
- Alternative: B.R.O.K.E (focus on results)

#### Business Strategy
- Recommended: R.O.S.E.S (systematic)
- Alternative: B.R.O.K.E (goal-oriented)

#### Quick Tasks
- Recommended: T.A.G (most concise)
- Alternative: A.P.E (three elements)

#### Product Design
- Recommended: C.O.A.S.T (scenario-driven)
- Alternative: C.R.I.S.P.E (comprehensive control)

#### Marketing Copy
- Recommended: C.R.I.S.P.E (persona control)
- Alternative: C.A.R.E (emphasizes results)

### Framework Comparison Table

| Framework | Elements | Complexity | Suitable Scenarios | Features |
|------|--------|--------|---------|------|
| A.P.E | 3 | Simple | Quick tasks | Ultra-concise |
| T.A.G | 3 | Simple | Quick tasks | Simplest |
| E.R.A | 3 | Simple | Clear goals | Prioritizes expectation |
| R.T.F | 3 | Simple | Technical tasks | Classic and concise |
| R.A.C.E | 4 | Medium | General tasks | Balanced and complete |
| C.A.R.E | 4 | Medium | General tasks | Emphasizes examples |
| I.C.I.O | 4 | Medium | Data processing | Data-specific |
| T.R.A.C.E | 5 | Medium-High | Technical tasks | Includes examples |
| R.I.S.E | 4 | Medium-High | Reasoning analysis | Emphasizes steps |
| C.O.A.S.T | 5 | Medium-High | Scenario tasks | Emphasizes scenario |
| R.O.S.E.S | 5 | Medium-High | System solutions | Complete system |
| B.R.O.K.E | 5 | Medium-High | Goal-oriented | Key results |
| C.R.I.S.P.E | 6 | High | Complex tasks | Most comprehensive |

### Framework Selection Decision Tree

```
Task complexity?
├─ Simple (single objective, quick completion)
│  ├─ Need most concise? → T.A.G
│  ├─ Need clear expectation? → E.R.A
│  └─ General simple task? → A.P.E
└─ Medium to Complex
   ├─ Technical development?
   │  ├─ Simple and quick? → R.T.F
   │  └─ Need examples? → T.R.A.C.E
   ├─ Data processing? → I.C.I.O
   ├─ Reasoning analysis? → R.I.S.E
   ├─ Decision planning?
   │  ├─ Goal-oriented? → B.R.O.K.E
   │  └─ Systematic? → R.O.S.E.S
   ├─ Creative writing?
   │  ├─ Scenario-driven? → C.O.A.S.T
   │  └─ Complete control? → C.R.I.S.P.E
   └─ General complex tasks
      ├─ Need examples? → C.A.R.E
      ├─ Emphasize action? → R.A.C.E
      └─ Most comprehensive? → C.R.I.S.P.E
```

### Usage Recommendations

1. **Beginner Path**:
   - Stage 1: Master R.T.F (classic framework)
   - Stage 2: Learn C.R.I.S.P.E (comprehensive framework)
   - Stage 3: Select other specialized frameworks based on needs

2. **Efficiency Priority**:
   - Daily quick tasks: T.A.G or A.P.E
   - Technical work: R.T.F
   - Data processing: I.C.I.O

3. **Quality Priority**:
   - Important projects: C.R.I.S.P.E or B.R.O.K.E
   - Complex decisions: R.I.S.E or R.O.S.E.S
   - System solutions: R.O.S.E.S

4. **Flexible Application**:
   - Can combine elements from different frameworks
   - Adjust framework based on task
   - Don't be constrained by framework form

5. **Advanced Techniques**:
   - Create personal template library
   - Record effective patterns
   - Iteratively optimize framework application

Remember: Frameworks are tools, not constraints. Choose the framework that works best for you, or flexibly combine elements from different frameworks to achieve the best results.
