# TF::Volterra::Discovery AccessInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#incluster" title="InCluster">InCluster</a>" : <i>Boolean</i>,
    "<a href="#isolated" title="Isolated">Isolated</a>" : <i>Boolean</i>,
    "<a href="#reachable" title="Reachable">Reachable</a>" : <i>Boolean</i>,
    "<a href="#connectioninfo" title="ConnectionInfo">ConnectionInfo</a>" : <i>[ <a href="connectioninfodefinition.md">ConnectionInfoDefinition</a>, ... ]</i>,
    "<a href="#kubeconfigurl" title="KubeconfigUrl">KubeconfigUrl</a>" : <i>[ <a href="kubeconfigurldefinition.md">KubeconfigUrlDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#incluster" title="InCluster">InCluster</a>: <i>Boolean</i>
<a href="#isolated" title="Isolated">Isolated</a>: <i>Boolean</i>
<a href="#reachable" title="Reachable">Reachable</a>: <i>Boolean</i>
<a href="#connectioninfo" title="ConnectionInfo">ConnectionInfo</a>: <i>
      - <a href="connectioninfodefinition.md">ConnectionInfoDefinition</a></i>
<a href="#kubeconfigurl" title="KubeconfigUrl">KubeconfigUrl</a>: <i>
      - <a href="kubeconfigurldefinition.md">KubeconfigUrlDefinition</a></i>
</pre>

## Properties

#### InCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Isolated

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Reachable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionInfo

_Required_: No

_Type_: List of <a href="connectioninfodefinition.md">ConnectionInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubeconfigUrl

_Required_: No

_Type_: List of <a href="kubeconfigurldefinition.md">KubeconfigUrlDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

