# TF::Volterra::GcpVpcSite CustomStaticRouteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#attrs" title="Attrs">Attrs</a>" : <i>[ String, ... ]</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
    "<a href="#nexthop" title="Nexthop">Nexthop</a>" : <i>[ <a href="nexthopdefinition.md">NexthopDefinition</a>, ... ]</i>,
    "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ <a href="subnetsdefinition.md">SubnetsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#attrs" title="Attrs">Attrs</a>: <i>
      - String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
<a href="#nexthop" title="Nexthop">Nexthop</a>: <i>
      - <a href="nexthopdefinition.md">NexthopDefinition</a></i>
<a href="#subnets" title="Subnets">Subnets</a>: <i>
      - <a href="subnetsdefinition.md">SubnetsDefinition</a></i>
</pre>

## Properties

#### Attrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nexthop

_Required_: No

_Type_: List of <a href="nexthopdefinition.md">NexthopDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: List of <a href="subnetsdefinition.md">SubnetsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

