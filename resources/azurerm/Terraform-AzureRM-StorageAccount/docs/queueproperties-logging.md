# Terraform::AzureRM::StorageAccount QueueProperties Logging

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#delete" title="Delete">Delete</a>" : <i>Boolean</i>,
    "<a href="#read" title="Read">Read</a>" : <i>Boolean</i>,
    "<a href="#retentionpolicydays" title="RetentionPolicyDays">RetentionPolicyDays</a>" : <i>Double</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#write" title="Write">Write</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#delete" title="Delete">Delete</a>: <i>Boolean</i>
<a href="#read" title="Read">Read</a>: <i>Boolean</i>
<a href="#retentionpolicydays" title="RetentionPolicyDays">RetentionPolicyDays</a>: <i>Double</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#write" title="Write">Write</a>: <i>Boolean</i>
</pre>

## Properties

#### Delete

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Read

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicyDays

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Write

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

