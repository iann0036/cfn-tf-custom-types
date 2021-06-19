# TF::Dynatrace::DatabaseAnomalies

CloudFormation equivalent of dynatrace_database_anomalies

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dynatrace::DatabaseAnomalies",
    "Properties" : {
        "<a href="#dbconnectfailures" title="DbConnectFailures">DbConnectFailures</a>" : <i>[ <a href="dbconnectfailuresdefinition.md">DbConnectFailuresDefinition</a>, ... ]</i>,
        "<a href="#failurerate" title="FailureRate">FailureRate</a>" : <i>[ <a href="failureratedefinition.md">FailureRateDefinition</a>, ... ]</i>,
        "<a href="#load" title="Load">Load</a>" : <i>[ <a href="loaddefinition.md">LoadDefinition</a>, ... ]</i>,
        "<a href="#responsetime" title="ResponseTime">ResponseTime</a>" : <i>[ <a href="responsetimedefinition.md">ResponseTimeDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dynatrace::DatabaseAnomalies
Properties:
    <a href="#dbconnectfailures" title="DbConnectFailures">DbConnectFailures</a>: <i>
      - <a href="dbconnectfailuresdefinition.md">DbConnectFailuresDefinition</a></i>
    <a href="#failurerate" title="FailureRate">FailureRate</a>: <i>
      - <a href="failureratedefinition.md">FailureRateDefinition</a></i>
    <a href="#load" title="Load">Load</a>: <i>
      - <a href="loaddefinition.md">LoadDefinition</a></i>
    <a href="#responsetime" title="ResponseTime">ResponseTime</a>: <i>
      - <a href="responsetimedefinition.md">ResponseTimeDefinition</a></i>
</pre>

## Properties

#### DbConnectFailures

_Required_: No

_Type_: List of <a href="dbconnectfailuresdefinition.md">DbConnectFailuresDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailureRate

_Required_: No

_Type_: List of <a href="failureratedefinition.md">FailureRateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Load

_Required_: No

_Type_: List of <a href="loaddefinition.md">LoadDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseTime

_Required_: No

_Type_: List of <a href="responsetimedefinition.md">ResponseTimeDefinition</a>

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

