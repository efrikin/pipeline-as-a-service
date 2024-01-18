# pylint: disable=C0103
"""Script generating .gitlab-ci.yml file for dinamic dowstream pipelines."""
#!/usr/bin/python

import os
import sys
import gcip
# from gcip.lib import rules
import gitlab

def get_pipeline_jobs(url, token, env='PP__IS_ENABLED'):
    """Function getting list of projects from different namespaces."""
    jobs = {}
    gl = gitlab.Gitlab(
                    url,
                    token,
            )

    ## Get all namespaces
    namespaces = gl.namespaces.list()
    # pylint: disable=R1702
    for namespace in namespaces:
            ## Administrator's namespace will be skipped
        if namespace.parent_id is None and namespace.id > 1:

            group = gl.groups.get(
                            namespace.name,
                            lazy=True
                    )
            try:
                projects = group.projects.list(
                                include_subgroups=True,
                                all=True
                        )
            ## TODO(efrikin): either need to exclude personal namespace
            ## or create special user for this operaton
            except gitlab.exceptions.GitlabListError:
                continue
            for project in projects:
                    ## If CI/CD was disabled, then skip.
                    ## Settings => Visibility, project features, permissions => CI/CD
                if not project.jobs_enabled:
                    continue
                ci_config_path = '.gitlab-ci.yml'
                p = gl.projects.get(project.id)
                try:
                        ## TODO(efrikin): Currently, need to add project lavel variable
                        ## PP__IS_ENABLED without value and also need to implement
                        ## check group vars
                    _variable = p.variables.get(env)
                    try:
                        ## If repository exist, but it haven't branches, then continue
                        if len(p.branches.list()) == 0:
                            continue
                        ## If .gitlab-ci.yml file stored in other place
                        if project.ci_config_path is not None and len(project.ci_config_path) > 0:
                            ci_config_path = project.ci_config_path
                        _headers = p.files.head(ci_config_path, ref=project.default_branch)
                        jobs[project.path_with_namespace] = ci_config_path
                    ## TODO(efrikin): Need to check
                    except gitlab.exceptions.GitlabHttpError:
                        continue
                except gitlab.exceptions.GitlabGetError:
                    pass
    return jobs

def build_ci_file(jobs):
    """Function generating list of job for testing."""
    pipeline = gcip.Pipeline()
    for job in jobs:
        job = gcip.TriggerJob(
                name=job.replace('/','-'),
                stage="test",
                project=job,
                strategy=gcip.TriggerStrategy.DEPEND,
        )

        job.add_variables(
                PP__IS_ENABLED='true',
                PP__CI_COMMIT_REF_NAME='$CI_COMMIT_REF_NAME',
        )

        # job.append_rules(
        #       rules.on_merge_request_events(),
        #       rules.on_branch('$CI_DEFAULT_BRANCH'),
        #       rules.on_tags(),
        # )

        pipeline.add_children(job)

    return pipeline.write_yaml()

if __name__ == "__main__":
    END_COLOR='\033[0m'
    FAILED_COLOR='\033[41m'
    SUCCESS_COLOR='\033[42m'
    GITLAB__SERVER_URL = os.environ.get('CI_SERVER_URL', 'http://gitlab')
    PP__TOKEN = os.environ.get('PP__TOKEN', 'glpat-LTpLQvQoVZNYsyFdxxA9')

    gitlab_jobs = get_pipeline_jobs(GITLAB__SERVER_URL, PP__TOKEN)
    build_ci_file(gitlab_jobs)
    total = len(gitlab_jobs.keys())
    if total > 0:
        print(f'{SUCCESS_COLOR} ci file was built and contain {total} job(s){END_COLOR}')
    else:
        print(f'{FAILED_COLOR}ci file was built and contain {total} job(s){END_COLOR}')
        sys.exit(1)
