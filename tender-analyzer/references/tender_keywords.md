# Tender Document Keywords and Fields

This reference contains common keywords and field patterns for extracting information from tender documents in both Chinese and English.

## Core Fields to Extract

### 1. Basic Information

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Project Name | 项目名称、项目、工程名称 | Project Name, Project, Title |
| Tender Number | 招标编号、项目编号、采购编号 | Tender No., Bid No., Reference No., Procurement No. |
| Budget Amount | 预算金额、预算、采购预算、最高限价 | Budget, Estimated Cost, Maximum Price, Budget Amount |
| Tender Type | 招标方式、采购方式 | Tender Method, Procurement Type |

### 2. Time Information

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Deadline | 投标截止时间、投标截止日期、递交截止时间 | Deadline, Closing Date, Submission Deadline, Bid Closing Time |
| Opening Time | 开标时间、开标日期 | Bid Opening Time, Opening Date |
| Publication Date | 招标公告发布日期、公告时间 | Publication Date, Announcement Date |

### 3. Tenderer Information

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Tenderer Name | 招标人、采购人、发包人 | Tenderer, Purchaser, Client, Employer, Procuring Entity |
| Contact Person | 联系人、项目负责人 | Contact Person, Contact Name |
| Contact Phone | 联系电话、联系电话 | Contact Phone, Telephone, Contact Number |
| Contact Email | 联系邮箱、电子邮箱 | Contact Email, Email Address |
| Address | 地址、联系地址、招标人地址 | Address, Contact Address |

### 4. Agency Information

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Agency Name | 招标代理机构、代理机构 | Tender Agent, Procurement Agent, Agency |
| Agency Contact | 代理联系人、代理机构联系方式 | Agency Contact |

### 5. Bid Security

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Security Amount | 投标保证金、保证金金额 | Bid Security, Bid Bond, Security Deposit, Performance Bond |
| Security Payment | 保证金缴纳方式、保证金支付 | Payment Method, How to Pay |

### 6. Technical Requirements

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Technical Specs | 技术要求、技术规格、技术参数 | Technical Requirements, Technical Specifications, Specs |
| Qualification | 资质要求、资格要求 | Qualification Requirements, Eligibility Criteria |
| Experience | 业绩要求、类似业绩 | Experience Requirements, Similar Projects |
| Standards | 技术标准、执行标准 | Standards, Code Standards |

### 7. Commercial Requirements

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Business Terms | 商务要求、商务条款 | Commercial Requirements, Business Terms |
| Payment Terms | 付款方式、付款条件 | Payment Terms, Terms of Payment |
| Delivery Time | 交货期、工期、交付时间 | Delivery Time, Completion Period, Lead Time |
| Delivery Location | 交货地点、项目地点 | Delivery Location, Site Location, Place of Delivery |

### 8. Evaluation Criteria

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Evaluation Method | 评标办法、评审方法 | Evaluation Method, Evaluation Criteria |
| Scoring Standard | 评分标准、评分细则 | Scoring Criteria, Marking Scheme |
| Weight Distribution | 权重分配、分值分布 | Weight Distribution, Point Allocation |

### 9. Bid Submission

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Submission Method | 递交方式、投标方式 | Submission Method, How to Submit |
| Submission Location | 投标地点、递交地址 | Submission Address, Bid Submission Location |
| Documents Required | 投标文件要求、需提交的文件 | Required Documents, Bid Documents Required |

### 10. Other Information

| Field | Chinese Keywords | English Keywords |
|-------|------------------|------------------|
| Attachment | 附件、附件下载 | Attachment, Annex, Appendix |
| Clarification | 答疑、澄清 | Clarification, Q&A |
| Addendum | 补遗、补充通知 | Addendum, Supplement, Amendment |
| Source | 来源、信息来源 | Source, Tender Source |
| URL | 网址、链接、链接地址 | URL, Link, Website |

## Regular Expression Patterns

### Date Patterns
- Chinese: `\d{4}年\d{1,2}月\d{1,2}日`
- Chinese (short): `\d{4}-\d{1,2}-\d{1,2}`
- ISO: `\d{4}-\d{2}-\d{2}`
- US: `\d{1,2}/\d{1,2}/\d{4}`
- Time: `\d{1,2}:\d{2}` or `\d{1,2}:\d{2}:\d{2}`

### Money Patterns
- Chinese: `[¥￥]\s*[\d,]+\.?\d*\s*(万元|元|万)?`
- English/General: `[$€£¥]\s*[\d,]+\.?\d*\s*(K|M|B|thousand|million|billion)?`
- General: `[\d,]+\.?\d*\s*(元|万|万元|CNY|RMB|USD|EUR|GBP)`

### Phone Patterns
- China: `1[3-9]\d{9}` or `0\d{2,3}-?\d{7,8}`
- International: `\+\d{1,3}[-\s]?\(?\d{1,4}\)?[-\s]?\d{1,4}[-\s]?\d{1,9}`

### Email Pattern
- General: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`

## Document Structure Patterns

### Chinese Tender Structure
1. 招标公告 (Tender Announcement)
2. 项目概况 (Project Overview)
3. 投标人资格要求 (Bidder Qualification)
4. 招标文件获取 (Obtaining Tender Documents)
5. 投标文件递交 (Bid Submission)
6. 开标 (Bid Opening)
7. 评标办法 (Evaluation Method)
8. 其他事项 (Other Matters)

### English Tender Structure
1. Invitation to Bid / Tender Notice
2. Project Overview / Introduction
3. Qualification Requirements
4. Obtaining Tender Documents
5. Bid Submission
6. Bid Opening
7. Evaluation Criteria
8. Other Information

## Tips for Extraction

1. **Context Matters**: Keywords may appear in multiple contexts. Check surrounding text to determine correct field assignment.

2. **Tables and Lists**: Important information is often in tables or bullet points. Pay special attention to these sections.

3. **Cross-Reference**: The same information (like dates or amounts) may appear multiple times. Verify consistency and use the most authoritative source (often in a dedicated section or table).

4. **Missing Fields**: Not all tenders contain all fields. Mark missing information as "未找到" (Not Found) or "N/A" rather than guessing.

5. **Field Variations**: A single tender may use different terms for the same concept (e.g., both "预算金额" and "最高限价" for budget).

6. **Sections Mapping**: Map extracted content to sections:
   - Basic info → Summary section
   - Requirements → Technical/Commercial sections
   - Timeline → Important Dates section
   - Contacts → Contact Information section
