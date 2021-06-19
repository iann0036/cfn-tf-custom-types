# TF::AWS::DefaultNetworkAcl

Provides a resource to manage a VPC's default network ACL. This resource can manage the default network ACL of the default or a non-default VPC.

~> **NOTE:** This is an advanced resource with special caveats. Please read this document in its entirety before using this resource. The `aws_default_network_acl` behaves differently from normal resources. Terraform does not _create_ this resource but instead attempts to "adopt" it into management.

Every VPC has a default network ACL that can be managed but not destroyed. When Terraform first adopts the Default Network ACL, it **immediately removes all rules in the ACL**. It then proceeds to create any rules specified in the configuration. This step is required so that only the rules specified in the configuration are created.

This resource treats its inline rules as absolute; only the rules defined inline are created, and any additions/removals external to this resource will result in diffs being shown. For these reasons, this resource is incompatible with t...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DefaultNetworkAcl",
    "Properties" : {
        "<a href="#defaultnetworkaclid" title="DefaultNetworkAclId">DefaultNetworkAclId</a>" : <i>String</i>,
        "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#egress" title="Egress">Egress</a>" : <i>[ <a href="egressdefinition.md">EgressDefinition</a>, ... ]</i>,
        "<a href="#ingress" title="Ingress">Ingress</a>" : <i>[ <a href="ingressdefinition.md">IngressDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DefaultNetworkAcl
Properties:
    <a href="#defaultnetworkaclid" title="DefaultNetworkAclId">DefaultNetworkAclId</a>: <i>String</i>
    <a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#egress" title="Egress">Egress</a>: <i>
      - <a href="egressdefinition.md">EgressDefinition</a></i>
    <a href="#ingress" title="Ingress">Ingress</a>: <i>
      - <a href="ingressdefinition.md">IngressDefinition</a></i>
</pre>

## Properties

#### DefaultNetworkAclId

Network ACL ID to manage. This attribute is exported from `aws_vpc`, or manually found via the AWS Console.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

List of Subnet IDs to apply the ACL to. See the notes below on managing Subnets in the Default Network ACL.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Egress

_Required_: No

_Type_: List of <a href="egressdefinition.md">EgressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ingress

_Required_: No

_Type_: List of <a href="ingressdefinition.md">IngressDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

#### OwnerId

Returns the <code>OwnerId</code> value.

#### VpcId

Returns the <code>VpcId</code> value.

