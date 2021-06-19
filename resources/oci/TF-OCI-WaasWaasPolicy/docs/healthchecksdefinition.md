# TF::OCI::WaasWaasPolicy HealthChecksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expectedresponsecodegroup" title="ExpectedResponseCodeGroup">ExpectedResponseCodeGroup</a>" : <i>[ String, ... ]</i>,
    "<a href="#expectedresponsetext" title="ExpectedResponseText">ExpectedResponseText</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>" : <i>Double</i>,
    "<a href="#intervalinseconds" title="IntervalInSeconds">IntervalInSeconds</a>" : <i>Double</i>,
    "<a href="#isenabled" title="IsEnabled">IsEnabled</a>" : <i>Boolean</i>,
    "<a href="#isresponsetextcheckenabled" title="IsResponseTextCheckEnabled">IsResponseTextCheckEnabled</a>" : <i>Boolean</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#timeoutinseconds" title="TimeoutInSeconds">TimeoutInSeconds</a>" : <i>Double</i>,
    "<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#expectedresponsecodegroup" title="ExpectedResponseCodeGroup">ExpectedResponseCodeGroup</a>: <i>
      - String</i>
<a href="#expectedresponsetext" title="ExpectedResponseText">ExpectedResponseText</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#healthythreshold" title="HealthyThreshold">HealthyThreshold</a>: <i>Double</i>
<a href="#intervalinseconds" title="IntervalInSeconds">IntervalInSeconds</a>: <i>Double</i>
<a href="#isenabled" title="IsEnabled">IsEnabled</a>: <i>Boolean</i>
<a href="#isresponsetextcheckenabled" title="IsResponseTextCheckEnabled">IsResponseTextCheckEnabled</a>: <i>Boolean</i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#timeoutinseconds" title="TimeoutInSeconds">TimeoutInSeconds</a>: <i>Double</i>
<a href="#unhealthythreshold" title="UnhealthyThreshold">UnhealthyThreshold</a>: <i>Double</i>
</pre>

## Properties

#### ExpectedResponseCodeGroup

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedResponseText

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthyThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsResponseTextCheckEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TimeoutInSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnhealthyThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

