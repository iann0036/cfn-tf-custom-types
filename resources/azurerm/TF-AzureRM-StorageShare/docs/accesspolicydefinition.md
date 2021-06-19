# TF::AzureRM::StorageShare AccessPolicyDefinition

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

The time at which this Access Policy should be valid until, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

The permissions which should be associated with this Shared Identifier. Possible value is combination of `r` (read), `w` (write), `d` (delete), and `l` (list).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

The time at which this Access Policy should be valid from, in [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) format.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

