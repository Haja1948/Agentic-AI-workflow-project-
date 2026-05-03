# Homework 2: AI Content Monitoring and Generation Workflow

## Objective
Design and document an AI-powered workflow and agentic system that continuously monitors, filters, classifies, and synthesizes the latest developments in Artificial Intelligence (AI) and its business applications. The final output should generate high-quality, domain-relevant thought leadership content suitable for professional platforms such as LinkedIn.

---

## Step-by-Step Implementation Guide

### Phase 1: Daily AI News and Information Monitoring
Design an AI agent to monitor the latest AI-related news and information on a daily basis.
- **Sources to track:**
  - **Venture Capital Firms:** Y Combinator, a16z, Sequoia Capital, etc.
  - **Financial Institutions:** Goldman Sachs, JPMorgan, Morgan Stanley.
  - **KOLs:** Andrew Ng, Andrej Karpathy, Jensen Huang, Demis Hassabis, Lex Fridman, etc.
  - **Academic/Business Schools:** HBR, MIT Technology Review, Stanford University.
  - **Consulting Firms:** McKinsey, BCG, Bain, Accenture, Deloitte.
  - **Tech Giants:** Google, Microsoft, OpenAI.
- **Storage:** Consider using a vector database or a regular database to store insights.

### Phase 2: Relevance Routing and Domain Definition
Build a relevance router to filter information based on your specific context.
- **Define:** Your industry, business domain (e.g., finance, healthcare, SaaS), and target audience.
- **Criteria:** Evaluate relevance based on strategic impact, revenue/cost implications, competitive advantage, operational efficiency, or regulatory considerations.

### Phase 3: Information Classification
Implement an AI-based classification mechanism for relevant documents.
- **Categories:** Group information into meaningful business-relevant categories such as:
  - Strategy and Executive Decision-Making
  - Product and Service Innovation
  - Infrastructure, Models, and Platforms
  - Governance, Ethics, and Regulation
  - Industry-Specific AI Use Cases

### Phase 4: LinkedIn Content Research
Reverse engineer the posting style of 2–5 admired Key Opinion Leaders (KOLs).
- **Document analysis:**
  - **Hooks:** How they open their posts.
  - **Structure:** Scannable formatting techniques.
  - **Credibility:** Use of data, cases, or opinions.
  - **Engagement:** Questions and provocations.
  - **Style:** Concise vs. narrative, instructional vs. contrarian.
- **Output:** Create a "LinkedIn post style and anatomy" checklist to guide your generation.

### Phase 5: LinkedIn Content Generation
Generate professional LinkedIn content for 2–3 selected categories from Phase 3.
- **Requirements:**
  - Include both **text and image**.
  - Translate AI developments into clear business implications.
  - Demonstrate depth of analysis and strategic thinking.
  - Ensure it is concise and suitable for executives/investors.
- **Specify:** Target audience, tone, and positioning for each post.

### Phase 6: Documentation and Progress Report
Document the entire process and optimizations.
- **Components:**
  - Workflow architecture and design logic.
  - Key Challenges encountered.
  - Workflow and prompt optimization progress (before/after, quality improvements).
  - Lessons learned and future automation opportunities.

---

## Running the Pipeline

### Manual Execution
To run the full workflow (Monitoring -> Routing -> Classification -> Generation):
```bash
python -m src.pipeline
```

### Automated Daily Monitoring (Assignment Requirement)
To fulfill the requirement of checking news on a **daily basis**, it is recommended to schedule the `src.pipeline` module using a system scheduler:

**For Windows (Task Scheduler):**
1. Open Task Scheduler.
2. Create a Basic Task.
3. Set the trigger to "Daily".
4. For "Action", choose "Start a program" and point it to your Python executable with the argument `-m src.pipeline`.

**For Linux/Mac (Cron Job):**
Add the following line to your `crontab`:
```bash
0 9 * * * cd /path/to/project && python3 -m src.pipeline >> daily_run.log 2>&1
```
*This schedules the agent to run every morning at 9:00 AM.*

---

## Final Deliverables
1.  **Workflow Files:** The actual design and logic of your agentic system.
2.  **Prompt Design Samples:** Key prompts used at each stage of the workflow.
3.  **Final LinkedIn Content:** One post per selected category (2–3 total).
4.  **Progress Report:** A structured report covering the implementation details.

## Evaluation Criteria
- Soundness of workflow and agent design.
- Effectiveness of relevance routing.
- Quality and business value of insight classification.
- Clarity, relevance, and professionalism of LinkedIn content.
- Depth of reflection and continuous improvement.
