# TF::AzureRM::PointToSiteVpnGateway PropagatedRouteTableDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ids" title="Ids">Ids</a>" : <i>[ String, ... ]</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ids" title="Ids">Ids</a>: <i>
      - String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - String</i>
</pre>

## Properties

#### Ids

The list of Virtual Hub Route Table resource id which the routes will be propagated to.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

The list of labels to logically group Virtual Hub Route Tables which the routes will be propagated to.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

