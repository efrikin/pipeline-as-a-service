# `projects`

## `Create projects`

### `devops/ci`

```bash
git clone
cd projects/devops/ci
git init
git checkout -b main
git remote add origin http://gitlab/devops/ci.git
git add .
git commit -m '[skip-ci]: Init'
git push --set-upstream origin main
```

### `apps/test`

```bash
cd ../../apps/test
git init
git checkout -b main
git remote add origin http://gitlab/apps/test.git
git add .
git commit -m '[skip-ci]: Init'
git push --set-upstream origin main
```

## `Check`

- Create feature/branch to `devops/ci` project
- Add some feature
- Enjoy!
