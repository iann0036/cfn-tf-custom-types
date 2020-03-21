# Terraform::Google::ComputeInstance ServiceAccount

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#email" title="Email">Email</a>" : <i>String</i>,
    "<a href="#scopes" title="Scopes">Scopes</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#email" title="Email">Email</a>: <i>String</i>
<a href="#scopes" title="Scopes">Scopes</a>: <i>
      - String</i>
</pre>

## Properties

#### Email

The service account e-mail address. If not given, the
default Google Compute Engine service account is used.
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scopes

A list of service scopes. Both OAuth2 URLs and gcloud
short names are supported. To allow full access to all Cloud APIs, use the
`cloud-platform` scope. See a complete list of scopes [here](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes#--scopes).
**Note**: [`allow_stopping_for_update`](#allow_stopping_for_update) must be set to true or your instance must have a `desired_status` of `TERMINATED` in order to update this field.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

