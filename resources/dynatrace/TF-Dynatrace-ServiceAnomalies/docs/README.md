# TF::Dynatrace::ServiceAnomalies

CloudFormation equivalent of dynatrace_service_anomalies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::ServiceAnomalies",
    "Properties" : {
        "<a href="#failurerates" title="FailureRates">FailureRates</a>" : <i>[ <a href="failureratesdefinition.md">FailureRatesDefinition</a>, ... ]</i>,
        "<a href="#load" title="Load">Load</a>" : <i>[ <a href="loaddefinition.md">LoadDefinition</a>, ... ]</i>,
        "<a href="#loaddrops" title="LoadDrops">LoadDrops</a>" : <i>[ <a href="loaddropsdefinition.md">LoadDropsDefinition</a>, ... ]</i>,
        "<a href="#responsetimes" title="ResponseTimes">ResponseTimes</a>" : <i>[ <a href="responsetimesdefinition.md">ResponseTimesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::ServiceAnomalies
Properties:
    <a href="#failurerates" title="FailureRates">FailureRates</a>: <i>
      - <a href="failureratesdefinition.md">FailureRatesDefinition</a></i>
    <a href="#load" title="Load">Load</a>: <i>
      - <a href="loaddefinition.md">LoadDefinition</a></i>
    <a href="#loaddrops" title="LoadDrops">LoadDrops</a>: <i>
      - <a href="loaddropsdefinition.md">LoadDropsDefinition</a></i>
    <a href="#responsetimes" title="ResponseTimes">ResponseTimes</a>: <i>
      - <a href="responsetimesdefinition.md">ResponseTimesDefinition</a></i>
</pre>

## Properties

#### FailureRates

_Required_: No

_Type_: List of <a href="failureratesdefinition.md">FailureRatesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Load

_Required_: No

_Type_: List of <a href="loaddefinition.md">LoadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadDrops

_Required_: No

_Type_: List of <a href="loaddropsdefinition.md">LoadDropsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTimes

_Required_: No

_Type_: List of <a href="responsetimesdefinition.md">ResponseTimesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

