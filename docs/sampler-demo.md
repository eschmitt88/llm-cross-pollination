---
kind: demo
name: sampler-demo
added: "2026-08-22"
---

# Sampler demo — 20 blind seeds + 10 keyword-level seeds

Generated with `uv run xpol sample -k 20` (OS-entropy seed, stratified by domain, topic level) and `uv run xpol sample -k 10 --level keyword`. Re-run with `--seed <printed value>` to reproduce.

```
# rng seed 1112379601646157348  level=topic  population=4516  eligible=4516  stratify=domain
 1. Dementia and Cognitive Impairment Research
    Health Sciences > Medicine > Psychiatry and Mental health > Dementia and Cognitive Impairment Research
 2. Electrical and Thermal Properties of Materials
    Physical Sciences > Engineering > Electrical and Electronic Engineering > Electrical and Thermal Properties of Materials
 3. Service-Learning and Community Engagement
    Social Sciences > Social Sciences > Education > Service-Learning and Community Engagement
 4. Mycorrhizal Fungi and Plant Interactions
    Life Sciences > Agricultural and Biological Sciences > Plant Science > Mycorrhizal Fungi and Plant Interactions
 5. Glioma Diagnosis and Treatment
    Health Sciences > Medicine > Genetics > Glioma Diagnosis and Treatment
 6. Information Architecture and Usability
    Physical Sciences > Computer Science > Information Systems > Information Architecture and Usability
 7. Philosophy and Literary Analysis
    Social Sciences > Arts and Humanities > Philosophy > Philosophy and Literary Analysis
 8. Diptera species taxonomy and behavior
    Life Sciences > Agricultural and Biological Sciences > Ecology, Evolution, Behavior and Systematics > Diptera species taxonomy and behavior
 9. Complementary and Alternative Medicine Studies
    Health Sciences > Medicine > Complementary and alternative medicine > Complementary and Alternative Medicine Studies
10. Aluminum Alloy Microstructure Properties
    Physical Sciences > Engineering > Aerospace Engineering > Aluminum Alloy Microstructure Properties
11. African Studies and Ethnography
    Social Sciences > Social Sciences > Sociology and Political Science > African Studies and Ethnography
12. Ginger and Zingiberaceae research
    Life Sciences > Pharmacology, Toxicology and Pharmaceutics > Pharmacology > Ginger and Zingiberaceae research
13. Mobile Health and mHealth Applications
    Health Sciences > Health Professions > General Health Professions > Mobile Health and mHealth Applications
14. Advanced Fiber Optic Sensors
    Physical Sciences > Engineering > Electrical and Electronic Engineering > Advanced Fiber Optic Sensors
15. Healthcare Systems and Technology
    Social Sciences > Business, Management and Accounting > Organizational Behavior and Human Resource Management > Healthcare Systems and Technology
16. Memory Processes and Influences
    Life Sciences > Neuroscience > Cognitive Neuroscience > Memory Processes and Influences
17. Nutrition and Health Studies
    Health Sciences > Medicine > Public Health, Environmental and Occupational Health > Nutrition and Health Studies
18. Advanced Algebra and Geometry
    Physical Sciences > Mathematics > Mathematical Physics > Advanced Algebra and Geometry
19. Philosophy and Historical Thought
    Social Sciences > Arts and Humanities > Philosophy > Philosophy and Historical Thought
20. Microbial Metabolic Engineering and Bioproduction
    Life Sciences > Biochemistry, Genetics and Molecular Biology > Molecular Biology > Microbial Metabolic Engineering and Bioproduction

# rng seed 8826667548409646597  level=keyword  population=45154  eligible=45154  stratify=domain
 1. Waterborne Transmission
    Life Sciences > Immunology and Microbiology > Parasitology > Parasitic Infections and Diagnostics > Waterborne Transmission
 2. Leadership
    Physical Sciences > Environmental Science > Management, Monitoring, Policy and Law > Conservation, Ecology, Wildlife Education > Leadership
 3. Health Service Utilization
    Health Sciences > Medicine > Pediatrics, Perinatology and Child Health > Global Maternal and Child Health > Health Service Utilization
 4. Social Welfare
    Social Sciences > Social Sciences > General Social Sciences > Contemporary Social and Economic Issues > Social Welfare
 5. Isoprenoid Pathway
    Life Sciences > Biochemistry, Genetics and Molecular Biology > Molecular Biology > Plant biochemistry and biosynthesis > Isoprenoid Pathway
 6. Diamond Thin Films
    Physical Sciences > Materials Science > Materials Chemistry > Diamond and Carbon-based Materials Research > Diamond Thin Films
 7. Fibrodysplasia Ossificans Progressiva
    Health Sciences > Medicine > Rheumatology > Heterotopic Ossification and Related Conditions > Fibrodysplasia Ossificans Progressiva
 8. Cultural History
    Social Sciences > Arts and Humanities > Language and Linguistics > Classical Studies and Philology > Cultural History
 9. Complex Diseases
    Life Sciences > Biochemistry, Genetics and Molecular Biology > Genetics > Genetic Associations and Epidemiology > Complex Diseases
10. Nuclear Waste Immobilization
    Physical Sciences > Materials Science > Ceramics and Composites > Glass properties and applications > Nuclear Waste Immobilization
```
