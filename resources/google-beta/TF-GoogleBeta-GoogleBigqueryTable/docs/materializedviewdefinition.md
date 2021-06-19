# TF::GoogleBeta::GoogleBigqueryTable MaterializedViewDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enablerefresh" title="EnableRefresh">EnableRefresh</a>" : <i>Boolean</i>,
    "<a href="#query" title="Query">Query</a>" : <i>String</i>,
    "<a href="#refreshintervalms" title="RefreshIntervalMs">RefreshIntervalMs</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#enablerefresh" title="EnableRefresh">EnableRefresh</a>: <i>Boolean</i>
<a href="#query" title="Query">Query</a>: <i>String</i>
<a href="#refreshintervalms" title="RefreshIntervalMs">RefreshIntervalMs</a>: <i>Double</i>
</pre>

## Properties

#### EnableRefresh

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RefreshIntervalMs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

