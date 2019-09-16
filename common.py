#!/usr/bin/env python

import yaml

global_exclusion_list = ['api_form_aws_access_key_id', 'api_form_aws_secret_access_key', 'camunda_aws_access_key_id', 'camunda_aws_secret_access_key', 'cop_ops_sql_clients_aws_access_key_id', 'cop_ops_sql_clients_aws_secret_access_key', 'docker_password', 'docker_username', 'docker_credentials', 'doc_cop_aws_access_key_id', 'doc_cop_aws_secret_access_key','drone_private_token', 'drone_public_token', 'executor_aws_access_key_id', 'executor_aws_secret_access_key', 'flyway_image', 'flyway_tag', 'formbuilder_aws_access_key_id', 'formbuilder_aws_secret_access_key','nginx_image', 'nginx_tag', 'postgres_image', 'postgres_tag', 'quay_username', 'quay_password', 'report_aws_access_key_id', 'report_aws_secret_access_key', 'slack_webhook']

env_exclusion_list = ['analytics_site_id', 'analytics_url', 'api_cop_port', 'api_cop_protocol', 'api_cop_url', 'api_ref_port', 'api_ref_protocol', 'api_ref_url', 'db_cop_protocol', 'db_cop_port', 'db_cop_hostname', 'db_cop_options', 'db_cop_operations_dbname', 'db_operations_schema', 'db_cop_operations_authenticator_username', 'db_cop_operations_authenticator_password', 'drone_aws_access_key_id', 'drone_aws_secret_access_key', 'keycloak_protocol', 'keycloak_realm', 'keycloak_url', 'kube_server', 'kube_token', 'redis_port', 'redis_ssl', 'redis_token', 'redis_url', 'report_url', 'whitelist', 'www_port', 'www_protocol', 'www_url']

def summaryStatus(success_list, error_list):
    print ('Successful secrets')
    print ('------------------')
    for success_item in success_list:
        print(success_item)

    print ('\n\nUnsuccessful secrets')
    print ('--------------------')
    for error_item in error_list:
        print(error_item)


def validateFile(src_file):
    try:
        data = yaml.safe_load(open(src_file))
        return True
    except yaml.YAMLError as e:
        print(e)
        return False


def validateArgs(arguments):
    # TODO
    # if logging in, mfa needs to be supplied
    # if update, service, env_deploy needs to be supplied
    return True
