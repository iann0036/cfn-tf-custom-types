# Terraform::FlexibleEngine::CesAlarmrule

CloudFormation equivalent of flexibleengine_ces_alarmrule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::FlexibleEngine::CesAlarmrule",
    "Properties" : {
        "<a href="#alarmactionenabled" title="AlarmActionEnabled">AlarmActionEnabled</a>" : <i>Boolean</i>,
        "<a href="#alarmdescription" title="AlarmDescription">AlarmDescription</a>" : <i>String</i>,
        "<a href="#alarmenabled" title="AlarmEnabled">AlarmEnabled</a>" : <i>Boolean</i>,
        "<a href="#alarmname" title="AlarmName">AlarmName</a>" : <i>String</i>,
        "<a href="#alarmstate" title="AlarmState">AlarmState</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#updatetime" title="UpdateTime">UpdateTime</a>" : <i>Double</i>,
        "<a href="#alarmactions" title="AlarmActions">AlarmActions</a>" : <i>[ &lt;a href=&#34;alarmactions.md&#34;&gt;AlarmActions&lt;/a&gt;, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;, ... ]</i>,
        "<a href="#insufficientdataactions" title="InsufficientdataActions">InsufficientdataActions</a>" : <i>[ &lt;a href=&#34;insufficientdataactions.md&#34;&gt;InsufficientdataActions&lt;/a&gt;, ... ]</i>,
        "<a href="#metric" title="Metric">Metric</a>" : <i>[ &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;, ... ]</i>,
        "<a href="#okactions" title="OkActions">OkActions</a>" : <i>[ &lt;a href=&#34;okactions.md&#34;&gt;OkActions&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#dimensions" title="Dimensions">Dimensions</a>" : <i>[ &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::FlexibleEngine::CesAlarmrule
Properties:
    <a href="#alarmactionenabled" title="AlarmActionEnabled">AlarmActionEnabled</a>: <i>Boolean</i>
    <a href="#alarmdescription" title="AlarmDescription">AlarmDescription</a>: <i>String</i>
    <a href="#alarmenabled" title="AlarmEnabled">AlarmEnabled</a>: <i>Boolean</i>
    <a href="#alarmname" title="AlarmName">AlarmName</a>: <i>String</i>
    <a href="#alarmstate" title="AlarmState">AlarmState</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#updatetime" title="UpdateTime">UpdateTime</a>: <i>Double</i>
    <a href="#alarmactions" title="AlarmActions">AlarmActions</a>: <i>
      - &lt;a href=&#34;alarmactions.md&#34;&gt;AlarmActions&lt;/a&gt;</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;</i>
    <a href="#insufficientdataactions" title="InsufficientdataActions">InsufficientdataActions</a>: <i>
      - &lt;a href=&#34;insufficientdataactions.md&#34;&gt;InsufficientdataActions&lt;/a&gt;</i>
    <a href="#metric" title="Metric">Metric</a>: <i>
      - &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;</i>
    <a href="#okactions" title="OkActions">OkActions</a>: <i>
      - &lt;a href=&#34;okactions.md&#34;&gt;OkActions&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#dimensions" title="Dimensions">Dimensions</a>: <i>
      - &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;</i>
</pre>

## Properties

#### AlarmActionEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpdateTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlarmActions

_Required_: No

_Type_: List of &lt;a href=&#34;alarmactions.md&#34;&gt;AlarmActions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsufficientdataActions

_Required_: No

_Type_: List of &lt;a href=&#34;insufficientdataactions.md&#34;&gt;InsufficientdataActions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: No

_Type_: List of &lt;a href=&#34;metric.md&#34;&gt;Metric&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OkActions

_Required_: No

_Type_: List of &lt;a href=&#34;okactions.md&#34;&gt;OkActions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dimensions

_Required_: No

_Type_: List of &lt;a href=&#34;dimensions.md&#34;&gt;Dimensions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

