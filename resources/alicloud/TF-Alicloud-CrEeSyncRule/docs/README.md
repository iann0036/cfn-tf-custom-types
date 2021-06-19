# TF::Alicloud::CrEeSyncRule

This resource will help you to manager Container Registry Enterprise Edition sync rules.

For information about Container Registry Enterprise Edition sync rules and how to use it, see [Create a Sync Rule](https://www.alibabacloud.com/help/doc-detail/145280.htm)

-> **NOTE:** Available in v1.90.0+.

-> **NOTE:** You need to set your registry password in Container Registry Enterprise Edition console before use this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CrEeSyncRule",
    "Properties" : {
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespacename" title="NamespaceName">NamespaceName</a>" : <i>String</i>,
        "<a href="#reponame" title="RepoName">RepoName</a>" : <i>String</i>,
        "<a href="#tagfilter" title="TagFilter">TagFilter</a>" : <i>String</i>,
        "<a href="#targetinstanceid" title="TargetInstanceId">TargetInstanceId</a>" : <i>String</i>,
        "<a href="#targetnamespacename" title="TargetNamespaceName">TargetNamespaceName</a>" : <i>String</i>,
        "<a href="#targetregionid" title="TargetRegionId">TargetRegionId</a>" : <i>String</i>,
        "<a href="#targetreponame" title="TargetRepoName">TargetRepoName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CrEeSyncRule
Properties:
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespacename" title="NamespaceName">NamespaceName</a>: <i>String</i>
    <a href="#reponame" title="RepoName">RepoName</a>: <i>String</i>
    <a href="#tagfilter" title="TagFilter">TagFilter</a>: <i>String</i>
    <a href="#targetinstanceid" title="TargetInstanceId">TargetInstanceId</a>: <i>String</i>
    <a href="#targetnamespacename" title="TargetNamespaceName">TargetNamespaceName</a>: <i>String</i>
    <a href="#targetregionid" title="TargetRegionId">TargetRegionId</a>: <i>String</i>
    <a href="#targetreponame" title="TargetRepoName">TargetRepoName</a>: <i>String</i>
</pre>

## Properties

#### InstanceId

ID of Container Registry Enterprise Edition source instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Container Registry Enterprise Edition sync rule.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceName

Name of Container Registry Enterprise Edition source namespace. It can contain 2 to 30 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoName

Name of the source repository which should be set together with `target_repo_name`, if empty means that the synchronization scope is the entire namespace level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagFilter

The regular expression used to filter image tags for synchronization in the source repository.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetInstanceId

ID of Container Registry Enterprise Edition target instance to be synchronized.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetNamespaceName

Name of Container Registry Enterprise Edition target namespace to be synchronized. It can contain 2 to 30 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRegionId

The target region to be synchronized.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetRepoName

Name of the target repository.

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

#### RuleId

Returns the <code>RuleId</code> value.

#### SyncDirection

Returns the <code>SyncDirection</code> value.

#### SyncScope

Returns the <code>SyncScope</code> value.

