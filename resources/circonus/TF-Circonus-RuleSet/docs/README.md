# TF::Circonus::RuleSet

The ``circonus_rule_set`` resource creates and manages a
[Circonus Rule Set](https://login.circonus.com/resources/api/calls/rule_set).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Circonus::RuleSet",
    "Properties" : {
        "<a href="#check" title="Check">Check</a>" : <i>String</i>,
        "<a href="#link" title="Link">Link</a>" : <i>String</i>,
        "<a href="#metricfilter" title="MetricFilter">MetricFilter</a>" : <i>String</i>,
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#metricpattern" title="MetricPattern">MetricPattern</a>" : <i>String</i>,
        "<a href="#metrictype" title="MetricType">MetricType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#userjson" title="UserJson">UserJson</a>" : <i>String</i>,
        "<a href="#if" title="If">If</a>" : <i>[ <a href="ifdefinition.md">IfDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Circonus::RuleSet
Properties:
    <a href="#check" title="Check">Check</a>: <i>String</i>
    <a href="#link" title="Link">Link</a>: <i>String</i>
    <a href="#metricfilter" title="MetricFilter">MetricFilter</a>: <i>String</i>
    <a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
    <a href="#metricpattern" title="MetricPattern">MetricPattern</a>: <i>String</i>
    <a href="#metrictype" title="MetricType">MetricType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#userjson" title="UserJson">UserJson</a>: <i>String</i>
    <a href="#if" title="If">If</a>: <i>
      - <a href="ifdefinition.md">IfDefinition</a></i>
</pre>

## Properties

#### Check

The Circonus ID that this Rule Set will use to search for
a metric stream to alert on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Link

A link to external documentation (or anything else you
feel is important) when a notification is sent.  This value will show up in
email alerts and the Circonus UI.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

The name of the metric stream within a given check
that this rule set is active on.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricPattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricType

The type of metric this rule set will operate on.
Valid values are `numeric` (the default) and `text`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

Notes about this rule set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

A Circonus Metric ID that, if specified and active with
a severity 1 alert, will silence this rule set until all of the severity 1
alerts on the parent clear.  This value must match the format
`${check_id}_${metric_name}`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags assigned to this rule set.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserJson

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### If

_Required_: No

_Type_: List of <a href="ifdefinition.md">IfDefinition</a>

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

#### RuleSetId

Returns the <code>RuleSetId</code> value.

