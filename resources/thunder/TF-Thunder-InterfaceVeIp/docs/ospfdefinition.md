# TF::Thunder::InterfaceVeIp OspfDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ospfglobal" title="OspfGlobal">OspfGlobal</a>" : <i>[ <a href="ospfglobaldefinition.md">OspfGlobalDefinition</a>, ... ]</i>,
    "<a href="#ospfiplist" title="OspfIpList">OspfIpList</a>" : <i>[ <a href="ospfiplistdefinition.md">OspfIpListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ospfglobal" title="OspfGlobal">OspfGlobal</a>: <i>
      - <a href="ospfglobaldefinition.md">OspfGlobalDefinition</a></i>
<a href="#ospfiplist" title="OspfIpList">OspfIpList</a>: <i>
      - <a href="ospfiplistdefinition.md">OspfIpListDefinition</a></i>
</pre>

## Properties

#### OspfGlobal

_Required_: No

_Type_: List of <a href="ospfglobaldefinition.md">OspfGlobalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OspfIpList

_Required_: No

_Type_: List of <a href="ospfiplistdefinition.md">OspfIpListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

