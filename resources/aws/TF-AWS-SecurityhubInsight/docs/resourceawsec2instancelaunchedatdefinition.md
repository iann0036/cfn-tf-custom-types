# TF::AWS::SecurityhubInsight ResourceAwsEc2InstanceLaunchedAtDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#end" title="End">End</a>" : <i>String</i>,
    "<a href="#start" title="Start">Start</a>" : <i>String</i>,
    "<a href="#daterange" title="DateRange">DateRange</a>" : <i>[ <a href="daterangedefinition.md">DateRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#end" title="End">End</a>: <i>String</i>
<a href="#start" title="Start">Start</a>: <i>String</i>
<a href="#daterange" title="DateRange">DateRange</a>: <i>
      - <a href="daterangedefinition.md">DateRangeDefinition</a></i>
</pre>

## Properties

#### End

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Start

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DateRange

_Required_: No

_Type_: List of <a href="daterangedefinition.md">DateRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

