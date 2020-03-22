# Terraform::VSphere::Host

Provides a VMware vSphere host resource. This represents an ESXi host that
can be used either as part of a Compute Cluster or Standalone.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::VSphere::Host",
    "Properties" : {
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>String</i>,
        "<a href="#connected" title="Connected">Connected</a>" : <i>Boolean</i>,
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#force" title="Force">Force</a>" : <i>Boolean</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#license" title="License">License</a>" : <i>String</i>,
        "<a href="#lockdown" title="Lockdown">Lockdown</a>" : <i>String</i>,
        "<a href="#maintenance" title="Maintenance">Maintenance</a>" : <i>Boolean</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#thumbprint" title="Thumbprint">Thumbprint</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::VSphere::Host
Properties:
    <a href="#cluster" title="Cluster">Cluster</a>: <i>String</i>
    <a href="#connected" title="Connected">Connected</a>: <i>Boolean</i>
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#force" title="Force">Force</a>: <i>Boolean</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#license" title="License">License</a>: <i>String</i>
    <a href="#lockdown" title="Lockdown">Lockdown</a>: <i>String</i>
    <a href="#maintenance" title="Maintenance">Maintenance</a>: <i>Boolean</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#thumbprint" title="Thumbprint">Thumbprint</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### Cluster

The ID of the Compute Cluster this host should
be added to. This should not be set if `datacenter` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Connected

If set to false then the host will be disconected.
Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Datacenter

The ID of the datacenter this host should
be added to. This should not be set if `cluster` is set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Force

If set to true then it will force the host to be added, even
if the host is already connected to a different vSphere instance. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

FQDN or IP address of the host to be added.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### License

The license key that will be applied to the host.
The license key is expected to be present in vSphere.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lockdown

Set the lockdown state of the host. Valid options are
`disabled`, `normal`, and `strict`. Default is `disabled`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Maintenance

Set the management state of the host. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Password that will be used by vSphere to authenticate
to the host.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Thumbprint

Host's certificate SHA-1 thumbprint. If not set the the
CA that signed the host's certificate should be trusted. If the CA is not trusted
and no thumbprint is set then the operation will fail.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

Username that will be used by vSphere to authenticate
to the host.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

