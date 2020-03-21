# Terraform::Vault::GcpSecretRoleset Binding

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#resource" title="Resource">Resource</a>" : <i>String</i>,
    "<a href="#roles" title="Roles">Roles</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#resource" title="Resource">Resource</a>: <i>String</i>
<a href="#roles" title="Roles">Roles</a>: <i>
      - String</i>
</pre>

## Properties

#### Resource

Resource or resource path for which IAM policy information will be bound. The resource path may be specified in a few different [formats](https://www.vaultproject.io/docs/secrets/gcp/index.html#roleset-bindings).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Roles

List of [GCP IAM roles](https://cloud.google.com/iam/docs/understanding-roles) for the resource.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

