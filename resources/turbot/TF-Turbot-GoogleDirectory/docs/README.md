# TF::Turbot::GoogleDirectory

The `Turbot Google Directory` resource adds support for google directory. It is used to create, manage and delete directory settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::GoogleDirectory",
    "Properties" : {
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#groupidtemplate" title="GroupIdTemplate">GroupIdTemplate</a>" : <i>String</i>,
        "<a href="#hostedname" title="HostedName">HostedName</a>" : <i>String</i>,
        "<a href="#loginnametemplate" title="LoginNameTemplate">LoginNameTemplate</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#pgpkey" title="PgpKey">PgpKey</a>" : <i>String</i>,
        "<a href="#poolid" title="PoolId">PoolId</a>" : <i>String</i>,
        "<a href="#profileidtemplate" title="ProfileIdTemplate">ProfileIdTemplate</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#title" title="Title">Title</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::GoogleDirectory
Properties:
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#groupidtemplate" title="GroupIdTemplate">GroupIdTemplate</a>: <i>String</i>
    <a href="#hostedname" title="HostedName">HostedName</a>: <i>String</i>
    <a href="#loginnametemplate" title="LoginNameTemplate">LoginNameTemplate</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#pgpkey" title="PgpKey">PgpKey</a>: <i>String</i>
    <a href="#poolid" title="PoolId">PoolId</a>: <i>String</i>
    <a href="#profileidtemplate" title="ProfileIdTemplate">ProfileIdTemplate</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#title" title="Title">Title</a>: <i>String</i>
</pre>

## Properties

#### ClientId

Client ID provided by Google.
- `client_secret` - (Required) Client Secret provided by Google.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `hosted_name` - (Optional) Domain name of the organization.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this directory.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

Client Secret provided by Google.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `hosted_name` - (Optional) Domain name of the organization.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this directory.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Brief description of the purpose and details of the directory.
- `hosted_name` - (Optional) Domain name of the organization.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this directory.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupIdTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostedName

Domain name of the organization.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this directory.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoginNameTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

ID or `aka` of the parent resource.
- `title` - (Required) Short descriptive name for the directory.
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through a google directory. For example, email id of the user.
- `client_id` - (Required) Client ID provided by Google.
- `client_secret` - (Required) Client Secret provided by Google.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `hosted_name` - (Optional) Domain name of the organization.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this directory.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PgpKey

A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProfileIdTemplate

A template to generate profile id for users authenticated through a google directory. For example, email id of the user.
- `client_id` - (Required) Client ID provided by Google.
- `client_secret` - (Required) Client Secret provided by Google.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `hosted_name` - (Optional) Domain name of the organization.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this directory.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Labels that can be used to manage, group, categorize, search, and save metadata for this directory.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Title

Short descriptive name for the directory.
- `profile_id_template` - (Required) A template to generate profile id for users authenticated through a google directory. For example, email id of the user.
- `client_id` - (Required) Client ID provided by Google.
- `client_secret` - (Required) Client Secret provided by Google.
- `description` - (Optional) Brief description of the purpose and details of the directory.
- `hosted_name` - (Optional) Domain name of the organization.
- `tags` - (Optional) Labels that can be used to manage, group, categorize, search, and save metadata for this directory.
- `pgp_key` - (Optional) A base-64 encoded PGP public key, applies on resource creation. If specified, the resource is encrypted in the state file with the key specified.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DirectoryType

Returns the <code>DirectoryType</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyFingerprint

Returns the <code>KeyFingerprint</code> value.

#### ParentAkas

Returns the <code>ParentAkas</code> value.

#### Status

Returns the <code>Status</code> value.

