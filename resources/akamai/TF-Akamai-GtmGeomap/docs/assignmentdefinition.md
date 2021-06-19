# TF::Akamai::GtmGeomap AssignmentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#countries" title="Countries">Countries</a>" : <i>[ String, ... ]</i>,
    "<a href="#datacenterid" title="DatacenterId">DatacenterId</a>" : <i>Double</i>,
    "<a href="#nickname" title="Nickname">Nickname</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#countries" title="Countries">Countries</a>: <i>
      - String</i>
<a href="#datacenterid" title="DatacenterId">DatacenterId</a>: <i>Double</i>
<a href="#nickname" title="Nickname">Nickname</a>: <i>String</i>
</pre>

## Properties

#### Countries

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatacenterId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nickname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

