# Terraform::AWS::CodedeployDeploymentGroup TriggerConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#triggerevents" title="TriggerEvents">TriggerEvents</a>" : <i>[ String, ... ]</i>,
    "<a href="#triggername" title="TriggerName">TriggerName</a>" : <i>String</i>,
    "<a href="#triggertargetarn" title="TriggerTargetArn">TriggerTargetArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#triggerevents" title="TriggerEvents">TriggerEvents</a>: <i>
      - String</i>
<a href="#triggername" title="TriggerName">TriggerName</a>: <i>String</i>
<a href="#triggertargetarn" title="TriggerTargetArn">TriggerTargetArn</a>: <i>String</i>
</pre>

## Properties

#### TriggerEvents

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TriggerTargetArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

