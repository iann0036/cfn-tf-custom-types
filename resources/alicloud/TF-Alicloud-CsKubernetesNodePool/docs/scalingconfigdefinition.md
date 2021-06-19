# TF::Alicloud::CsKubernetesNodePool ScalingConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eipbandwidth" title="EipBandwidth">EipBandwidth</a>" : <i>Double</i>,
    "<a href="#eipinternetchargetype" title="EipInternetChargeType">EipInternetChargeType</a>" : <i>String</i>,
    "<a href="#isbondeip" title="IsBondEip">IsBondEip</a>" : <i>Boolean</i>,
    "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
    "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#eipbandwidth" title="EipBandwidth">EipBandwidth</a>: <i>Double</i>
<a href="#eipinternetchargetype" title="EipInternetChargeType">EipInternetChargeType</a>: <i>String</i>
<a href="#isbondeip" title="IsBondEip">IsBondEip</a>: <i>Boolean</i>
<a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
<a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### EipBandwidth

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EipInternetChargeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsBondEip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

