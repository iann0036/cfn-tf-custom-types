# Terraform::AzureStack::VirtualMachineScaleSet OsProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
    "<a href="#computernameprefix" title="ComputerNamePrefix">ComputerNamePrefix</a>" : <i>String</i>,
    "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
<a href="#computernameprefix" title="ComputerNamePrefix">ComputerNamePrefix</a>: <i>String</i>
<a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
</pre>

## Properties

#### AdminPassword

Specifies the administrator password to use for all the instances of virtual machines in a scale set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

Specifies the administrator account name to use for all the instances of virtual machines in the scale set.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputerNamePrefix

Specifies the computer name prefix for all of the virtual machines in the scale set. Computer name prefixes must be 1 to 9 characters long for windows images and 1 - 58 for linux. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomData

Specifies custom data to supply to the machine. On linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, Terraform will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

