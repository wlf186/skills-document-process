---
name: tender-analyzer
description: Automated extraction and analysis of tender/bid document PDFs. Extracts key information including project name, tender number, budget, deadlines, contact info, technical requirements, commercial terms, evaluation criteria, and more. Outputs structured markdown reports. Supports both Chinese and English tender documents. Use when analyzing tender documents, RFPs, procurement notices, or bid announcements.
---

# Tender Analyzer

## Overview

Extract structured information from PDF tender/bid documents and output a comprehensive markdown analysis report. Supports both Chinese and English documents.

## Workflow

### Step 1: Extract PDF Content

Use the `pdf` skill to extract text content from the PDF:

```
Extract all text from the tender PDF
```

For scanned/image-based PDFs, use OCR to make the content searchable first.

### Step 2: Identify Language and Structure

Determine if the document is primarily in Chinese or English based on the extracted text. Identify the document structure (sections, tables, etc.).

### Step 3: Extract Key Information

Extract the following fields using the keyword patterns in [references/tender_keywords.md](references/tender_keywords.md):

#### Basic Information
- **Project Name** (项目名称/Project Name)
- **Tender Number** (招标编号/Tender No.)
- **Budget Amount** (预算金额/Budget)
- **Tender Type** (招标方式/Tender Method)

#### Important Dates
- **Publication Date** (发布日期/Publication Date)
- **Bid Deadline** (投标截止时间/Deadline)
- **Opening Time** (开标时间/Bid Opening Time)

#### Tenderer Information
- **Tenderer Name** (招标人/Tenderer)
- **Contact Person** (联系人/Contact Person)
- **Contact Phone** (联系电话/Contact Phone)
- **Contact Email** (联系邮箱/Contact Email)
- **Address** (地址/Address)

#### Agency Information (if applicable)
- **Agency Name** (代理机构/Agency)
- **Agency Contact** (代理联系方式/Agency Contact)

#### Bid Security
- **Security Amount** (投标保证金/Bid Security)
- **Payment Method** (缴纳方式/Payment Method)

#### Requirements
- **Technical Requirements** (技术要求/Technical Requirements)
- **Qualification Requirements** (资质要求/Qualification Requirements)
- **Commercial Requirements** (商务要求/Commercial Requirements)
- **Delivery Terms** (交货期/Delivery Time, Location)

#### Evaluation
- **Evaluation Method** (评标办法/Evaluation Method)
- **Scoring Criteria** (评分标准/Scoring Criteria)

#### Submission
- **Submission Method** (递交方式/Submission Method)
- **Required Documents** (投标文件要求/Required Documents)

### Step 4: Generate Markdown Report

Output the extracted information in the following structured markdown format:

```markdown
# 招标书分析报告 / Tender Analysis Report

## 一、基本信息 / Basic Information

| 项目 / Item | 内容 / Content |
|-------------|----------------|
| 项目名称 / Project Name | [Extracted Name] |
| 招标编号 / Tender Number | [Number] |
| 预算金额 / Budget Amount | [Amount] |
| 招标方式 / Tender Method | [Method] |

## 二、重要时间 / Important Dates

| 时间项 / Time Item | 日期时间 / Date & Time |
|-------------------|------------------------|
| 发布日期 / Publication Date | [Date] |
| 投标截止时间 / Bid Deadline | [Date & Time] |
| 开标时间 / Opening Time | [Date & Time] |

## 三、招标人信息 / Tenderer Information

| 项目 / Item | 内容 / Content |
|-------------|----------------|
| 招标人 / Tenderer | [Name] |
| 联系人 / Contact | [Name] |
| 联系电话 / Phone | [Number] |
| 联系邮箱 / Email | [Email] |
| 地址 / Address | [Address] |

## 四、代理机构（如有）/ Agency Information (if applicable)

[Agency details]

## 五、投标保证金 / Bid Security

| 项目 / Item | 内容 / Content |
|-------------|----------------|
| 保证金金额 / Security Amount | [Amount] |
| 缴纳方式 / Payment Method | [Method] |

## 六、技术要求 / Technical Requirements

[Extracted technical requirements]

### 资质要求 / Qualification Requirements
[Extracted qualifications]

## 七、商务要求 / Commercial Requirements

[Extracted commercial terms]

### 付款方式 / Payment Terms
[Payment terms]

### 交货期/工期 / Delivery Period
[Delivery timeline]

### 交货地点 / Delivery Location
[Location]

## 八、评标办法 / Evaluation Method

[Extracted evaluation method]

### 评分标准 / Scoring Criteria
[Scoring details]

## 九、投标文件要求 / Bid Document Requirements

[Document requirements list]

## 十、其他信息 / Other Information

- 附件 / Attachments: [List]
- 来源 / Source: [URL or description]
```

### Step 5: Handle Missing Information

If a field cannot be found in the document, mark it as:
- Chinese: `未找到 (Not Found)`
- English: `N/A`

Do not guess or fabricate information.

## Resources

### scripts/extract_pdf_text.py

Utility script for extracting text from PDF files. Usage:

```bash
python3 scripts/extract_pdf_text.py /path/to/tender.pdf
```

This can be used when the `pdf` skill is unavailable or for batch processing.

### references/tender_keywords.md

Comprehensive reference containing:
- Chinese and English keyword mappings for all tender fields
- Regular expression patterns for dates, money, phone numbers, emails
- Common document structure patterns
- Extraction tips and best practices

**Read this file** when you need to:
- Look up keywords for a specific field
- Find appropriate regex patterns for data extraction
- Understand tender document structure conventions
- Handle variations in terminology

## Best Practices

1. **Be Thorough**: Extract all available information, not just the obvious fields. Look for information in tables, footers, headers, and appendices.

2. **Maintain Accuracy**: Only extract what is explicitly stated in the document. Do not infer or assume values.

3. **Preserve Context**: When extracting requirements or criteria, include sufficient context to make the information useful (e.g., include full requirement descriptions, not just titles).

4. **Handle Multiple Values**: Some fields may have multiple values (e.g., multiple contact persons, multiple required documents). List all of them.

5. **Format Dates Consistently**: Preserve the original date format but consider adding ISO format (YYYY-MM-DD) for clarity.

6. **Currency Conversion**: If the document uses different currency formats, preserve the original with the currency code clearly noted.

7. **Cross-Reference**: When the same information appears in multiple places, prefer information from dedicated sections or summary tables over passing mentions.

8. **Language Consistency**: If the document is primarily in Chinese, use Chinese as the primary language in the output with English in parentheses. If primarily English, use English with Chinese in parentheses where helpful.
