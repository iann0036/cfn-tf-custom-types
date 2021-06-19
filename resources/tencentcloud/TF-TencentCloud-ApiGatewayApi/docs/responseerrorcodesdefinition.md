# TF::TencentCloud::ApiGatewayApi ResponseErrorCodesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#code" title="Code">Code</a>" : <i>Double</i>,
    "<a href="#convertedcode" title="ConvertedCode">ConvertedCode</a>" : <i>Double</i>,
    "<a href="#desc" title="Desc">Desc</a>" : <i>String</i>,
    "<a href="#msg" title="Msg">Msg</a>" : <i>String</i>,
    "<a href="#needconvert" title="NeedConvert">NeedConvert</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#code" title="Code">Code</a>: <i>Double</i>
<a href="#convertedcode" title="ConvertedCode">ConvertedCode</a>: <i>Double</i>
<a href="#desc" title="Desc">Desc</a>: <i>String</i>
<a href="#msg" title="Msg">Msg</a>: <i>String</i>
<a href="#needconvert" title="NeedConvert">NeedConvert</a>: <i>Boolean</i>
</pre>

## Properties

#### Code

Custom response configuration error code.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConvertedCode

Custom error code conversion.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Desc

Parameter description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Msg

Custom response configuration error message.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NeedConvert

Whether to enable error code conversion. Default value: `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

