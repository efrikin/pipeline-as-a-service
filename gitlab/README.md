# `gitlab`

## `Deploy`

```bash
docker compose -f gitlab/compose.yaml up -d
```

### `Register runner`

```bash
docker exec -ti gitlab-gitlab-runner-1 gitlab-runner register --registration-token TOKEN
```

### `Get token`

**Admin Area => CI/CD => Runner**

## `Configuration`

### `Create groups`

**Creating `devops` and `apps` groups**

### `Add variables`

**Settings => CI/CD => Variables**

#### `Instalce/Group level`

- `PP__CI_COMMIT_REF_NAME=main` (non-protected, non-masked)

##### `Personal Access Token`

- `PP__TOKEN=Personal Access Token` (non-protected, masked)

**Personal Access Token must have following permissions:**

- `read_api`
- `read_user`
- `read_repository`

#### `Project level`

**PP__IS_ENABLED must be defined(i.e. without value)**

- `PP__IS_ENABLED` (non-protected, non-masked)

## `References`

- [Registering Runner](https://docs.gitlab.com/runner/register/)
- [Register with a runner authentication token](https://docs.gitlab.com/runner/register/?tab=Docker#register-with-a-runner-authentication-token)
- [Create a group](https://docs.gitlab.com/ee/user/group/#create-a-group)
- [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
- [CI/CD variable expressions](https://docs.gitlab.com/ee/ci/jobs/job_control.html#cicd-variable-expressions)
