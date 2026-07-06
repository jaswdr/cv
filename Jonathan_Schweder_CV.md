# Jonathan Schweder

<cv@jaswdr.dev> • Santa Catarina, Brazil • <https://linkedin.com/in/jaswdr>

## SUMMARY

Senior Software Engineer with 16+ years of experience, specializing in designing and scaling distributed backend systems. Owned AWS Lambda control-plane services that processed billions of requests weekly, built internal platform APIs and tooling at MongoDB, and now build payroll processing services at Remote, a global HR platform. Focused on correctness, reliability, and API design, with a track record of mentoring engineers and leading cross-team design reviews. Writes design docs, RFCs, runbooks, postmortems, and user documentation, and works asynchronously across time zones. Experienced in on-call for production services, performance profiling, load testing and benchmarking, and daily use of AI coding agents. Core stack: Elixir, Go, Python, and Kubernetes.

## EXPERIENCE

### Remote, Senior Backend Engineer

May 2026 - Present

- Design and build multi-country payroll processing backend services in Elixir and Phoenix, on PostgreSQL, Kafka, and Redis.
- Design PostgreSQL schemas and migrations for payroll data and tune slow queries; build event-driven services on Kafka, with Redis for caching, rate limits, and background jobs.
- Develop fault tolerant payroll run workflows with retries and idempotency, with a focus on correctness and auditability, in compliance with local legislation.
- Keep payroll pipelines reliable as part of the on-call rotation, with metrics, distributed tracing, and automated validation of payroll outputs.
- Partner with product and compliance teams to ship payroll features that work across legal jurisdictions.
- Mentor engineers and lead design reviews for backend services.
- Use AI coding agents in daily development, and review and test the code they produce before it ships.
- Write unit and integration tests, enforce test coverage in CI, and review other engineers' code.

### MongoDB, Software Engineer - Platform Tools & Services

May 2025 - Apr 2026

- Increased deployment velocity by 40% by leading a team of 3 engineers that built internal self-service tools and APIs in Go and Kubernetes, adopted by 10+ engineering teams, with Crossplane and Argo CD automating infrastructure provisioning.
- Owned the self-service platform end to end, from gathering requirements with its users to launch and improvements after launch.
- Saved 16 hours/week of manual toil and enabled zero-downtime canary and staged rollouts by building automated maintenance workflows and CI/CD improvements with Argo Workflows and Drone CI.
- Sped up incident resolution by 30% and improved developer self-service by integrating LLMs (OpenAI, Anthropic) into developer support tools through internal APIs, and adopted AI coding agents in daily development.
- Implemented distributed tracing and metrics with OpenTelemetry, Prometheus, and Grafana, providing visibility into platform health and performance.
- Ran PostgreSQL in production with high availability, replication, and backups, and used Elasticsearch for log search and analytics during incidents.
- Took part in the on-call rotation for platform services built on PostgreSQL, Kafka, Redis, and Elasticsearch, debugging failing Kubernetes pods and jobs, in a team working asynchronously across time zones.
- Led cross-team design reviews for global services, focusing on API consistency, security (Okta, OIDC), and developer ergonomics.

### Amazon Web Services (AWS), Software Development Engineer - AWS Lambda

Apr 2024 - May 2025

- Owned low latency, fault tolerant Lambda function state transition services in Java and Go, including on-call, serving millions of developers and processing billions of requests weekly through the Lambda Control Plane API.
- Mentored 4 engineers on core Lambda architecture and operational excellence, improving team code review velocity by 25%.
- Cut MTTA by 40% by migrating legacy monitoring to a high-cardinality stack on AWS Kinesis and Athena, enabling real-time performance insights.
- Accelerated region launches by 30% and reduced manual operations by 90% by leading a team of 3 engineers from requirements to launch and later iterations of an automated capacity deployment system with CloudFormation.
- Built event-driven services on Kafka, using Redis for caching and distributed locks.

### Amazon Web Services (AWS), Systems Development Engineer - AWS Networking

Mar 2020 - Apr 2024

- Maintained a high-concurrency internal workflow engine in Python that managed hundreds of thousands of network devices daily.
- Built data pipelines with AWS Glue, EMR, Kinesis, and Kafka to process network telemetry, enabling automated detection and remediation of network events impacting millions of customers.
- Automated global compute capacity deployment with AWS CDK and Ruby, cutting manual provisioning work and regional deployment risk.
- Reduced large-scale events (LSEs) by 20% by developing an automated ticket prioritization system that improved impact analysis.
- Built a ranking algorithm using LLMs and traditional machine learning techniques to optimize how network engineers work through hundreds of daily tickets.
- Served as platform subject matter expert and on-call engineer for global network events, developing automation tools for rapid traffic shifting to mitigate customer impact.

### Pantacor, Software Engineer - IoT & Infrastructure

Feb 2019 - Mar 2020

- Managed Kubernetes clusters across AWS, Google Cloud, and DigitalOcean, as part of a fully remote team.

### Eventials, Systems Analyst - Backend & Integrations

Jul 2018 - Feb 2019

### Bludata Software, Software & Web Developer

Sep 2014 - Jul 2018

### Pomerplast, Software Developer

Feb 2010 - Sep 2014

## EDUCATION

### IGTI
Master of Business Administration (MBA) • Software Engineering • 2018 - 2020

### FURB - Fundação Universidade Regional de Blumenau
Bachelor’s Degree • Computer Science • 2010 - 2015

## LICENSES & CERTIFICATIONS

- [AWS Cloud Solutions Architect Professional Certificate](https://coursera.org/verify/professional-cert/NXAYYAXL6FRW) (Coursera)
- [Google Data Analytics Professional Certificate](https://www.coursera.org/account/accomplishments/specialization/certificate/VFN4TACZWH4G) (Coursera)

## SKILLS

- **Languages & Frameworks:** Elixir (Phoenix), Go, Python, Java, TypeScript, JavaScript (Node.js), Ruby, PHP, SQL, Bash, HTML/CSS
- **Cloud Infrastructure:** AWS (Lambda, EKS, S3, RDS, VPC, IAM, CDK, CloudFormation, Kinesis, Athena, Glue, EMR), Google Cloud, Kubernetes, Docker, Crossplane, Terraform, Terragrunt
- **DevOps & Observability:** GitOps (Argo CD), CI/CD (GitHub Actions, Jenkins, Drone, Argo Workflows), OpenTelemetry, Prometheus, Grafana, NGINX, Git, Helm, Ansible
- **Data & Databases:** MongoDB (Atlas), PostgreSQL, Redis, Kafka, Elasticsearch, DynamoDB, Amazon DocumentDB, SQLite, Data Modeling, Pandas, NumPy
- **AI/ML:** LLM Integration (OpenAI, Anthropic), Machine Learning
- **Architecture & Engineering:** System Design, Distributed Systems, Scalability, API Design (REST/gRPC), Microservices, Serverless, Infrastructure as Code (IaC), Developer Experience (DX), Security (OAuth2, OIDC, Okta), IoT, Embedded Linux
- **Testing & Practices:** Pytest, Selenium, Performance & Stress Testing, Unit/Integration/Regression Testing, Agile/Scrum

## HONORS & AWARDS

- **AWS Ownership Award**, Amazon Web Services: Recognized for exceptional ownership and delivery of high-impact solutions for global customers.
- **Startup Incubation**, Instituto Gene: EPlus project accepted into a startup incubation program focused on educational technology.
