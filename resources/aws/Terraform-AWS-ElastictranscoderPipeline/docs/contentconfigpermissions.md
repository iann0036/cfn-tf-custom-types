# Terraform::AWS::ElastictranscoderPipeline ContentConfigPermissions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#access" title="Access">Access</a>" : <i>[ String, ... ]</i>,
    "<a href="#grantee" title="Grantee">Grantee</a>" : <i>String</i>,
    "<a href="#granteetype" title="GranteeType">GranteeType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#access" title="Access">Access</a>: <i>
      - String</i>
<a href="#grantee" title="Grantee">Grantee</a>: <i>String</i>
<a href="#granteetype" title="GranteeType">GranteeType</a>: <i>String</i>
</pre>

## Properties

#### Access

The permission that you want to give to the AWS user that you specified in `content_config_permissions.grantee`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Grantee

The AWS user or group that you want to have access to transcoded files and playlists.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GranteeType

Specify the type of value that appears in the `content_config_permissions.grantee` object. Valid values are `Canonical`, `Email` or `Group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

