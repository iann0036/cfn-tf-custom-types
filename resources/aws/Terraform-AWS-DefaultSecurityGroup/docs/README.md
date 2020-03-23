# Terraform::AWS::DefaultSecurityGroup

Provides a resource to manage the default AWS Security Group.

For EC2 Classic accounts, each region comes with a Default Security Group.
Additionally, each VPC created in AWS comes with a Default Security Group that can be managed, but not
destroyed. **This is an advanced resource**, and has special caveats to be aware
of when using it. Please read this document in its entirety before using this
resource.

The `aws_default_security_group` behaves differently from normal resources, in that
Terraform does not _create_ this resource, but instead "adopts" it
into management. We can do this because these default security groups cannot be
destroyed, and are created with a known set of default ingress/egress rules.

When Terraform first adopts the Default Security Group, it **immediately removes all
ingress and egress rules in the Security Group**. It then proceeds to create any rules specified in the
configuration. This step is required so that only the rules specified in the
configuration are created.

This resource treats its inline rules as absolute; only the rules defined
inline are created, and any additions/removals external to this resource will
result in diff shown. For these reasons, this resource is incompatible with the
`aws_security_group_rule` resource.

For more information about Default Security Groups, see the AWS Documentation on
[Default Security Groups][aws-default-security-groups].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DefaultSecurityGroup",
    "Properties" : {
        "<a href="#egress" title="Egress">Egress</a>" : <i>[ <a href="egress.md">Egress</a>, ... ]</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="ingress.md">Ingress</a>, ... ]</i>,
        "<a href="#revokerulesondelete" title="RevokeRulesOnDelete">RevokeRulesOnDelete</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DefaultSecurityGroup
Properties:
    <a href="#egress" title="Egress">Egress</a>: <i>
      - <a href="egress.md">Egress</a></i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="ingress.md">Ingress</a></i>
    <a href="#revokerulesondelete" title="RevokeRulesOnDelete">RevokeRulesOnDelete</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### Egress

Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.

_Required_: No

_Type_: List of <a href="egress.md">Egress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.

_Required_: No

_Type_: List of <a href="ingress.md">Ingress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RevokeRulesOnDelete

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

The VPC ID. **Note that changing
the `vpc_id` will _not_ restore any default security group rules that were
modified, added, or removed.** It will be left in its current state.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Description

Returns the <code>Description</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

