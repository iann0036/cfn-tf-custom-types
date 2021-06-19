# Heroku Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/heroku**. The below arguments may be included as the key/value or JSON properties in the secret:

* `api_key` - (Required) Heroku API token. It must be provided, but it can also
  be sourced from [other locations](#Authentication).

* `email` - (Required) Email to be notified by Heroku. It must be provided, but
  it can also be sourced from [other locations](#Authentication).

* `headers` - (Optional) Additional Headers to be sent to Heroku.

* `customizations` - (Optional) Various attributes altering the behavior of certain resources.

  * `set_app_all_config_vars_in_state` - (Optional) Controls whether the `heroku_app.all_config_vars` attribute
    is set in the state file. The aforementioned attribute stores a snapshot of all config vars in Terraform state,
    even if they are not defined in Terraform. This means sensitive Heroku add-on config vars,
    such as Postgres' `DATABASE_URL`, are always accessible in the state.
    Set to `false` to only track managed config vars in the state. Defaults to `true`.

* `delays` - (Optional) Delays help mitigate issues that can arise due to
  Heroku's eventually consistent data model. Only a single `delays` block may be

  * `post_app_create_delay` - (Optional) The number of seconds to wait after an
    app is created. Default is to wait 5 seconds.

  * `post_space_create_delay` - (Optional) The number of seconds to wait after a
    private space is created. Default is to wait 5 seconds.

  * `post_domain_create_delay` - (Optional) The number of seconds to wait after
    a domain is created. Default is to wait 5 seconds.

* `timeouts` - (Optional) Define a max duration the provider will wait for certain resources
  to be properly modified before proceeding with further action(s). Only a single `timeouts` block may be specified,

  * `addon_create_timeout` - (Optional) The number of minutes for the provider to wait for an addon to be
  created/provisioned. Defaults to 20 minutes. Minimum required value is 10 minutes.

## Supported Resources

* [TF::Heroku::AccountFeature](../resources/heroku/TF-Heroku-AccountFeature/docs/README.md)
* [TF::Heroku::AddonAttachment](../resources/heroku/TF-Heroku-AddonAttachment/docs/README.md)
* [TF::Heroku::Addon](../resources/heroku/TF-Heroku-Addon/docs/README.md)
* [TF::Heroku::AppConfigAssociation](../resources/heroku/TF-Heroku-AppConfigAssociation/docs/README.md)
* [TF::Heroku::AppFeature](../resources/heroku/TF-Heroku-AppFeature/docs/README.md)
* [TF::Heroku::AppRelease](../resources/heroku/TF-Heroku-AppRelease/docs/README.md)
* [TF::Heroku::AppWebhook](../resources/heroku/TF-Heroku-AppWebhook/docs/README.md)
* [TF::Heroku::App](../resources/heroku/TF-Heroku-App/docs/README.md)
* [TF::Heroku::Build](../resources/heroku/TF-Heroku-Build/docs/README.md)
* [TF::Heroku::Cert](../resources/heroku/TF-Heroku-Cert/docs/README.md)
* [TF::Heroku::Collaborator](../resources/heroku/TF-Heroku-Collaborator/docs/README.md)
* [TF::Heroku::Config](../resources/heroku/TF-Heroku-Config/docs/README.md)
* [TF::Heroku::Domain](../resources/heroku/TF-Heroku-Domain/docs/README.md)
* [TF::Heroku::Drain](../resources/heroku/TF-Heroku-Drain/docs/README.md)
* [TF::Heroku::Formation](../resources/heroku/TF-Heroku-Formation/docs/README.md)
* [TF::Heroku::PipelineConfigVar](../resources/heroku/TF-Heroku-PipelineConfigVar/docs/README.md)
* [TF::Heroku::PipelineCoupling](../resources/heroku/TF-Heroku-PipelineCoupling/docs/README.md)
* [TF::Heroku::Pipeline](../resources/heroku/TF-Heroku-Pipeline/docs/README.md)
* [TF::Heroku::ReviewAppConfig](../resources/heroku/TF-Heroku-ReviewAppConfig/docs/README.md)
* [TF::Heroku::Slug](../resources/heroku/TF-Heroku-Slug/docs/README.md)
* [TF::Heroku::SpaceAppAccess](../resources/heroku/TF-Heroku-SpaceAppAccess/docs/README.md)
* [TF::Heroku::SpaceInboundRuleset](../resources/heroku/TF-Heroku-SpaceInboundRuleset/docs/README.md)
* [TF::Heroku::SpacePeeringConnectionAccepter](../resources/heroku/TF-Heroku-SpacePeeringConnectionAccepter/docs/README.md)
* [TF::Heroku::SpaceVpnConnection](../resources/heroku/TF-Heroku-SpaceVpnConnection/docs/README.md)
* [TF::Heroku::Space](../resources/heroku/TF-Heroku-Space/docs/README.md)
* [TF::Heroku::TeamCollaborator](../resources/heroku/TF-Heroku-TeamCollaborator/docs/README.md)
* [TF::Heroku::TeamMember](../resources/heroku/TF-Heroku-TeamMember/docs/README.md)