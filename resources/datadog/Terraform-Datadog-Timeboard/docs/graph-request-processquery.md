# Terraform::Datadog::Timeboard Graph Request ProcessQuery

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#filterby" title="FilterBy">FilterBy</a>" : <i>[ String, ... ]</i>,
    "<a href="#limit" title="Limit">Limit</a>" : <i>Double</i>,
    "<a href="#metric" title="Metric">Metric</a>" : <i>String</i>,
    "<a href="#searchby" title="SearchBy">SearchBy</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#filterby" title="FilterBy">FilterBy</a>: <i>
      - String</i>
<a href="#limit" title="Limit">Limit</a>: <i>Double</i>
<a href="#metric" title="Metric">Metric</a>: <i>String</i>
<a href="#searchby" title="SearchBy">SearchBy</a>: <i>String</i>
</pre>

## Properties

#### FilterBy

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Limit

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metric

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SearchBy

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

