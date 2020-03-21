# Terraform::FlexibleEngine::DdsInstanceV3 Flavor

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#num" title="Num">Num</a>" : <i>Double</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#speccode" title="SpecCode">SpecCode</a>" : <i>String</i>,
    "<a href="#storage" title="Storage">Storage</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#num" title="Num">Num</a>: <i>Double</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#speccode" title="SpecCode">SpecCode</a>: <i>String</i>
<a href="#storage" title="Storage">Storage</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Num

Specifies the node quantity. Valid value:
* the number of mongos ranges from 2 to 12.
* the number of shard ranges from 2 to 12.
* config: the value is 1.
* replica: the value is 1.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

Specifies the disk size. The value must be a multiple of 10. The unit is GB. This parameter
is mandatory for nodes except mongos and invalid for mongos.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpecCode

Specifies the resource specification code. Valid values:.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Storage

Specifies the disk type. Valid value: ULTRAHIGH which indicates the type SSD.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the node type. Valid value: mongos, shard, config, replica.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

