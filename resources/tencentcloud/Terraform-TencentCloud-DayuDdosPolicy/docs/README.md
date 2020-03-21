# Terraform::TencentCloud::DayuDdosPolicy

CloudFormation equivalent of tencentcloud_dayu_ddos_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::DayuDdosPolicy",
    "Properties" : {
        "<a href="#blackips" title="BlackIps">BlackIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcetype" title="ResourceType">ResourceType</a>" : <i>String</i>,
        "<a href="#whiteips" title="WhiteIps">WhiteIps</a>" : <i>[ String, ... ]</i>,
        "<a href="#dropoptions" title="DropOptions">DropOptions</a>" : <i>[ <a href="dropoptions.md">DropOptions</a>, ... ]</i>,
        "<a href="#packetfilters" title="PacketFilters">PacketFilters</a>" : <i>[ <a href="packetfilters.md">PacketFilters</a>, ... ]</i>,
        "<a href="#portfilters" title="PortFilters">PortFilters</a>" : <i>[ <a href="portfilters.md">PortFilters</a>, ... ]</i>,
        "<a href="#watermarkfilters" title="WatermarkFilters">WatermarkFilters</a>" : <i>[ <a href="watermarkfilters.md">WatermarkFilters</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::DayuDdosPolicy
Properties:
    <a href="#blackips" title="BlackIps">BlackIps</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcetype" title="ResourceType">ResourceType</a>: <i>String</i>
    <a href="#whiteips" title="WhiteIps">WhiteIps</a>: <i>
      - String</i>
    <a href="#dropoptions" title="DropOptions">DropOptions</a>: <i>
      - <a href="dropoptions.md">DropOptions</a></i>
    <a href="#packetfilters" title="PacketFilters">PacketFilters</a>: <i>
      - <a href="packetfilters.md">PacketFilters</a></i>
    <a href="#portfilters" title="PortFilters">PortFilters</a>: <i>
      - <a href="portfilters.md">PortFilters</a></i>
    <a href="#watermarkfilters" title="WatermarkFilters">WatermarkFilters</a>: <i>
      - <a href="watermarkfilters.md">WatermarkFilters</a></i>
</pre>

## Properties

#### BlackIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WhiteIps

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DropOptions

_Required_: No

_Type_: List of <a href="dropoptions.md">DropOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PacketFilters

_Required_: No

_Type_: List of <a href="packetfilters.md">PacketFilters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortFilters

_Required_: No

_Type_: List of <a href="portfilters.md">PortFilters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WatermarkFilters

_Required_: No

_Type_: List of <a href="watermarkfilters.md">WatermarkFilters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreateTime

Returns the <code>CreateTime</code> value.

#### PolicyId

Returns the <code>PolicyId</code> value.

#### SceneId

Returns the <code>SceneId</code> value.

#### WatermarkKey

Returns the <code>WatermarkKey</code> value.

