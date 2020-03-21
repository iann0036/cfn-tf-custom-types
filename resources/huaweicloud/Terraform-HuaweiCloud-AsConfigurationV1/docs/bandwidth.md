# Terraform::HuaweiCloud::AsConfigurationV1 Bandwidth

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#chargingmode" title="ChargingMode">ChargingMode</a>" : <i>String</i>,
    "<a href="#sharetype" title="ShareType">ShareType</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#chargingmode" title="ChargingMode">ChargingMode</a>: <i>String</i>
<a href="#sharetype" title="ShareType">ShareType</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
</pre>

## Properties

#### ChargingMode

The bandwidth charging mode. The system only supports `traffic`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShareType

The bandwidth sharing type. The system only supports `PER` (indicates exclusive bandwidth).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The bandwidth (Mbit/s). The value range is 1 to 300.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

