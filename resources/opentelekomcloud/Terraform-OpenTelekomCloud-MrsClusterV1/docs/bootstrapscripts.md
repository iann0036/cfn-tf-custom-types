# Terraform::OpenTelekomCloud::MrsClusterV1 BootstrapScripts

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#activemaster" title="ActiveMaster">ActiveMaster</a>" : <i>Boolean</i>,
    "<a href="#beforecomponentstart" title="BeforeComponentStart">BeforeComponentStart</a>" : <i>Boolean</i>,
    "<a href="#failaction" title="FailAction">FailAction</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#nodes" title="Nodes">Nodes</a>" : <i>[ String, ... ]</i>,
    "<a href="#parameters" title="Parameters">Parameters</a>" : <i>String</i>,
    "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#activemaster" title="ActiveMaster">ActiveMaster</a>: <i>Boolean</i>
<a href="#beforecomponentstart" title="BeforeComponentStart">BeforeComponentStart</a>: <i>Boolean</i>
<a href="#failaction" title="FailAction">FailAction</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#nodes" title="Nodes">Nodes</a>: <i>
      - String</i>
<a href="#parameters" title="Parameters">Parameters</a>: <i>String</i>
<a href="#uri" title="Uri">Uri</a>: <i>String</i>
</pre>

## Properties

#### ActiveMaster

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BeforeComponentStart

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailAction

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nodes

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

