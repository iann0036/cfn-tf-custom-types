# Terraform::OCI::ApigatewayDeployment Routes Backend

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#body" title="Body">Body</a>" : <i>String</i>,
    "<a href="#connecttimeoutinseconds" title="ConnectTimeoutInSeconds">ConnectTimeoutInSeconds</a>" : <i>Double</i>,
    "<a href="#functionid" title="FunctionId">FunctionId</a>" : <i>String</i>,
    "<a href="#issslverifydisabled" title="IsSslVerifyDisabled">IsSslVerifyDisabled</a>" : <i>Boolean</i>,
    "<a href="#readtimeoutinseconds" title="ReadTimeoutInSeconds">ReadTimeoutInSeconds</a>" : <i>Double</i>,
    "<a href="#sendtimeoutinseconds" title="SendTimeoutInSeconds">SendTimeoutInSeconds</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="routes-backend-headers.md">Headers</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#body" title="Body">Body</a>: <i>String</i>
<a href="#connecttimeoutinseconds" title="ConnectTimeoutInSeconds">ConnectTimeoutInSeconds</a>: <i>Double</i>
<a href="#functionid" title="FunctionId">FunctionId</a>: <i>String</i>
<a href="#issslverifydisabled" title="IsSslVerifyDisabled">IsSslVerifyDisabled</a>: <i>Boolean</i>
<a href="#readtimeoutinseconds" title="ReadTimeoutInSeconds">ReadTimeoutInSeconds</a>: <i>Double</i>
<a href="#sendtimeoutinseconds" title="SendTimeoutInSeconds">SendTimeoutInSeconds</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="routes-backend-headers.md">Headers</a></i>
</pre>

## Properties

#### Body

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectTimeoutInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FunctionId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSslVerifyDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadTimeoutInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendTimeoutInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="routes-backend-headers.md">Headers</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

