# TF::FortiOS::RouterbgpNeighbor ConditionalAdvertiseDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#advertiseroutemap" title="AdvertiseRoutemap">AdvertiseRoutemap</a>" : <i>String</i>,
    "<a href="#conditionroutemap" title="ConditionRoutemap">ConditionRoutemap</a>" : <i>String</i>,
    "<a href="#conditiontype" title="ConditionType">ConditionType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#advertiseroutemap" title="AdvertiseRoutemap">AdvertiseRoutemap</a>: <i>String</i>
<a href="#conditionroutemap" title="ConditionRoutemap">ConditionRoutemap</a>: <i>String</i>
<a href="#conditiontype" title="ConditionType">ConditionType</a>: <i>String</i>
</pre>

## Properties

#### AdvertiseRoutemap

Name of advertising route map.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionRoutemap

Name of condition route map.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConditionType

Type of condition. Valid values: `exist`, `non-exist`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

