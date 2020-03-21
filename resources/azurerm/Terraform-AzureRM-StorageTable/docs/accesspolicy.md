# Terraform::AzureRM::StorageTable AccessPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expiry" title="Expiry">Expiry</a>" : <i>String</i>,
    "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>,
    "<a href="#start" title="Start">Start</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#expiry" title="Expiry">Expiry</a>: <i>String</i>
<a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
<a href="#start" title="Start">Start</a>: <i>String</i>
</pre>

## Properties

#### Expiry

The ISO8061 UTC time at which this Access Policy should be valid until.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

The permissions which should associated with this Shared Identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

The ISO8061 UTC time at which this Access Policy should be valid from.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

