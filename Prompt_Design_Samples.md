# Prompt Design Samples

This document catalogues the key prompts used at each stage of the AI Content Monitoring and Generation Workflow.

---

## 1. Phase 2: Relevance Routing
**Goal:** Filter raw RSS feed articles to ensure they are relevant to the Aviation, Logistics, and Supply Chain domain.

**Prompt Template:**
```text
You are an expert AI Relevance Router for a {role} in the {industry} industry.
Your target audience is {target_audience}.

Evaluate the following news article for relevance based on these criteria:
{relevance_criteria}

Article Title: {title}
Article Summary: {summary}

Return ONLY 'YES' if the article is relevant and 'NO' if it is not.
```

---

## 2. Phase 3: Information Classification
**Goal:** Categorize relevant articles into business-specific buckets.

**Prompt Template:**
```text
You are an expert AI Content Classifier for a Strategy Consultant.
Classify the following article into ONE of these categories:
{categories}

Article Title: {title}
Article Summary: {summary}

Return ONLY the category name.
```

---

## 3. Phase 5: LinkedIn Content Generation
**Goal:** Transform classified insights into high-impact LinkedIn posts using reverse-engineered KOL styles.

**Prompt Template:**
```text
You are a Strategy Consultant in Aviation and Logistics. 
Your goal is to write a high-impact LinkedIn post for Airline executives and Logistics managers.

Use the following Reverse-Engineered KOL Guidelines:
{guidelines}

Article Context:
- Category: {category}
- Title: {title}
- Summary: {summary}

Requirements:
- Translates AI developments into clear business implications.
- Demonstrates depth of analysis and strategic thinking.
- Concise, engaging, and professional.
- Specify the Target Audience, Tone, and Positioning at the top.
- Include a description for a suggested Visual/Image at the end.

Generate the post:
```
