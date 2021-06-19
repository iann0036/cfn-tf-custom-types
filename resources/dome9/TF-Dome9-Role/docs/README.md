# TF::Dome9::Role

The Role resource is used to create and manage Dome9 roles. Roles are used to manage access permissions for Dome9 users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::Role",
    "Properties" : {
        "<a href="#create" title="Create">Create</a>" : <i>[ String, ... ]</i>,
        "<a href="#crossaccountaccess" title="CrossAccountAccess">CrossAccountAccess</a>" : <i>[ String, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#permitalertactions" title="PermitAlertActions">PermitAlertActions</a>" : <i>Boolean</i>,
        "<a href="#permitnotifications" title="PermitNotifications">PermitNotifications</a>" : <i>Boolean</i>,
        "<a href="#permitonboarding" title="PermitOnBoarding">PermitOnBoarding</a>" : <i>Boolean</i>,
        "<a href="#permitpolicies" title="PermitPolicies">PermitPolicies</a>" : <i>Boolean</i>,
        "<a href="#permitrulesets" title="PermitRulesets">PermitRulesets</a>" : <i>Boolean</i>,
        "<a href="#access" title="Access">Access</a>" : <i>[ <a href="accessdefinition.md">AccessDefinition</a>, ... ]</i>,
        "<a href="#manage" title="Manage">Manage</a>" : <i>[ <a href="managedefinition.md">ManageDefinition</a>, ... ]</i>,
        "<a href="#view" title="View">View</a>" : <i>[ <a href="viewdefinition.md">ViewDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::Role
Properties:
    <a href="#create" title="Create">Create</a>: <i>
      - String</i>
    <a href="#crossaccountaccess" title="CrossAccountAccess">CrossAccountAccess</a>: <i>
      - String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#permitalertactions" title="PermitAlertActions">PermitAlertActions</a>: <i>Boolean</i>
    <a href="#permitnotifications" title="PermitNotifications">PermitNotifications</a>: <i>Boolean</i>
    <a href="#permitonboarding" title="PermitOnBoarding">PermitOnBoarding</a>: <i>Boolean</i>
    <a href="#permitpolicies" title="PermitPolicies">PermitPolicies</a>: <i>Boolean</i>
    <a href="#permitrulesets" title="PermitRulesets">PermitRulesets</a>: <i>Boolean</i>
    <a href="#access" title="Access">Access</a>: <i>
      - <a href="accessdefinition.md">AccessDefinition</a></i>
    <a href="#manage" title="Manage">Manage</a>: <i>
      - <a href="managedefinition.md">ManageDefinition</a></i>
    <a href="#view" title="View">View</a>: <i>
      - <a href="viewdefinition.md">ViewDefinition</a></i>
</pre>

## Properties

#### Create

Create permission list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossAccountAccess

Cross account access.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Dome9 role description.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Dome9 role name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitAlertActions

Is permitted permit alert actions (Optional) .

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitNotifications

Is permitted permit notifications (Optional) .

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitOnBoarding

Is permitted permit on boarding (Optional)  .

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitPolicies

Is permitted permit policies (Optional) .

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitRulesets

Is permitted permit rulesets (Optional) .

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Access

_Required_: No

_Type_: List of <a href="accessdefinition.md">AccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manage

_Required_: No

_Type_: List of <a href="managedefinition.md">ManageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

_Required_: No

_Type_: List of <a href="viewdefinition.md">ViewDefinition</a>

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

