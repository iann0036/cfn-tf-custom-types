# Terraform::Alicloud::NasMountTarget

Provides a Nas Mount Target resource.

-> NOTE: Available in v1.34.0+.

-> NOTE: Currently this resource support create a mount point in a classic network only when current region is China mainland regions.

-> NOTE: You must grant NAS with specific RAM permissions when creating a classic mount targets,
and it only can be achieved by creating a classic mount target mannually.
See [Add a mount point](https://www.alibabacloud.com/help/doc-detail/60431.htm) and [Why do I need RAM permissions to create a mount point in a classic network](https://www.alibabacloud.com/help/faq-detail/42176.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::NasMountTarget",
    "Properties" : {
        "<a href="#accessgroupname" title="AccessGroupName">AccessGroupName</a>" : <i>String</i>,
        "<a href="#filesystemid" title="FileSystemId">FileSystemId</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vswitchid" title="VswitchId">VswitchId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::NasMountTarget
Properties:
    <a href="#accessgroupname" title="AccessGroupName">AccessGroupName</a>: <i>String</i>
    <a href="#filesystemid" title="FileSystemId">FileSystemId</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vswitchid" title="VswitchId">VswitchId</a>: <i>String</i>
</pre>

## Properties

#### AccessGroupName

Permission group name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSystemId

File system ID.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Whether the MountTarget is active. An inactive MountTarget is inusable. Valid values are Active(default) and Inactive.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VswitchId

VSwitch ID.

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

