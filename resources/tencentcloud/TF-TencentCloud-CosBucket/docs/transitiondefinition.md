# TF::TencentCloud::CosBucket TransitionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#date" title="Date">Date</a>" : <i>String</i>,
    "<a href="#days" title="Days">Days</a>" : <i>Double</i>,
    "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#date" title="Date">Date</a>: <i>String</i>
<a href="#days" title="Days">Days</a>: <i>Double</i>
<a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
</pre>

## Properties

#### Date

Specifies the date after which you want the corresponding action to take effect.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Days

Specifies the number of days after object creation when the specific rule action takes effect.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

Specifies the storage class to which you want the object to transition. Available values include `STANDARD`, `STANDARD_IA` and `ARCHIVE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

