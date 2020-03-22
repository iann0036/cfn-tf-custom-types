# Terraform::Alicloud::NasAccessRule

Provides a Nas Access Rule resource.

When NAS is activated, the Default VPC Permission Group is automatically generated. It allows all IP addresses in a VPC to access the mount point with full permissions. Full permissions include Read/Write permission with no restriction on root users.

-> **NOTE:** Available in v1.34.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::NasAccessRule",
    "Properties" : {
        "<a href="#accessgroupname" title="AccessGroupName">AccessGroupName</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#rwaccesstype" title="RwAccessType">RwAccessType</a>" : <i>String</i>,
        "<a href="#sourcecidrip" title="SourceCidrIp">SourceCidrIp</a>" : <i>String</i>,
        "<a href="#useraccesstype" title="UserAccessType">UserAccessType</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::NasAccessRule
Properties:
    <a href="#accessgroupname" title="AccessGroupName">AccessGroupName</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#rwaccesstype" title="RwAccessType">RwAccessType</a>: <i>String</i>
    <a href="#sourcecidrip" title="SourceCidrIp">SourceCidrIp</a>: <i>String</i>
    <a href="#useraccesstype" title="UserAccessType">UserAccessType</a>: <i>String</i>
</pre>

## Properties

#### AccessGroupName

Permission group name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

Priority level. Range: 1-100. Default value: 1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RwAccessType

Read-write permission type: RDWR (default), RDONLY.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCidrIp

Address or address segment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserAccessType

User permission type: no_squash (default), root_squash, all_squash.

_Required_: No

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

#### AccessRuleId

Returns the <code>AccessRuleId</code> value.

#### Id

Returns the <code>Id</code> value.

