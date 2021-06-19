# TF::Nutanix::RecoveryPlan StageListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#delaytimesecs" title="DelayTimeSecs">DelayTimeSecs</a>" : <i>Double</i>,
    "<a href="#stageuuid" title="StageUuid">StageUuid</a>" : <i>String</i>,
    "<a href="#stagework" title="StageWork">StageWork</a>" : <i>[ <a href="stageworkdefinition.md">StageWorkDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#delaytimesecs" title="DelayTimeSecs">DelayTimeSecs</a>: <i>Double</i>
<a href="#stageuuid" title="StageUuid">StageUuid</a>: <i>String</i>
<a href="#stagework" title="StageWork">StageWork</a>: <i>
      - <a href="stageworkdefinition.md">StageWorkDefinition</a></i>
</pre>

## Properties

#### DelayTimeSecs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StageWork

_Required_: No

_Type_: List of <a href="stageworkdefinition.md">StageWorkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

