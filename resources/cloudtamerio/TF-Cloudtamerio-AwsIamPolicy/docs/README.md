# TF::Cloudtamerio::AwsIamPolicy

CloudFormation equivalent of cloudtamerio_aws_iam_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudtamerio::AwsIamPolicy",
    "Properties" : {
        "<a href="#awsiampath" title="AwsIamPath">AwsIamPath</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#lastupdated" title="LastUpdated">LastUpdated</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#ownerusergroups" title="OwnerUserGroups">OwnerUserGroups</a>" : <i>[ <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a>, ... ]</i>,
        "<a href="#ownerusers" title="OwnerUsers">OwnerUsers</a>" : <i>[ <a href="ownerusersdefinition.md">OwnerUsersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudtamerio::AwsIamPolicy
Properties:
    <a href="#awsiampath" title="AwsIamPath">AwsIamPath</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#lastupdated" title="LastUpdated">LastUpdated</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#ownerusergroups" title="OwnerUserGroups">OwnerUserGroups</a>: <i>
      - <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a></i>
    <a href="#ownerusers" title="OwnerUsers">OwnerUsers</a>: <i>
      - <a href="ownerusersdefinition.md">OwnerUsersDefinition</a></i>
</pre>

## Properties

#### AwsIamPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastUpdated

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerUserGroups

_Required_: No

_Type_: List of <a href="ownerusergroupsdefinition.md">OwnerUserGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OwnerUsers

_Required_: No

_Type_: List of <a href="ownerusersdefinition.md">OwnerUsersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AwsManagedPolicy

Returns the <code>AwsManagedPolicy</code> value.

#### Id

Returns the <code>Id</code> value.

#### PathSuffix

Returns the <code>PathSuffix</code> value.

#### SystemManagedPolicy

Returns the <code>SystemManagedPolicy</code> value.

