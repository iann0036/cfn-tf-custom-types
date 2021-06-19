# TF::Thunder::InterfaceVe RouterDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#isis" title="Isis">Isis</a>" : <i>[ <a href="isisdefinition.md">IsisDefinition</a>, ... ]</i>,
    "<a href="#ospf" title="Ospf">Ospf</a>" : <i>[ <a href="ospfdefinition.md">OspfDefinition</a>, ... ]</i>,
    "<a href="#ripng" title="Ripng">Ripng</a>" : <i>[ <a href="ripngdefinition.md">RipngDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#isis" title="Isis">Isis</a>: <i>
      - <a href="isisdefinition.md">IsisDefinition</a></i>
<a href="#ospf" title="Ospf">Ospf</a>: <i>
      - <a href="ospfdefinition.md">OspfDefinition</a></i>
<a href="#ripng" title="Ripng">Ripng</a>: <i>
      - <a href="ripngdefinition.md">RipngDefinition</a></i>
</pre>

## Properties

#### Isis

_Required_: No

_Type_: List of <a href="isisdefinition.md">IsisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ospf

_Required_: No

_Type_: List of <a href="ospfdefinition.md">OspfDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ripng

_Required_: No

_Type_: List of <a href="ripngdefinition.md">RipngDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

