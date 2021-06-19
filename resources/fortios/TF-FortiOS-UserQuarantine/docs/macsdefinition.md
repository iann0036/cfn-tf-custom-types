# TF::FortiOS::UserQuarantine MacsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#drop" title="Drop">Drop</a>" : <i>String</i>,
    "<a href="#entryid" title="EntryId">EntryId</a>" : <i>Double</i>,
    "<a href="#mac" title="Mac">Mac</a>" : <i>String</i>,
    "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#drop" title="Drop">Drop</a>: <i>String</i>
<a href="#entryid" title="EntryId">EntryId</a>: <i>Double</i>
<a href="#mac" title="Mac">Mac</a>: <i>String</i>
<a href="#parent" title="Parent">Parent</a>: <i>String</i>
</pre>

## Properties

#### Description

Description for the quarantine MAC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Drop

Enable/Disable dropping of quarantined device traffic Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EntryId

FSW entry id for the quarantine MAC.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mac

Quarantine MAC.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

Parent entry name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

