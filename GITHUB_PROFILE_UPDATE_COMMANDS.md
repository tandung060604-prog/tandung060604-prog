# Proposed GitHub Profile Metadata Update

These commands were **not executed**. GitHub CLI authentication was invalid during the audit, and location/website values still require confirmation.

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
  -f bio='Robotics & AI Graduate | Building RAG, LLM and practical AI applications'
```

No company value is included because no verified company was provided.

## 3. Add optional fields only after replacing placeholders

Do not run the following example until both placeholders contain real, public values:

```powershell
gh api --method PATCH user `
  -f location='<LOCATION>' `
  -f blog='<PORTFOLIO_URL>'
```

Add social accounts through GitHub only after the corresponding public URLs are confirmed. Never place a token directly in a command or Markdown file.
