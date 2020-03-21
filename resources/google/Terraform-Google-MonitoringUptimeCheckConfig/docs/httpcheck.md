# Terraform::Google::MonitoringUptimeCheckConfig HttpCheck

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="httpcheck-headers.md">Headers</a>, ... ]</i>,
    "<a href="#maskheaders" title="MaskHeaders">MaskHeaders</a>" : <i>Boolean</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#usessl" title="UseSsl">UseSsl</a>" : <i>Boolean</i>,
    "<a href="#validatessl" title="ValidateSsl">ValidateSsl</a>" : <i>Boolean</i>,
    "<a href="#authinfo" title="AuthInfo">AuthInfo</a>" : <i>[ <a href="httpcheck-authinfo.md">AuthInfo</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="httpcheck-headers.md">Headers</a></i>
<a href="#maskheaders" title="MaskHeaders">MaskHeaders</a>: <i>Boolean</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#usessl" title="UseSsl">UseSsl</a>: <i>Boolean</i>
<a href="#validatessl" title="ValidateSsl">ValidateSsl</a>: <i>Boolean</i>
<a href="#authinfo" title="AuthInfo">AuthInfo</a>: <i>
      - <a href="httpcheck-authinfo.md">AuthInfo</a></i>
</pre>

## Properties

#### Headers

_Required_: No

_Type_: List of <a href="httpcheck-headers.md">Headers</a>

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

_Type_: List of <a href="httpcheck-authinfo.md">AuthInfo</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

