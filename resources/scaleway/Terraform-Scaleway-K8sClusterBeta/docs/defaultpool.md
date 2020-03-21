# Terraform::Scaleway::K8sClusterBeta DefaultPool

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autohealing" title="Autohealing">Autohealing</a>" : <i>Boolean</i>,
    "<a href="#autoscaling" title="Autoscaling">Autoscaling</a>" : <i>Boolean</i>,
    "<a href="#containerruntime" title="ContainerRuntime">ContainerRuntime</a>" : <i>String</i>,
    "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
    "<a href="#minsize" title="MinSize">MinSize</a>" : <i>Double</i>,
    "<a href="#nodetype" title="NodeType">NodeType</a>" : <i>String</i>,
    "<a href="#placementgroupid" title="PlacementGroupId">PlacementGroupId</a>" : <i>String</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#waitforpoolready" title="WaitForPoolReady">WaitForPoolReady</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#autohealing" title="Autohealing">Autohealing</a>: <i>Boolean</i>
<a href="#autoscaling" title="Autoscaling">Autoscaling</a>: <i>Boolean</i>
<a href="#containerruntime" title="ContainerRuntime">ContainerRuntime</a>: <i>String</i>
<a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
<a href="#minsize" title="MinSize">MinSize</a>: <i>Double</i>
<a href="#nodetype" title="NodeType">NodeType</a>: <i>String</i>
<a href="#placementgroupid" title="PlacementGroupId">PlacementGroupId</a>: <i>String</i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#waitforpoolready" title="WaitForPoolReady">WaitForPoolReady</a>: <i>Boolean</i>
</pre>

## Properties

#### Autohealing

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Autoscaling

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContainerRuntime

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSize

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PlacementGroupId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForPoolReady

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

