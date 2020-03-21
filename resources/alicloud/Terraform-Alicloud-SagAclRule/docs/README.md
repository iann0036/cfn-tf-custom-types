# Terraform::Alicloud::SagAclRule

Provides a Sag Acl Rule resource. This topic describes how to configure an access control list (ACL) rule for a target Smart Access Gateway instance to permit or deny access to or from specified IP addresses in the ACL rule.

For information about Sag Acl Rule and how to use it, see [What is access control list (ACL) rule](https://www.alibabacloud.com/help/doc-detail/111483.htm).

-> **NOTE:** Available in 1.60.0+

-> **NOTE:** Only the following regions support create Cloud Connect Network. [`cn-shanghai`, `cn-shanghai-finance-1`, `cn-hongkong`, `ap-southeast-1`, `ap-southeast-2`, `ap-southeast-3`, `ap-southeast-5`, `ap-northeast-1`, `eu-central-1`]

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SagAclRule",
    "Properties" : {
        "<a href="#aclid" title="AclId">AclId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#destcidr" title="DestCidr">DestCidr</a>" : <i>String</i>,
        "<a href="#destportrange" title="DestPortRange">DestPortRange</a>" : <i>String</i>,
        "<a href="#direction" title="Direction">Direction</a>" : <i>String</i>,
        "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#sourcecidr" title="SourceCidr">SourceCidr</a>" : <i>String</i>,
        "<a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SagAclRule
Properties:
    <a href="#aclid" title="AclId">AclId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#destcidr" title="DestCidr">DestCidr</a>: <i>String</i>
    <a href="#destportrange" title="DestPortRange">DestPortRange</a>: <i>String</i>
    <a href="#direction" title="Direction">Direction</a>: <i>String</i>
    <a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#sourcecidr" title="SourceCidr">SourceCidr</a>: <i>String</i>
    <a href="#sourceportrange" title="SourcePortRange">SourcePortRange</a>: <i>String</i>
</pre>

## Properties

#### AclId

The ID of the ACL.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the ACL rule. It must be 1 to 512 characters in length.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestCidr

The destination address. It is an IPv4 address range in CIDR format. Default value: 0.0.0.0/0.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestPortRange

The range of the destination port. Valid value: 80/80.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Direction

The direction of the ACL rule. Valid values: in|out.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

The protocol used by the ACL rule. The value is not case sensitive.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

The policy used by the ACL rule. Valid values: accept|drop.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority of the ACL rule. Value range: 1 to 100.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCidr

The source address. It is an IPv4 address range in the CIDR format. Default value: 0.0.0.0/0.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePortRange

The range of the source port. Valid value: 80/80.

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

