# TF::Rancher2::ClusterTemplate VsphereCloudProviderDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disk" title="Disk">Disk</a>" : <i>[ <a href="diskdefinition.md">DiskDefinition</a>, ... ]</i>,
    "<a href="#global" title="Global">Global</a>" : <i>[ <a href="globaldefinition.md">GlobalDefinition</a>, ... ]</i>,
    "<a href="#network" title="Network">Network</a>" : <i>[ <a href="networkdefinition.md">NetworkDefinition</a>, ... ]</i>,
    "<a href="#virtualcenter" title="VirtualCenter">VirtualCenter</a>" : <i>[ <a href="virtualcenterdefinition.md">VirtualCenterDefinition</a>, ... ]</i>,
    "<a href="#workspace" title="Workspace">Workspace</a>" : <i>[ <a href="workspacedefinition.md">WorkspaceDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disk" title="Disk">Disk</a>: <i>
      - <a href="diskdefinition.md">DiskDefinition</a></i>
<a href="#global" title="Global">Global</a>: <i>
      - <a href="globaldefinition.md">GlobalDefinition</a></i>
<a href="#network" title="Network">Network</a>: <i>
      - <a href="networkdefinition.md">NetworkDefinition</a></i>
<a href="#virtualcenter" title="VirtualCenter">VirtualCenter</a>: <i>
      - <a href="virtualcenterdefinition.md">VirtualCenterDefinition</a></i>
<a href="#workspace" title="Workspace">Workspace</a>: <i>
      - <a href="workspacedefinition.md">WorkspaceDefinition</a></i>
</pre>

## Properties

#### Disk

_Required_: No

_Type_: List of <a href="diskdefinition.md">DiskDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Global

_Required_: No

_Type_: List of <a href="globaldefinition.md">GlobalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: List of <a href="networkdefinition.md">NetworkDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VirtualCenter

_Required_: No

_Type_: List of <a href="virtualcenterdefinition.md">VirtualCenterDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Workspace

_Required_: No

_Type_: List of <a href="workspacedefinition.md">WorkspaceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

