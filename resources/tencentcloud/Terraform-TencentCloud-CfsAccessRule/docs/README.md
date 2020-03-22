# Terraform::TencentCloud::CfsAccessRule

Provides a resource to create a CFS access rule.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::TencentCloud::CfsAccessRule",
    "Properties" : {
        "<a href="#accessgroupid" title="AccessGroupId">AccessGroupId</a>" : <i>String</i>,
        "<a href="#authclientip" title="AuthClientIp">AuthClientIp</a>" : <i>String</i>,
        "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
        "<a href="#rwpermission" title="RwPermission">RwPermission</a>" : <i>String</i>,
        "<a href="#userpermission" title="UserPermission">UserPermission</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::TencentCloud::CfsAccessRule
Properties:
    <a href="#accessgroupid" title="AccessGroupId">AccessGroupId</a>: <i>String</i>
    <a href="#authclientip" title="AuthClientIp">AuthClientIp</a>: <i>String</i>
    <a href="#priority" title="Priority">Priority</a>: <i>Double</i>
    <a href="#rwpermission" title="RwPermission">RwPermission</a>: <i>String</i>
    <a href="#userpermission" title="UserPermission">UserPermission</a>: <i>String</i>
</pre>

## Properties

#### AccessGroupId

ID of a access group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthClientIp

A single IP or a single IP address range such as 10.1.10.11 or 10.10.1.0/24 indicates that all IPs are allowed. Please note that the IP entered should be CVM's private IP.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority level of rule. The range is 1-100, and 1 indicates the highest priority.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RwPermission

Read and write permissions. Valid values are `RO` and `RW`, and default is `RO`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserPermission

The permissions of accessing users. Valid values are `all_squash`, `no_all_squash`, `root_squash` and `no_root_squash`, and default is `root_squash`. `all_squash` indicates that all access users are mapped as anonymous users or user groups; `no_all_squash` indicates that access users will match local users first and be mapped to anonymous users or user groups after matching failed; `root_squash` indicates that map access root users to anonymous users or user groups; `no_root_squash` indicates that access root users keep root account permission.

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

#### Id

Returns the <code>Id</code> value.

