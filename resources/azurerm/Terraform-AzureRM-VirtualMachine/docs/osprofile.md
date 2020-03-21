# Terraform::AzureRM::VirtualMachine OsProfile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#adminpassword" title="AdminPassword">AdminPassword</a>" : <i>String</i>,
    "<a href="#adminusername" title="AdminUsername">AdminUsername</a>" : <i>String</i>,
    "<a href="#computername" title="ComputerName">ComputerName</a>" : <i>String</i>,
    "<a href="#customdata" title="CustomData">CustomData</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#adminpassword" title="AdminPassword">AdminPassword</a>: <i>String</i>
<a href="#adminusername" title="AdminUsername">AdminUsername</a>: <i>String</i>
<a href="#computername" title="ComputerName">ComputerName</a>: <i>String</i>
<a href="#customdata" title="CustomData">CustomData</a>: <i>String</i>
</pre>

## Properties

#### AdminPassword

The password associated with the local administrator account.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUsername

Specifies the name of the local administrator account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputerName

Specifies the name of the Virtual Machine.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomData

Specifies custom data to supply to the machine. On Linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, Terraform will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

