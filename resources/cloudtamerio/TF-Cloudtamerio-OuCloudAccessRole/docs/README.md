# TF::Cloudtamerio::OuCloudAccessRole

CloudFormation equivalent of cloudtamerio_ou_cloud_access_role

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudtamerio::OuCloudAccessRole",
    "Properties" : {
        "<a href="#awsiampath" title="AwsIamPath">AwsIamPath</a>" : <i>String</i>,
        "<a href="#awsiampermissionsboundary" title="AwsIamPermissionsBoundary">AwsIamPermissionsBoundary</a>" : <i>Double</i>,
        "<a href="#awsiamrolename" title="AwsIamRoleName">AwsIamRoleName</a>" : <i>String</i>,
        "<a href="#lastupdated" title="LastUpdated">LastUpdated</a>" : <i>String</i>,
        "<a href="#longtermaccesskeys" title="LongTermAccessKeys">LongTermAccessKeys</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ouid" title="OuId">OuId</a>" : <i>Double</i>,
        "<a href="#shorttermaccesskeys" title="ShortTermAccessKeys">ShortTermAccessKeys</a>" : <i>Boolean</i>,
        "<a href="#webaccess" title="WebAccess">WebAccess</a>" : <i>Boolean</i>,
        "<a href="#awsiampolicies" title="AwsIamPolicies">AwsIamPolicies</a>" : <i>[ <a href="awsiampoliciesdefinition.md">AwsIamPoliciesDefinition</a>, ... ]</i>,
        "<a href="#usergroups" title="UserGroups">UserGroups</a>" : <i>[ <a href="usergroupsdefinition.md">UserGroupsDefinition</a>, ... ]</i>,
        "<a href="#users" title="Users">Users</a>" : <i>[ <a href="usersdefinition.md">UsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudtamerio::OuCloudAccessRole
Properties:
    <a href="#awsiampath" title="AwsIamPath">AwsIamPath</a>: <i>String</i>
    <a href="#awsiampermissionsboundary" title="AwsIamPermissionsBoundary">AwsIamPermissionsBoundary</a>: <i>Double</i>
    <a href="#awsiamrolename" title="AwsIamRoleName">AwsIamRoleName</a>: <i>String</i>
    <a href="#lastupdated" title="LastUpdated">LastUpdated</a>: <i>String</i>
    <a href="#longtermaccesskeys" title="LongTermAccessKeys">LongTermAccessKeys</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ouid" title="OuId">OuId</a>: <i>Double</i>
    <a href="#shorttermaccesskeys" title="ShortTermAccessKeys">ShortTermAccessKeys</a>: <i>Boolean</i>
    <a href="#webaccess" title="WebAccess">WebAccess</a>: <i>Boolean</i>
    <a href="#awsiampolicies" title="AwsIamPolicies">AwsIamPolicies</a>: <i>
      - <a href="awsiampoliciesdefinition.md">AwsIamPoliciesDefinition</a></i>
    <a href="#usergroups" title="UserGroups">UserGroups</a>: <i>
      - <a href="usergroupsdefinition.md">UserGroupsDefinition</a></i>
    <a href="#users" title="Users">Users</a>: <i>
      - <a href="usersdefinition.md">UsersDefinition</a></i>
</pre>

## Properties

#### AwsIamPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsIamPermissionsBoundary

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsIamRoleName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastUpdated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongTermAccessKeys

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OuId

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortTermAccessKeys

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WebAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsIamPolicies

_Required_: No

_Type_: List of <a href="awsiampoliciesdefinition.md">AwsIamPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserGroups

_Required_: No

_Type_: List of <a href="usergroupsdefinition.md">UserGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Users

_Required_: No

_Type_: List of <a href="usersdefinition.md">UsersDefinition</a>

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

