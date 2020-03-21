# Terraform::OCI::LoadBalancerBackendSet HealthChecker

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#intervalms" title="IntervalMs">IntervalMs</a>" : <i>Double</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
    "<a href="#responsebodyregex" title="ResponseBodyRegex">ResponseBodyRegex</a>" : <i>String</i>,
    "<a href="#retries" title="Retries">Retries</a>" : <i>Double</i>,
    "<a href="#returncode" title="ReturnCode">ReturnCode</a>" : <i>Double</i>,
    "<a href="#timeoutinmillis" title="TimeoutInMillis">TimeoutInMillis</a>" : <i>Double</i>,
    "<a href="#urlpath" title="UrlPath">UrlPath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#intervalms" title="IntervalMs">IntervalMs</a>: <i>Double</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
<a href="#responsebodyregex" title="ResponseBodyRegex">ResponseBodyRegex</a>: <i>String</i>
<a href="#retries" title="Retries">Retries</a>: <i>Double</i>
<a href="#returncode" title="ReturnCode">ReturnCode</a>: <i>Double</i>
<a href="#timeoutinmillis" title="TimeoutInMillis">TimeoutInMillis</a>: <i>Double</i>
<a href="#urlpath" title="UrlPath">UrlPath</a>: <i>String</i>
</pre>

## Properties

#### IntervalMs

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseBodyRegex

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReturnCode

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutInMillis

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlPath

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

