# Terraform::AWS::DefaultNetworkAcl

Provides a resource to manage the default AWS Network ACL. VPC Only.

Each VPC created in AWS comes with a Default Network ACL that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource.

The `aws_default_network_acl` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead attempts to "adopt" it
into management. We can do this because each VPC created has a Default Network
ACL that cannot be destroyed, and is created with a known set of default rules.

When Terraform first adopts the Default Network ACL, it **immediately removes all
rules in the ACL**. It then proceeds to create any rules specified in the
configuration. This step is required so that only the rules specified in the
configuration are created.

This resource treats its inline rules as absolute; only the rules defined
inline are created, and any additions/removals external to this resource will
result in diffs being shown. For these reasons, this resource is incompatible with the
`aws_network_acl_rule` resource.

For more information about Network ACLs, see the AWS Documentation on
[Network ACLs][aws-network-acls].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DefaultNetworkAcl",
    "Properties" : {
        "<a href="#defaultnetworkaclid" title="DefaultNetworkAclId">DefaultNetworkAclId</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#egress" title="Egress">Egress</a>" : <i>[ <a href="egress.md">Egress</a>, ... ]</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="ingress.md">Ingress</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DefaultNetworkAcl
Properties:
    <a href="#defaultnetworkaclid" title="DefaultNetworkAclId">DefaultNetworkAclId</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#egress" title="Egress">Egress</a>: <i>
      - <a href="egress.md">Egress</a></i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="ingress.md">Ingress</a></i>
</pre>

## Properties

#### DefaultNetworkAclId

The Network ACL ID to manage. This
attribute is exported from `aws_vpc`, or manually found via the AWS Console.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

A list of Subnet IDs to apply the ACL to. See the
notes below on managing Subnets in the Default Network ACL.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No

_Type_: List of <a href="egress.md">Egress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of <a href="ingress.md">Ingress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

