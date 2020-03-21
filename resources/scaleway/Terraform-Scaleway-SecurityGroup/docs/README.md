# Terraform::Scaleway::SecurityGroup

**DEPRECATED**: This resource is deprecated and will be removed in `v2.0+`.
Please use `scaleway_instance_security_group` instead.

Provides security groups. This allows security groups to be created, updated and deleted.
For additional details please refer to [API documentation](https://developer.scaleway.com/#security-groups).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Scaleway::SecurityGroup",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabledefaultsecurity" title="EnableDefaultSecurity">EnableDefaultSecurity</a>" : <i>Boolean</i>,
        "<a href="#inbounddefaultpolicy" title="InboundDefaultPolicy">InboundDefaultPolicy</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#outbounddefaultpolicy" title="OutboundDefaultPolicy">OutboundDefaultPolicy</a>" : <i>String</i>,
        "<a href="#stateful" title="Stateful">Stateful</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Scaleway::SecurityGroup
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabledefaultsecurity" title="EnableDefaultSecurity">EnableDefaultSecurity</a>: <i>Boolean</i>
    <a href="#inbounddefaultpolicy" title="InboundDefaultPolicy">InboundDefaultPolicy</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#outbounddefaultpolicy" title="OutboundDefaultPolicy">OutboundDefaultPolicy</a>: <i>String</i>
    <a href="#stateful" title="Stateful">Stateful</a>: <i>Boolean</i>
</pre>

## Properties

#### Description

description of security group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableDefaultSecurity

default: true. Add default security group rules.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundDefaultPolicy

default policy for inbound traffic. Can be one of accept or drop.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

name of security group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutboundDefaultPolicy

default policy for outbound traffic. Can be one of accept or drop.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stateful

default: false. Mark the security group as stateful. Note that stateful security groups can not be associated with bare metal servers.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

