# Domain documentation

This repository currently contains one implemented editorial context: TFB Volume 1. It belongs to a wider project family with the planned TLB Volume 2. DRC is a separate project.

Treat TFB and TLB as bounded editorial contexts sharing a worldview and selected terminology, not as one undifferentiated outline. Until TLB receives its own approved structure, do not create TLB chapters or move organisation-wide technical-leadership material into TFB.

Before changing its structure or terminology, read:

- `AGENTS.md` for project intent, repository boundaries and contributor rules;
- `PROJECT_FAMILY.md` for the audiences and boundaries of TFB, TLB and DRC;
- `OUTLINE.md` for disclosure tiers, chapter boundaries and canonical homes;
- `STYLE_GUIDE.md` for reader, language and source rules;
- `GLOSSARY.md` for published terminology;
- relevant decisions under `docs/adr/` if that directory is added later.

If a root `CONTEXT.md` is added later, treat it as the domain-language source. Do not invent synonyms for terms it defines. If a proposed change contradicts an architecture decision record, surface the conflict instead of silently replacing the decision.
