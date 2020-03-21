# Terraform::AzureRM::ContainerGroup ImageRegistryCredential

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#password" title="Password">Password</a>" : <i>String</i>,
    "<a href="#server" title="Server">Server</a>" : <i>String</i>,
    "<a href="#username" title="Username">Username</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#password" title="Password">Password</a>: <i>String</i>
<a href="#server" title="Server">Server</a>: <i>String</i>
<a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### Password

The password with which to connect to the registry. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Server

The address to use to connect to the registry without protocol ("https"/"http"). For example: "myacr.acr.io". Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

The username with which to connect to the registry. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

