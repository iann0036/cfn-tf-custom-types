# Terraform::AzureRM::ServiceFabricCluster ApplicationPorts

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endport" title="EndPort">EndPort</a>" : <i>Double</i>,
    "<a href="#startport" title="StartPort">StartPort</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#endport" title="EndPort">EndPort</a>: <i>Double</i>
<a href="#startport" title="StartPort">StartPort</a>: <i>Double</i>
</pre>

## Properties

#### EndPort

The end of the Application Port Range on this Node Type.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartPort

The start of the Application Port Range on this Node Type.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

