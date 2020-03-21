# Heroku Provider

## Configuration

To configure this resource, you must create an AWS Secrets Manager secret with the name **terraform/heroku**. The below arguments may be included as the key/value or JSON properties in the secret or metadata object:

* `api_key` - (Required) Heroku API token. It must be provided, but it can also
  be sourced from [other locations](#Authentication).

* `email` - (Required) Email to be notified by Heroku. It must be provided, but
  it can also be sourced from [other locations](#Authentication).

* `headers` - (Optional) Additional Headers to be sent to Heroku.

* `delays` - (Optional) Delays help mitigate issues that can arise due to
  Heroku's eventually consistent data model. Only a single `delays` block may be

  * `post_app_create_delay` - (Optional) The number of seconds to wait after an
    app is created. Default is to wait 5 seconds.

  * `post_space_create_delay` - (Optional) The number of seconds to wait after a
    private space is created. Default is to wait 5 seconds.

  * `post_domain_create_delay` - (Optional) The number of seconds to wait after
    a domain is created. Default is to wait 5 seconds.


## Supported Resources

* [Terraform::Heroku::AccountFeature](../resources/heroku/Terraform-Heroku-AccountFeature/docs/README.md)
* [Terraform::Heroku::AddonAttachment](../resources/heroku/Terraform-Heroku-AddonAttachment/docs/README.md)
* [Terraform::Heroku::Addon](../resources/heroku/Terraform-Heroku-Addon/docs/README.md)
* [Terraform::Heroku::AppConfigAssociation](../resources/heroku/Terraform-Heroku-AppConfigAssociation/docs/README.md)
* [Terraform::Heroku::AppFeature](../resources/heroku/Terraform-Heroku-AppFeature/docs/README.md)
* [Terraform::Heroku::AppRelease](../resources/heroku/Terraform-Heroku-AppRelease/docs/README.md)
* [Terraform::Heroku::AppWebhook](../resources/heroku/Terraform-Heroku-AppWebhook/docs/README.md)
* [Terraform::Heroku::App](../resources/heroku/Terraform-Heroku-App/docs/README.md)
* [Terraform::Heroku::Build](../resources/heroku/Terraform-Heroku-Build/docs/README.md)
* [Terraform::Heroku::Cert](../resources/heroku/Terraform-Heroku-Cert/docs/README.md)
* [Terraform::Heroku::Config](../resources/heroku/Terraform-Heroku-Config/docs/README.md)
* [Terraform::Heroku::Domain](../resources/heroku/Terraform-Heroku-Domain/docs/README.md)
* [Terraform::Heroku::Drain](../resources/heroku/Terraform-Heroku-Drain/docs/README.md)
* [Terraform::Heroku::Formation](../resources/heroku/Terraform-Heroku-Formation/docs/README.md)
* [Terraform::Heroku::PipelineCoupling](../resources/heroku/Terraform-Heroku-PipelineCoupling/docs/README.md)
* [Terraform::Heroku::Pipeline](../resources/heroku/Terraform-Heroku-Pipeline/docs/README.md)
* [Terraform::Heroku::Slug](../resources/heroku/Terraform-Heroku-Slug/docs/README.md)
* [Terraform::Heroku::SpaceAppAccess](../resources/heroku/Terraform-Heroku-SpaceAppAccess/docs/README.md)
* [Terraform::Heroku::SpaceInboundRuleset](../resources/heroku/Terraform-Heroku-SpaceInboundRuleset/docs/README.md)
* [Terraform::Heroku::SpacePeeringConnectionAccepter](../resources/heroku/Terraform-Heroku-SpacePeeringConnectionAccepter/docs/README.md)
* [Terraform::Heroku::SpaceVpnConnection](../resources/heroku/Terraform-Heroku-SpaceVpnConnection/docs/README.md)
* [Terraform::Heroku::Space](../resources/heroku/Terraform-Heroku-Space/docs/README.md)
* [Terraform::Heroku::TeamCollaborator](../resources/heroku/Terraform-Heroku-TeamCollaborator/docs/README.md)
* [Terraform::Heroku::TeamMember](../resources/heroku/Terraform-Heroku-TeamMember/docs/README.md)