# TF::Google::MonitoringUptimeCheckConfig HttpCheckDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#body" title="Body">Body</a>" : <i>String</i>,
    "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#maskheaders" title="MaskHeaders">MaskHeaders</a>" : <i>Boolean</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#requestmethod" title="RequestMethod">RequestMethod</a>" : <i>String</i>,
    "<a href="#usessl" title="UseSsl">UseSsl</a>" : <i>Boolean</i>,
    "<a href="#validatessl" title="ValidateSsl">ValidateSsl</a>" : <i>Boolean</i>,
    "<a href="#authinfo" title="AuthInfo">AuthInfo</a>" : <i>[ <a href="authinfodefinition.md">AuthInfoDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#body" title="Body">Body</a>: <i>String</i>
<a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#maskheaders" title="MaskHeaders">MaskHeaders</a>: <i>Boolean</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#requestmethod" title="RequestMethod">RequestMethod</a>: <i>String</i>
<a href="#usessl" title="UseSsl">UseSsl</a>: <i>Boolean</i>
<a href="#validatessl" title="ValidateSsl">ValidateSsl</a>: <i>Boolean</i>
<a href="#authinfo" title="AuthInfo">AuthInfo</a>: <i>
      - <a href="authinfodefinition.md">AuthInfoDefinition</a></i>
</pre>

## Properties

#### Body

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaskHeaders

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequestMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseSsl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidateSsl

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthInfo

_Required_: No

_Type_: List of <a href="authinfodefinition.md">AuthInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

