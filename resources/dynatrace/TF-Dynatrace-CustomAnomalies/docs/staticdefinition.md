# TF::Dynatrace::CustomAnomalies StaticDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alertcondition" title="AlertCondition">AlertCondition</a>" : <i>String</i>,
    "<a href="#alertingonmissingdata" title="AlertingOnMissingData">AlertingOnMissingData</a>" : <i>Boolean</i>,
    "<a href="#dealertingsamples" title="DealertingSamples">DealertingSamples</a>" : <i>Double</i>,
    "<a href="#samples" title="Samples">Samples</a>" : <i>Double</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#unit" title="Unit">Unit</a>" : <i>String</i>,
    "<a href="#unknowns" title="Unknowns">Unknowns</a>" : <i>String</i>,
    "<a href="#violatingsamples" title="ViolatingSamples">ViolatingSamples</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#alertcondition" title="AlertCondition">AlertCondition</a>: <i>String</i>
<a href="#alertingonmissingdata" title="AlertingOnMissingData">AlertingOnMissingData</a>: <i>Boolean</i>
<a href="#dealertingsamples" title="DealertingSamples">DealertingSamples</a>: <i>Double</i>
<a href="#samples" title="Samples">Samples</a>: <i>Double</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#unit" title="Unit">Unit</a>: <i>String</i>
<a href="#unknowns" title="Unknowns">Unknowns</a>: <i>String</i>
<a href="#violatingsamples" title="ViolatingSamples">ViolatingSamples</a>: <i>Double</i>
</pre>

## Properties

#### AlertCondition

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertingOnMissingData

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DealertingSamples

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Samples

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unit

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Unknowns

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ViolatingSamples

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

