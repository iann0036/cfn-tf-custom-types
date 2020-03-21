# Terraform::AzureRM::IothubDps LinkedHub

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allocationweight" title="AllocationWeight">AllocationWeight</a>" : <i>Double</i>,
    "<a href="#applyallocationpolicy" title="ApplyAllocationPolicy">ApplyAllocationPolicy</a>" : <i>Boolean</i>,
    "<a href="#connectionstring" title="ConnectionString">ConnectionString</a>" : <i>String</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#allocationweight" title="AllocationWeight">AllocationWeight</a>: <i>Double</i>
<a href="#applyallocationpolicy" title="ApplyAllocationPolicy">ApplyAllocationPolicy</a>: <i>Boolean</i>
<a href="#connectionstring" title="ConnectionString">ConnectionString</a>: <i>String</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
</pre>

## Properties

#### AllocationWeight

The weight applied to the IoT Hub. Defaults to 0.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplyAllocationPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectionString

The connection string to connect to the IoT Hub. Changing this forces a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The location of the IoT hub. Changing this forces a new resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

