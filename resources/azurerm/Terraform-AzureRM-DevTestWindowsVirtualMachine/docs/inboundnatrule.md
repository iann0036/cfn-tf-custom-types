# Terraform::AzureRM::DevTestWindowsVirtualMachine InboundNatRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backendport" title="BackendPort">BackendPort</a>" : <i>Double</i>,
    "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#backendport" title="BackendPort">BackendPort</a>: <i>Double</i>
<a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
</pre>

## Properties

#### BackendPort

The Backend Port associated with this NAT Rule. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

The Protocol used for this NAT Rule. Possible values are `Tcp` and `Udp`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

