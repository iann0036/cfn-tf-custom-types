# Terraform::Circonus::RuleSet

CloudFormation equivalent of circonus_rule_set

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Circonus::RuleSet",
    "Properties" : {
        "<a href="#check" title="Check">Check</a>" : <i>String</i>,
        "<a href="#link" title="Link">Link</a>" : <i>String</i>,
        "<a href="#metricfilter" title="MetricFilter">MetricFilter</a>" : <i>String</i>,
        "<a href="#metricname" title="MetricName">MetricName</a>" : <i>String</i>,
        "<a href="#metricpattern" title="MetricPattern">MetricPattern</a>" : <i>String</i>,
        "<a href="#metrictype" title="MetricType">MetricType</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#if" title="If">If</a>" : <i>[ <a href="if.md">If</a>, ... ]</i>,
        "<a href="#then" title="Then">Then</a>" : <i>[ <a href="then.md">Then</a>, ... ]</i>,
        "<a href="#value" title="Value">Value</a>" : <i>[ <a href="value.md">Value</a>, ... ]</i>,
        "<a href="#over" title="Over">Over</a>" : <i>[ <a href="over.md">Over</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Circonus::RuleSet
Properties:
    <a href="#check" title="Check">Check</a>: <i>String</i>
    <a href="#link" title="Link">Link</a>: <i>String</i>
    <a href="#metricfilter" title="MetricFilter">MetricFilter</a>: <i>String</i>
    <a href="#metricname" title="MetricName">MetricName</a>: <i>String</i>
    <a href="#metricpattern" title="MetricPattern">MetricPattern</a>: <i>String</i>
    <a href="#metrictype" title="MetricType">MetricType</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#if" title="If">If</a>: <i>
      - <a href="if.md">If</a></i>
    <a href="#then" title="Then">Then</a>: <i>
      - <a href="then.md">Then</a></i>
    <a href="#value" title="Value">Value</a>: <i>
      - <a href="value.md">Value</a></i>
    <a href="#over" title="Over">Over</a>: <i>
      - <a href="over.md">Over</a></i>
</pre>

## Properties

#### Check

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Link

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricPattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### If

_Required_: No

_Type_: List of <a href="if.md">If</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Then

_Required_: No

_Type_: List of <a href="then.md">Then</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

_Required_: No

_Type_: List of <a href="value.md">Value</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Over

_Required_: No

_Type_: List of <a href="over.md">Over</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### RuleSetId

Returns the <code>RuleSetId</code> value.

