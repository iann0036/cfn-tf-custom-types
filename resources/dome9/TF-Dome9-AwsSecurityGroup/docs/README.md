# TF::Dome9::AwsSecurityGroup

This resource has methods to add and manage Security Groups in a cloud account that is managed by Dome9.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::AwsSecurityGroup",
    "Properties" : {
        "<a href="#awsregionid" title="AwsRegionId">AwsRegionId</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dome9cloudaccountid" title="Dome9CloudAccountId">Dome9CloudAccountId</a>" : <i>String</i>,
        "<a href="#dome9securitygroupname" title="Dome9SecurityGroupName">Dome9SecurityGroupName</a>" : <i>String</i>,
        "<a href="#isprotected" title="IsProtected">IsProtected</a>" : <i>Boolean</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcname" title="VpcName">VpcName</a>" : <i>String</i>,
        "<a href="#services" title="Services">Services</a>" : <i>[ <a href="servicesdefinition.md">ServicesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::AwsSecurityGroup
Properties:
    <a href="#awsregionid" title="AwsRegionId">AwsRegionId</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dome9cloudaccountid" title="Dome9CloudAccountId">Dome9CloudAccountId</a>: <i>String</i>
    <a href="#dome9securitygroupname" title="Dome9SecurityGroupName">Dome9SecurityGroupName</a>: <i>String</i>
    <a href="#isprotected" title="IsProtected">IsProtected</a>: <i>Boolean</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpcname" title="VpcName">VpcName</a>: <i>String</i>
    <a href="#services" title="Services">Services</a>: <i>
      - <a href="servicesdefinition.md">ServicesDefinition</a></i>
</pre>

## Properties

#### AwsRegionId

AWS region, in AWS format (e.g., "us-east-1"); default is us_east_1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Security Group description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dome9CloudAccountId

Cloud account id in Dome9.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dome9SecurityGroupName

Name of the Security Group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsProtected

Indicates the Security Group is in Protected mode.
* Note: to set the protection mode, first create the Security Group, then update it with the desired protection mode value ('true' for Protected).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Security Group tags.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

VPC id for VPC containing the Security Group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcName

Security Group VPC name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Services

_Required_: No

_Type_: List of <a href="servicesdefinition.md">ServicesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CloudAccountName

Returns the <code>CloudAccountName</code> value.

#### ExternalId

Returns the <code>ExternalId</code> value.

#### Id

Returns the <code>Id</code> value.

