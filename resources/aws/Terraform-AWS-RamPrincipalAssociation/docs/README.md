# Terraform::AWS::RamPrincipalAssociation

Provides a Resource Access Manager (RAM) principal association. Depending if [RAM Sharing with AWS Organizations is enabled](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs), the RAM behavior with different principal types changes.

When RAM Sharing with AWS Organizations is enabled:

- For AWS Account ID, Organization, and Organizational Unit principals within the same AWS Organization, no resource share invitation is sent and resources become available automatically after creating the association.
- For AWS Account ID principals outside the AWS Organization, a resource share invitation is sent and must be accepted before resources become available. See the [`aws_ram_resource_share_accepter` resource](/docs/providers/aws/r/ram_resource_share_accepter.html) to accept these invitations.

When RAM Sharing with AWS Organizations is not enabled:

- Organization and Organizational Unit principals cannot be used.
- For AWS Account ID principals, a resource share invitation is sent and must be accepted before resources become available. See the [`aws_ram_resource_share_accepter` resource](/docs/providers/aws/r/ram_resource_share_accepter.html) to accept these invitations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::RamPrincipalAssociation",
    "Properties" : {
        "<a href="#principal" title="Principal">Principal</a>" : <i>String</i>,
        "<a href="#resourcesharearn" title="ResourceShareArn">ResourceShareArn</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::RamPrincipalAssociation
Properties:
    <a href="#principal" title="Principal">Principal</a>: <i>String</i>
    <a href="#resourcesharearn" title="ResourceShareArn">ResourceShareArn</a>: <i>String</i>
</pre>

## Properties

#### Principal

The principal to associate with the resource share. Possible values are an AWS account ID, an AWS Organizations Organization ARN, or an AWS Organizations Organization Unit ARN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceShareArn

The Amazon Resource Name (ARN) of the resource share.

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

#### Id

Returns the <code>Id</code> value.

