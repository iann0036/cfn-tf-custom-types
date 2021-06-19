# TF::AVI::Virtualservice ServicesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>" : <i>Boolean</i>,
    "<a href="#enablessl" title="EnableSsl">EnableSsl</a>" : <i>Boolean</i>,
    "<a href="#overrideapplicationprofileref" title="OverrideApplicationProfileRef">OverrideApplicationProfileRef</a>" : <i>String</i>,
    "<a href="#overridenetworkprofileref" title="OverrideNetworkProfileRef">OverrideNetworkProfileRef</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#portrangeend" title="PortRangeEnd">PortRangeEnd</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#enablehttp2" title="EnableHttp2">EnableHttp2</a>: <i>Boolean</i>
<a href="#enablessl" title="EnableSsl">EnableSsl</a>: <i>Boolean</i>
<a href="#overrideapplicationprofileref" title="OverrideApplicationProfileRef">OverrideApplicationProfileRef</a>: <i>String</i>
<a href="#overridenetworkprofileref" title="OverrideNetworkProfileRef">OverrideNetworkProfileRef</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#portrangeend" title="PortRangeEnd">PortRangeEnd</a>: <i>Double</i>
</pre>

## Properties

#### EnableHttp2

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableSsl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideApplicationProfileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideNetworkProfileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PortRangeEnd

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

