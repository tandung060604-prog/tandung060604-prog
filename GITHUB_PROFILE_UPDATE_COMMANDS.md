# Proposed GitHub Profile Metadata Update

These commands were **not executed**. GitHub CLI authentication was invalid during the audit. The location is confirmed; no public portfolio URL has been provided.

## 1. Authenticate and verify the target account

```powershell
gh auth login -h github.com
gh auth status
gh api user --jq '{login: .login, name: .name, bio: .bio, location: .location, blog: .blog}'
```

Continue only if `login` is exactly `tandung060604-prog`.

## 2. Apply the confirmed fields

```powershell
gh api --method PATCH user `
  -f name='Nguyễn Bùi Tấn Dũng' `
  -f bio='Robotics & AI Graduate | Building RAG, LLM and practical AI applications' `
  -f location='Ha Noi, Vietnam'
```

No company value is included because no verified company was provided.

## 3. Add optional website/social fields only after confirmation

No public portfolio or LinkedIn URL has been provided, so neither should be added to account metadata yet.

```powershell
gh api --method PATCH user `
  -f blog='<PORTFOLIO_URL>'
```

Add social accounts through GitHub only after the corresponding public URLs are confirmed. Never place a token directly in a command or Markdown file.
