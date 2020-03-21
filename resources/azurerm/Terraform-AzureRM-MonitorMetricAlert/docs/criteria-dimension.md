# Terraform::AzureRM::MonitorMetricAlert Criteria Dimension

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#operator" title="Operator">Operator</a>" : <i>String</i>,
    "<a href="#values" title="Values">Values</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#operator" title="Operator">Operator</a>: <i>String</i>
<a href="#values" title="Values">Values</a>: <i>
      - String</i>
</pre>

## Properties

#### Name

One of the dimension names.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operator

The dimension operator. Possible values are `Include` and `Exclude`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Values

The list of dimension values.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

