# Terraform::CloudStack::Instance

Creates and automatically starts a virtual machine based on a service offering,
disk offering, and template.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::CloudStack::Instance",
    "Properties" : {
        "<a href="#affinitygroupids" title="AffinityGroupIds">AffinityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#affinitygroupnames" title="AffinityGroupNames">AffinityGroupNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#expunge" title="Expunge">Expunge</a>" : <i>Boolean</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#ipaddress" title="IpAddress">IpAddress</a>" : <i>String</i>,
        "<a href="#keypair" title="Keypair">Keypair</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#rootdisksize" title="RootDiskSize">RootDiskSize</a>" : <i>Double</i>,
        "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#securitygroupnames" title="SecurityGroupNames">SecurityGroupNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#serviceoffering" title="ServiceOffering">ServiceOffering</a>" : <i>String</i>,
        "<a href="#startvm" title="StartVm">StartVm</a>" : <i>Boolean</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::CloudStack::Instance
Properties:
    <a href="#affinitygroupids" title="AffinityGroupIds">AffinityGroupIds</a>: <i>
      - String</i>
    <a href="#affinitygroupnames" title="AffinityGroupNames">AffinityGroupNames</a>: <i>
      - String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#expunge" title="Expunge">Expunge</a>: <i>Boolean</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#ipaddress" title="IpAddress">IpAddress</a>: <i>String</i>
    <a href="#keypair" title="Keypair">Keypair</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#rootdisksize" title="RootDiskSize">RootDiskSize</a>: <i>Double</i>
    <a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
    <a href="#securitygroupnames" title="SecurityGroupNames">SecurityGroupNames</a>: <i>
      - String</i>
    <a href="#serviceoffering" title="ServiceOffering">ServiceOffering</a>: <i>String</i>
    <a href="#startvm" title="StartVm">StartVm</a>: <i>Boolean</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### AffinityGroupIds

List of affinity group IDs to apply to this
instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AffinityGroupNames

List of affinity group names to apply to
this instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The display name of the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expunge

This determines if the instance is expunged when it is
destroyed (defaults false).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

The group name of the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddress

The IP address to assign to this instance. Changing
this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Keypair

The name of the SSH key pair that will be used to
access this instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

The ID of the network to connect this instance
to. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

The name or ID of the project to deploy this
instance to. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootDiskSize

The size of the root disk in gigabytes. The
root disk is resized on deploy. Only applies to template-based deployments.
Changing this forces a new resource to be created.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

List of security group IDs to apply to this
instance. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupNames

List of security group names to apply to
this instance. Changing this forces a new resource to be created.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceOffering

The name or ID of the service offering used
for this instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartVm

This determines if the instances is started after it
is created (defaults true).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The name or ID of the template used for this
instance. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

The user data to provide when launching the
instance. This can be either plain text or base64 encoded text.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

The name or ID of the zone where this instance will be
created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

