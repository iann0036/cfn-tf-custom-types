# Terraform::Google::ContainerNodePool Management

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autorepair" title="AutoRepair">AutoRepair</a>" : <i>Boolean</i>,
    "<a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#autorepair" title="AutoRepair">AutoRepair</a>: <i>Boolean</i>
<a href="#autoupgrade" title="AutoUpgrade">AutoUpgrade</a>: <i>Boolean</i>
</pre>

## Properties

#### AutoRepair

Whether the nodes will be automatically repaired.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoUpgrade

Whether the nodes will be automatically upgraded.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

