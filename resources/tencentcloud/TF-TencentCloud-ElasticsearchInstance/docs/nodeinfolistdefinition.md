# TF::TencentCloud::ElasticsearchInstance NodeInfoListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disksize" title="DiskSize">DiskSize</a>" : <i>Double</i>,
    "<a href="#disktype" title="DiskType">DiskType</a>" : <i>String</i>,
    "<a href="#encrypt" title="Encrypt">Encrypt</a>" : <i>Boolean</i>,
    "<a href="#nodenum" title="NodeNum">NodeNum</a>" : <i>Double</i>,
    "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#disksize" title="DiskSize">DiskSize</a>: <i>Double</i>
<a href="#disktype" title="DiskType">DiskType</a>: <i>String</i>
<a href="#encrypt" title="Encrypt">Encrypt</a>: <i>Boolean</i>
<a href="#nodenum" title="NodeNum">NodeNum</a>: <i>Double</i>
<a href="#nodetype" title="NodeType">NodeType</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### DiskSize

Node disk size. Unit is GB, and default value is `100`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskType

Node disk type. Valid values are `CLOUD_SSD` and `CLOUD_PREMIUM`. The default value is `CLOUD_SSD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypt

Decides to encrypt this disk or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeNum

Number of nodes.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

Node specification, and valid values refer to [document of tencentcloud](https://intl.cloud.tencent.com/document/product/845/18376).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Node type. Valid values are `hotData`, `warmData` and `dedicatedMaster`. The default value is 'hotData`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

