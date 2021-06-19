# TF::Spotinst::ElastigroupAzure HealthCheckDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autohealing" title="AutoHealing">AutoHealing</a>" : <i>Boolean</i>,
    "<a href="#graceperiod" title="GracePeriod">GracePeriod</a>" : <i>Double</i>,
    "<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#autohealing" title="AutoHealing">AutoHealing</a>: <i>Boolean</i>
<a href="#graceperiod" title="GracePeriod">GracePeriod</a>: <i>Double</i>
<a href="#healthchecktype" title="HealthCheckType">HealthCheckType</a>: <i>String</i>
</pre>

## Properties

#### AutoHealing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracePeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

